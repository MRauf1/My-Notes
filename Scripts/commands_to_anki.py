#!/usr/bin/env python3
"""Convert the command reference files in Commands/*.yaml into an Anki .apkg.

Usage:
    python3 commands_to_anki.py [--output PATH]

Requires: PyYAML (`python-yaml`), genanki (`python-genanki`), Markdown
(`python-markdown`).

File format (one file per tool/language, e.g. Commands/git.yaml):

    deck: Commands::Git                 # optional, default "Commands::<Stem>"
    source: https://git-scm.com/docs    # optional file-level citation
    entries:
      - command: git reset --soft HEAD~1   # required, card front
        meaning: Undo the last commit, keeping its changes staged.  # required
        details: |                          # optional, Markdown
          `--mixed` (default) also unstages; `--hard` discards changes.
        example: git reset --soft HEAD~3    # optional, shown as code
        source: https://git-scm.com/docs/git-reset   # optional override
        tags: [reset]                       # optional

Card rules:
  - one card per entry: Front = command, Back = meaning + details +
    example + source.
  - the file stem is added as a tag to every card from that file.

Re-running after editing entries updates existing Anki cards in place
(matched by a stable ID derived from the file stem + command), instead of
creating duplicates. Changing the `command` text itself creates a new card.
"""

import argparse
import hashlib
import html
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
COMMANDS_DIR = VAULT_ROOT / "Commands"
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "output" / "Commands.apkg"

DEFAULT_DECK_PREFIX = "Commands"

MODEL_ID = 1793541106  # fixed so re-imports reuse the same note type
MODEL_NAME = "Command Reference"

TAG_INVALID_RE = re.compile(r"\s+")

CARD_CSS = """
.card {
    font-family: -apple-system, Helvetica, Arial, sans-serif;
    font-size: 20px;
    text-align: left;
    line-height: 1.4;
}
.topic {
    opacity: 0.6;
    font-size: 14px;
    margin-bottom: 8px;
}
.command {
    font-family: "JetBrains Mono", "Fira Code", monospace;
    font-size: 22px;
    white-space: pre-wrap;
}
.meaning {
    font-weight: bold;
}
.label {
    margin-top: 12px;
    opacity: 0.6;
    font-size: 14px;
}
pre {
    background-color: rgba(128, 128, 128, 0.2);
    padding: 6px 10px;
    border-radius: 4px;
    white-space: pre-wrap;
}
code {
    font-family: "JetBrains Mono", "Fira Code", monospace;
    background-color: rgba(128, 128, 128, 0.2);
    padding: 1px 4px;
    border-radius: 3px;
}
pre code {
    background-color: transparent;
    padding: 0;
}
.source {
    margin-top: 12px;
    opacity: 0.6;
    font-size: 14px;
    font-style: italic;
}
"""


def stable_id(text: str) -> int:
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:15], 16)


def format_tag(tag: str) -> str:
    return tag.replace("_", " ").replace("-", " ").strip().title()


def anki_tag(tag: str) -> str:
    return TAG_INVALID_RE.sub("_", str(tag).strip())


def render_markdown(text: str) -> str:
    return markdown.markdown(text.strip(), extensions=["fenced_code", "sane_lists"])


def render_source(source: str) -> str:
    source = str(source).strip()
    escaped = html.escape(source)
    if source.startswith(("http://", "https://")):
        return f'<a href="{escaped}">{escaped}</a>'
    return escaped


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


def build_front(topic: str, command: str) -> str:
    return (
        f'<div class="topic">{html.escape(topic)}</div>'
        f'<div class="command">{html.escape(command)}</div>'
    )


def build_back(entry: dict, default_source) -> str:
    parts = [f'<div class="meaning">{render_markdown(str(entry["meaning"]))}</div>']
    details = entry.get("details")
    if details:
        parts.append(render_markdown(str(details)))
    example = entry.get("example")
    if example:
        parts.append('<div class="label">Example</div>')
        parts.append(f"<pre><code>{html.escape(str(example).strip())}</code></pre>")
    source = entry.get("source") or default_source
    if source:
        parts.append(f'<div class="source">Source: {render_source(source)}</div>')
    return "\n".join(parts)


def load_file(path: Path, errors: list):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        errors.append(f"{path.name}: invalid YAML: {e}")
        return None
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        errors.append(f"{path.name}: expected a mapping with an 'entries' list")
        return None
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not COMMANDS_DIR.is_dir():
        sys.exit(f"No commands directory found at {COMMANDS_DIR}")

    model = make_model()
    decks = {}  # full_name -> genanki.Deck
    errors = []
    counts = {"files": 0, "cards": 0}

    def get_deck(full_name):
        if full_name not in decks:
            decks[full_name] = genanki.Deck(stable_id(full_name), full_name)
        return decks[full_name]

    for path in sorted(COMMANDS_DIR.glob("*.y*ml")):
        data = load_file(path, errors)
        if data is None:
            continue
        stem = path.stem
        deck_name = data.get("deck") or f"{DEFAULT_DECK_PREFIX}::{format_tag(stem)}"
        topic = deck_name.split("::")[-1]
        deck = get_deck(deck_name)
        default_source = data.get("source")
        seen = set()

        for idx, entry in enumerate(data["entries"]):
            if not isinstance(entry, dict):
                errors.append(f"{path.name}: entry #{idx + 1} is not a mapping")
                continue
            command = str(entry.get("command") or "").strip()
            if not command:
                errors.append(f"{path.name}: entry #{idx + 1} has no 'command'")
                continue
            if not str(entry.get("meaning") or "").strip():
                errors.append(f"{path.name}: '{command}' has no 'meaning'")
                continue
            if command in seen:
                errors.append(f"{path.name}: duplicate command '{command}'")
                continue
            seen.add(command)

            tags = [anki_tag(stem)] + [anki_tag(t) for t in entry.get("tags") or []]
            note = genanki.Note(
                model=model,
                fields=[build_front(topic, command), build_back(entry, default_source)],
                guid=genanki.guid_for(f"{stem}::{command}"),
                tags=tags,
            )
            deck.add_note(note)
            counts["cards"] += 1
        counts["files"] += 1

    if errors:
        for e in errors:
            print("ERROR:", e)
        sys.exit("Fix the errors above; no package was written.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    package = genanki.Package(list(decks.values()))
    package.write_to_file(str(args.output))

    print(f"Wrote {args.output}")
    print(f"Files processed: {counts['files']}")
    print(f"Decks: {len(decks)}")
    print(f"Cards generated: {counts['cards']}")


if __name__ == "__main__":
    main()
