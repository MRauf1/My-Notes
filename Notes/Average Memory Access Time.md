---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Average Memory Access Time (AMAT)[^1]
> A single figure of merit for comparing cache designs that accounts for both hits and misses:
> $$
> \text{AMAT} = \text{Hit Time} + \text{Miss Rate} \times \text{Miss Penalty}.
> $$

# Properties
- Captures the trade-off central to [[Memory Hierarchy|memory hierarchy]] design: a change that lowers the miss rate (such as increasing [[Set-Associative Cache|associativity]] or block size) often raises the hit time or miss penalty, so no single parameter change is guaranteed to improve overall performance.
- Complements the [[Three Cs Model]], which explains why misses occur, by quantifying their aggregate cost.
- Pitfall: using AMAT to evaluate the memory hierarchy of an out-of-order processor can mislead, since such a processor can often hide part of a miss's latency behind other useful work, weakening the direct link between AMAT and actual execution time.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=425&annotation=R236GC6L)
