---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Unicode[^1]
> A universal [[Character Encoding|character-encoding]] standard that defines and assigns enough character codes — called code points — to represent almost every natural language in use, plus a large set of symbols and emojis, solving the problem that some alphabets have too many characters to fit in a single byte-sized code.

# Properties
- Code points are just integers, of arbitrary size, each standing for one character[^1].
- Also defines standard, platform- and language-neutral encodings — such as [[UTF-8]] — that map these code points to and from sequences of bytes for storage and transmission[^2].
- Earlier, narrower schemes fall entirely under the Unicode umbrella, unchanged, as one of its possible encodings[^3].
- In Python 3, a script's ordinary [[Python String|string]] type is Unicode text by definition, not an optional add-on, making Unicode required knowledge rather than a specialized topic[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1438&annotation=YFE4ZRZH)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1438&annotation=VIDGV668)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1438&annotation=H35YCJ6P)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1435&annotation=Q4Q2E2MS)
