---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Prefetching[^1]
> A technique in which blocks of data expected to be needed in the future are brought into a [[Cache Memory|cache]] early, using special instructions that name the address of the block to fetch.

# Properties
- Aims to hide the [[Memory Hierarchy|miss penalty]] of an access whose need can be anticipated ahead of time, rather than reducing the number of eventual misses outright.
- A software-driven complement to hardware techniques like a nonblocking [[Cache Memory|cache]], which instead tolerates a miss already in progress rather than avoiding it in advance.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=505&annotation=G3VUVBJG)
