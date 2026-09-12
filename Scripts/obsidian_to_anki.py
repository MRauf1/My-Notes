#!/usr/bin/env python3
"""Convert the Obsidian vault's Notes/ into an Anki .apkg deck package.

Usage:
    python3 obsidian_to_anki.py [--output PATH]

Requires: PyYAML (`python-yaml`), genanki (`python-genanki`), Markdown
(`python-markdown`, already installed on this system).

Deck rules:
  - tags: [<domain>, <subdomain>, ...] -> Deck "<Domain>::<Subdomain>"
  - the 'anki' tag is ignored everywhere (marker tag, not a domain)
  - any note carrying the 'review' tag -> Deck "Review", regardless of
    its other tags; split into one card per paragraph
  - notes with 1 remaining tag -> Deck "<Domain>" (no subdeck)
  - notes with 0 remaining tags -> Deck "Uncategorized"
  - only the first two (non-'anki') tags are used for domain/subdomain

Card rules:
  - normal notes: one card per top-level ("# ") Markdown header.
    Front = "<Note Title> - <Header>", Back = that section's content.
  - notes with no top-level header at all: one card for the whole note.
    Front = "<Note Title>", Back = whole body.
  - review notes: one card per paragraph. Front = "<Note Title>" for
    every card from that note, Back = that paragraph.

Re-running after editing notes updates existing Anki cards in place
(matched by a stable ID derived from the note path + header/paragraph),
instead of creating duplicates. Nothing outside vault-derived decks/notes
is ever touched.
"""

import argparse
import hashlib
import html
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit(
        "Missing dependency 'yaml'. Install it first:\n"
        "  sudo pacman -S python-yaml"
    )

try:
    import genanki
except ImportError:
    sys.exit(
        "Missing dependency 'genanki'. Install it first:\n"
        "  yay -S python-genanki"
    )

import markdown

VAULT_ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = VAULT_ROOT / "Notes"
MEDIA_DIR = VAULT_ROOT / "Media"
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "output" / "ObsidianVault.apkg"

EXCLUDED_DIR_NAMES = {"Personal", "Gamification", "Unneeded"}

MARKER_TAG = "anki"
REVIEW_TAG = "review"
UNCATEGORIZED_DECK = "Uncategorized"
REVIEW_DECK = "Review"

MODEL_ID = 1607392319  # fixed so re-imports reuse the same note type
MODEL_NAME = "Obsidian Vault Basic"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
TOP_HEADER_RE = re.compile(r"^# (.+)$", re.MULTILINE)
ANY_HEADER_LINE_RE = re.compile(r"^#+ .*$", re.MULTILINE)
FOOTNOTE_DEF_RE = re.compile(r"^\[\^[^\]]+\]:.*$", re.MULTILINE)
FOOTNOTE_REF_RE = re.compile(r"\[\^[^\]]+\]")
IMAGE_EMBED_RE = re.compile(r"!\[\[([^\]]+?)\]\]")
WIKILINK_ALIASED_RE = re.compile(r"\[\[([^\]|]+)\|([^\]]+)\]\]")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
CALLOUT_START_RE = re.compile(r"^>\s*\[!(\w+)\]([-+]?)\s*(.*)$")
ORDERED_LIST_FIX_RE = re.compile(r"^([ \t]*)(\d+)\)\s+", re.MULTILINE)
ORDERED_MARKER_RE = re.compile(r"^[ \t]*\d+[.)]\s")
UNORDERED_MARKER_RE = re.compile(r"^[ \t]*[-*+]\s")
BLOCK_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
INLINE_MATH_RE = re.compile(r"\$([^\$\n]+?)\$")

CARD_CSS = """
.card {
    font-family: -apple-system, Helvetica, Arial, sans-serif;
    font-size: 20px;
    text-align: left;
    line-height: 1.4;
}
.callout {
    border-left: 4px solid #7c93c0;
    padding: 6px 12px;
    margin: 8px 0;
}
.source {
    margin-top: 12px;
    opacity: 0.6;
    font-size: 14px;
    font-style: italic;
}
code {
    background-color: rgba(128, 128, 128, 0.2);
    padding: 1px 4px;
    border-radius: 3px;
}
"""


def stable_id(text: str) -> int:
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:15], 16)


def format_tag(tag: str) -> str:
    return tag.replace("_", " ").replace("-", " ").strip().title()


def parse_frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return [], text
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        data = {}
    raw_tags = data.get("tags") or []
    if isinstance(raw_tags, str):
        raw_tags = [raw_tags]
    tags = [str(t).strip() for t in raw_tags if str(t).strip()]
    body = text[m.end():]
    return tags, body


def compute_deck_name(tags):
    filtered = [t for t in tags if t != MARKER_TAG]
    if REVIEW_TAG in filtered:
        return REVIEW_DECK
    if len(filtered) == 0:
        return UNCATEGORIZED_DECK
    if len(filtered) == 1:
        return format_tag(filtered[0])
    return f"{format_tag(filtered[0])}::{format_tag(filtered[1])}"


def strip_footnotes(body: str) -> str:
    body = FOOTNOTE_DEF_RE.sub("", body)
    body = FOOTNOTE_REF_RE.sub("", body)
    return body


def convert_images(text: str, media_used: set) -> str:
    def repl(m):
        filename = m.group(1).strip()
        if (MEDIA_DIR / filename).is_file():
            media_used.add(filename)
            return f"![]({filename})"
        return ""  # missing media file, drop silently

    return IMAGE_EMBED_RE.sub(repl, text)


def convert_wikilinks(text: str) -> str:
    text = WIKILINK_ALIASED_RE.sub(lambda m: m.group(2).strip(), text)
    text = WIKILINK_RE.sub(lambda m: m.group(1).split("#")[0].strip(), text)
    return text


def wrap_callouts(text: str) -> str:
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        m = CALLOUT_START_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        title = m.group(3).strip()
        i += 1
        block = []
        while i < len(lines) and lines[i].startswith(">"):
            content = lines[i][1:]
            if content.startswith(" "):
                content = content[1:]
            block.append(content)
            i += 1
        inner = "\n".join(block).strip()
        title_part = f"**{title}**\n\n" if title else ""
        out.append(f'<div class="callout" markdown="1">\n\n{title_part}{inner}\n\n</div>')
    return "\n".join(out)


def marker_type(line: str):
    if ORDERED_MARKER_RE.match(line):
        return "ordered"
    if UNORDERED_MARKER_RE.match(line):
        return "unordered"
    return None


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" \t"))


def ensure_blank_lines_before_lists(text: str) -> str:
    """python-markdown (unlike Obsidian's CommonMark renderer) needs a blank
    line before a list interrupts a paragraph, and needs one between two
    adjacent top-level lists of different marker types (ordered vs bullet) or
    it silently merges them into a single run-on paragraph/list item."""
    lines = text.split("\n")
    out = []
    for line in lines:
        mtype = marker_type(line)
        if mtype is not None and indent_of(line) == 0 and out and out[-1].strip() != "":
            prev_type = marker_type(out[-1])
            if prev_type != mtype:
                out.append("")
        out.append(line)
    return "\n".join(out)


def protect_math(text: str):
    placeholders = {}

    def make_placeholder(latex_html):
        key = f"MATHPLACEHOLDER{len(placeholders)}ENDPLACEHOLDER"
        placeholders[key] = latex_html
        return key

    text = BLOCK_MATH_RE.sub(lambda m: make_placeholder(f"\\[{m.group(1).strip()}\\]"), text)
    text = INLINE_MATH_RE.sub(lambda m: make_placeholder(f"\\({m.group(1).strip()}\\)"), text)
    return text, placeholders


def restore_math(rendered_html: str, placeholders: dict) -> str:
    for key, value in placeholders.items():
        rendered_html = rendered_html.replace(key, value)
    return rendered_html


def render_section_html(raw_text: str, media_used: set) -> str:
    text = raw_text.strip()
    if not text:
        return ""
    text = convert_images(text, media_used)
    text = convert_wikilinks(text)
    text = wrap_callouts(text)
    text = ORDERED_LIST_FIX_RE.sub(r"\1\2. ", text)
    text = ensure_blank_lines_before_lists(text)
    text, placeholders = protect_math(text)
    rendered_html = markdown.markdown(text, extensions=["md_in_html", "sane_lists"])
    rendered_html = restore_math(rendered_html, placeholders)
    return rendered_html


def split_top_level_headers(body: str):
    matches = list(TOP_HEADER_RE.finditer(body))
    if not matches:
        return None
    sections = []
    for idx, m in enumerate(matches):
        header = m.group(1).strip()
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections.append((header, body[start:end]))
    return sections


def split_paragraphs(body: str):
    body = ANY_HEADER_LINE_RE.sub("", body)
    raw_paragraphs = re.split(r"\n\s*\n", body)
    return [p.strip() for p in raw_paragraphs if p.strip()]


def make_model() -> genanki.Model:
    return genanki.Model(
        MODEL_ID,
        MODEL_NAME,
        fields=[{"name": "Front"}, {"name": "Back"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Front}}",
                "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
            }
        ],
        css=CARD_CSS,
    )


def build_note(model, guid_key, front_html, back_body_html, source_label):
    back_html = f'{back_body_html}<div class="source">Source: {source_label}</div>'
    note = genanki.Note(
        model=model,
        fields=[front_html, back_html],
        guid=genanki.guid_for(guid_key),
    )
    return note


def iter_note_files():
    for root, dirs, files in os.walk(NOTES_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIR_NAMES]
        for fname in sorted(files):
            if fname.endswith(".md"):
                yield Path(root) / fname


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    model = make_model()
    decks = {}  # full_name -> genanki.Deck
    media_used = set()
    warnings = []

    counts = {"cards": 0, "notes_processed": 0, "notes_skipped_empty": 0}

    def get_deck(full_name):
        if full_name not in decks:
            decks[full_name] = genanki.Deck(stable_id(full_name), full_name)
        return decks[full_name]

    for path in iter_note_files():
        rel_path = path.relative_to(NOTES_DIR).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        tags, body = parse_frontmatter(text)
        body = strip_footnotes(body)
        note_title = html.escape(path.stem)
        deck_name = compute_deck_name(tags)
        deck = get_deck(deck_name)
        is_review = REVIEW_TAG in [t for t in tags if t != MARKER_TAG]

        if is_review:
            paragraphs = split_paragraphs(body)
            if not paragraphs:
                counts["notes_skipped_empty"] += 1
                continue
            for idx, para in enumerate(paragraphs):
                back_html = render_section_html(para, media_used)
                if not back_html:
                    continue
                note = build_note(
                    model,
                    guid_key=f"{rel_path}::para::{idx}",
                    front_html=note_title,
                    back_body_html=back_html,
                    source_label=note_title,
                )
                deck.add_note(note)
                counts["cards"] += 1
            counts["notes_processed"] += 1
            continue

        sections = split_top_level_headers(body)
        if sections is None:
            back_html = render_section_html(body, media_used)
            if not back_html:
                counts["notes_skipped_empty"] += 1
                continue
            note = build_note(
                model,
                guid_key=f"{rel_path}::whole",
                front_html=note_title,
                back_body_html=back_html,
                source_label=note_title,
            )
            deck.add_note(note)
            counts["cards"] += 1
            counts["notes_processed"] += 1
            continue

        any_card = False
        for header, section_body in sections:
            back_html = render_section_html(section_body, media_used)
            if not back_html:
                continue
            front_html = f"{note_title} - {html.escape(header)}"
            note = build_note(
                model,
                guid_key=f"{rel_path}::{header}",
                front_html=front_html,
                back_body_html=back_html,
                source_label=note_title,
            )
            deck.add_note(note)
            counts["cards"] += 1
            any_card = True
        if any_card:
            counts["notes_processed"] += 1
        else:
            counts["notes_skipped_empty"] += 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    media_files = [str(MEDIA_DIR / name) for name in sorted(media_used)]
    package = genanki.Package(list(decks.values()), media_files=media_files)
    package.write_to_file(str(args.output))

    print(f"Wrote {args.output}")
    print(f"Decks: {len(decks)}")
    print(f"Notes processed: {counts['notes_processed']}")
    print(f"Notes skipped (empty/no content): {counts['notes_skipped_empty']}")
    print(f"Cards generated: {counts['cards']}")
    print(f"Media files bundled: {len(media_files)}")
    for w in warnings:
        print("WARNING:", w)


if __name__ == "__main__":
    main()
