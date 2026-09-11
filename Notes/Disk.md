---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Disk[^1]
> The storage medium that backs a [[Filesystem]].

# Types
- Hard disk drive (HDD) — includes a spinning metallic platter and a head that magnetizes the platter to encode a 1 or a 0.
- Solid-state drive (SSD) — encodes a 1 or a 0 by flipping NAND gates on a chip or standalone drive.

# Properties
- An SSD's [[Partition Alignment|partition alignment]] relative to its native read-chunk size (typically 4096 bytes) significantly affects performance, since a misaligned read may cost two reads instead of one.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=277&annotation=UTTQBSTA)
