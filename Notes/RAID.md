---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] RAID[^1]
> A scheme for combining multiple [[Disk|disks]] into a single logical storage unit, trading among redundancy, performance, and cost per byte.

# Types
- RAID-0 (striping) — splits a file's data across multiple disks, letting different parts of a write proceed on different disks in parallel and roughly halving write time with two disks, at the cost of losing the entire file if any one disk in the array fails.[^2]
- RAID-1 (mirroring) — duplicates every write across a backup disk, keeping two full copies of the data; reads are faster since either disk can serve them, but writes are roughly twice as slow, since both disks must be written, and the storage cost per byte doubles. If one disk fails, the other still holds a complete copy until it is re-cloned.[^1]
- RAID-10 — nests RAID-0 striping on top of pairs of RAID-1 mirrors, combining RAID-0's speed with RAID-1's per-disk redundancy; any single disk can fail without data loss, with some chance of surviving two failures if they occur on opposing mirrored pairs, though this cannot be relied upon.[^3]

# Properties
- An application of [[Dependability via Redundancy]] to disk storage.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=298&annotation=WER7PDNM)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=298&annotation=UQZ8EFW6)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=299&annotation=5I747KIL)
