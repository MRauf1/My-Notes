---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Memory Address[^1]
> A value used to delineate the location of a specific data element within a memory array. [[Main Memory]] is a large, single-dimensional array, and the address acts as the index into that array, starting at 0.

# Properties
- Unlike general signed numbers, addresses naturally start at 0 and never go negative.
- Virtually all architectures today address individual bytes, so the address of a [[Word (Computer Architecture)|word]] equals the address of one of its bytes, and sequential word addresses differ by 4, not 1.
- Whether the address of a multi-byte word refers to its leftmost ("big end") or rightmost ("little end") byte is a choice of [[Endianness]].
- Used by [[Data Transfer Instruction|data transfer instructions]] to locate data in memory, and computed via an [[Addressing Mode]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=91&annotation=EKTVT5T8)
