---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Cache Write Policy[^1]
> The scheme a [[Cache Memory|cache]] uses to keep itself consistent with the lower level of the [[Memory Hierarchy]] when the processor writes data.

# Types
- Write-through — every write updates both the cache and the next lower level immediately, keeping the two always consistent, but performs poorly unless paired with a write buffer.
- Write-back — a write updates only the block in the cache; the modified ("dirty") block is written to the lower level only when it is later replaced. More complex than write-through but performs better when writes can be generated as fast as, or faster than, main memory can absorb them, and is the only practical option for [[Virtual Memory|virtual memory]], since disk transfer time is small relative to disk access time, so batching an entire page's writes into one write-back is far more efficient than writing individual words.

# Properties
- A write buffer is a queue that holds data waiting to be written to memory under write-through, letting the processor continue past the write itself; the processor stalls only if the buffer fills faster than memory can drain it, which can still happen in write bursts even when the average write rate is within the memory system's capacity — mitigated by making the buffer deeper.
- A dirty bit records whether a write-back block has been modified since it was loaded, so the cache (or, in a [[Page Table|page table]] entry, the operating system) knows whether the block must be written back before its location can be reused.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=416&annotation=VVDJ29ZD)
