---
tags:
  - computer_science
  - python
---

# Definition
> [!info] UTF-8[^1]
> A variable-length [[Unicode]] encoding: character codes below 128 are represented as a single byte, codes from 128 up to `0x7ff` (2047) become two bytes, and codes above `0x7ff` become three- or four-byte sequences — with every byte of a multi-byte sequence falling in the range 128-255.

# Properties
- Keeps plain ASCII text compact (still one byte per character), sidesteps byte-ordering issues, and avoids null (zero) bytes that can cause problems for C libraries and networking code[^1].
- Restricting every byte of a multi-byte sequence to 128-255, rather than the full 0-255, is what makes UTF-8 self-synchronizing: because plain ASCII bytes always fall in 0-127, any byte with its top bit set unambiguously signals that it belongs to a multi-byte character, letting a reader tell single-byte and multi-byte characters apart without additional context.
- One of several alternative Unicode encodings — alongside plain ASCII and Latin-1 — that all decode back to the exact same Unicode code-point text, so the choice of encoding is a storage/transmission detail rather than a difference in the text itself[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1440&annotation=IY8SXE6E)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1441&annotation=84XQ7U5Q)
