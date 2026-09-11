---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Endianness[^1]
> The convention determining whether the address of a multi-byte word refers to its leftmost ("big end") or rightmost ("little end") byte. Computers divide into big-endian architectures, which use the big-end byte as the word address, and little-endian architectures, which use the little-end byte; MIPS is big-endian.

# Properties
- Only matters when the identical data is accessed both as a whole [[Word (Computer Architecture)|word]] and as its individual bytes, so few programmers need to be aware of it in practice.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=93&annotation=PPXCFCJR)
