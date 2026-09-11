---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Partition Alignment[^1]
> Partition alignment is the placement of a [[Partition (Operating Systems)|partition]] and its data relative to a [[Disk|solid-state drive's]] native read-chunk boundaries (typically 4096 bytes), within which every read must begin at a multiple of the chunk size.

# Properties
- If a partition's data does not lie on a 4096-byte boundary, small, common operations such as reading a directory's contents may require two reads instead of one.
- One of the most significant factors affecting SSD performance.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=97&annotation=2YMJQIEE)
