---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Memory Hierarchy[^1]
> Architects address the conflicting demands of memory speed, size, and cost with a hierarchy of memories: the fastest, smallest, and most expensive memory per bit sits at the top of the hierarchy, and the slowest, largest, and cheapest memory per bit sits at the bottom.

# Types
- [[Cache Memory]] — a small, fast buffer between the processor and [[Main Memory]].
- [[Main Memory]] (primary memory) — volatile storage, typically DRAM, holding running programs and their data.
- [[Secondary Memory]] — nonvolatile storage used to hold programs and data between runs.

# Properties
- One of the [[Great Ideas in Computer Architecture]].
- Exploiting the [[Principle of Locality|locality]] of memory accesses through this hierarchy is one of the two key ideas (with exploiting parallelism) that computer architects use to improve performance.
- Although a hierarchy can have many levels, data moves between only two adjacent levels at a time, so analysis can focus on a single upper/lower pair: the upper level (closer to the processor) is smaller, faster, and built from more expensive technology, while the lower level is larger, slower, and cheaper per bit.
- A request found in the upper level is a hit; one not found there is a miss, which is serviced by fetching the containing block from the lower level. The hit rate (miss rate) is the fraction of accesses found (not found) in a given level; the hit time is the time to access a level, including determining hit or miss; the miss penalty is the time to fetch a missing block from the lower level, insert it, and pass it to the requester — always much larger than the hit time, which is why a high hit rate lets the whole hierarchy behave almost as if it had the access time of its fastest level and the size of its largest.
- In most systems the hierarchy is inclusive: data cannot be present at level $i$ unless it is also present at level $i+1$.
- [[Virtual Memory]] applies the very same hierarchy concept one level further down, between main memory and secondary storage.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=35&annotation=HTFV3JTS)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=399&annotation=RNMMKPSF)
