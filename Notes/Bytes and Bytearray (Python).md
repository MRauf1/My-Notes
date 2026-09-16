---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Bytes and Bytearray (Python)[^1]
> Python's two binary [[Object (Python)|object]] types, used alongside [[Python String|str]] to represent content: `bytes` holds raw byte values — including text still in its [[Encoding and Decoding|encoded]] form — and `bytearray` is a mutable flavor of the same thing.

# Properties
- Together with `str` (Unicode text, i.e., already-decoded code points), these three types cleanly split a script's textual and binary data: `str` for text already decoded into characters, and `bytes`/`bytearray` for raw, still-encoded, byte-level data[^1].
- Like other [[Mutability (Python)|mutable]] types, `bytearray` can be changed in place, whereas `bytes`, like `str`, cannot.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1442&annotation=PZ9UU6DY)
