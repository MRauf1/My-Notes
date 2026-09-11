---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Cache Memory[^1]
> A small, fast memory that acts as a buffer for a slower, larger memory. In a computer, cache memory buffers the slower [[Main Memory|DRAM main memory]] and is built using static random access memory (SRAM).

# Properties
- A layer of the [[Memory Hierarchy]], sitting above [[Main Memory]].
- SRAM is faster but less dense, and hence more expensive per bit, than the DRAM used for [[Main Memory]]; SRAM needs no refresh, so its access time sits very close to its cycle time.
- Organized into blocks (lines), the minimum unit of information that can be present or absent in the cache; every block carries a tag, an address field identifying which memory block it holds, and a valid bit marking whether its contents are meaningful.
- Placement of a block within the cache follows one of the schemes described in [[Direct-Mapped Cache]] and [[Set-Associative Cache]].
- A larger block size exploits [[Principle of Locality|spatial locality]] to lower the miss rate and reduces relative tag storage overhead, but increases the miss penalty (more data to transfer per miss) and, past some point, raises the miss rate again as fewer distinct blocks fit and useful data gets evicted before it is reused.
- Modern processors typically use a split cache, separate instruction and data caches operating in parallel, to match cache bandwidth to what a pipeline demands, even though a single combined cache of equal total size usually achieves a better hit rate; see [[Multilevel Cache]] for adding further cache levels below the first.
- Caching is a direct application of the big idea of prediction: it relies on the [[Principle of Locality]] to guess that recently or nearby accessed data will be wanted next, and falls back to the lower level of the hierarchy whenever that guess (a cache miss) is wrong; see [[Cache Write Policy]] for how writes are kept consistent with lower levels, and [[Average Memory Access Time]] and [[Three Cs Model]] for evaluating cache performance.
- A nonblocking cache lets the processor keep making cache references while an earlier miss is still being serviced, rather than stalling the whole pipeline as a simple in-order design would.
- Prefetching brings blocks into the cache before they are needed, using special instructions that name the address to fetch, to hide the miss penalty for accesses whose need can be anticipated ahead of time.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=44&annotation=DZUJKRLD)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=399&annotation=UGY2DSVR)
