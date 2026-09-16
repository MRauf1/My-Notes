---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Python String[^1]
> An immutable [[Sequence (Python)|sequence]] of Unicode code points, used to represent text.

# Properties
- Immutable like all [[Mutability (Python)|immutable objects]]: every string operation produces a new string rather than changing the original in place.
- String literals may be enclosed in single or double quotes interchangeably, or in triple quotes (single or double) to span multiple lines, with newline characters inserted at each line break — useful for embedding multiline text or documentation strings[^2].
- A raw string, prefixed with `r`, turns off the backslash escape mechanism, which is useful for regular-expression patterns and Windows file paths[^3].
- Length is measured in characters (code points), not bytes, and no special character terminates a string the way a null byte does in C — Python tracks the string's length directly[^4].
- Comes with full Unicode support for processing non-ASCII text[^5].
- Represents already-decoded text; raw or still-encoded byte data instead uses Python's [[Bytes and Bytearray (Python)|bytes and bytearray]] types.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=218&annotation=24KUILZ9)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=111&annotation=UUFKCKQ7)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=111&annotation=MXMC5FFE)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=221&annotation=BWXBHGK6)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=111&annotation=ZXCF83AK)
