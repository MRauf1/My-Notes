---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Amdahl's Law[^1]
> A rule stating that the performance enhancement possible from a given improvement is limited by the fraction of execution time during which the improved feature is used. It is a quantitative version of the law of diminishing returns. If an improvement speeds up a fraction $F_{enhanced}$ of the original execution time by a factor $S_{enhanced}$, the new execution time is
> $$
> T_{new} = T_{old}\left[(1 - F_{enhanced}) + \frac{F_{enhanced}}{S_{enhanced}}\right],
> $$
> so the overall speedup is
> $$
> \text{Speedup}_{overall} = \frac{T_{old}}{T_{new}} = \frac{1}{(1 - F_{enhanced}) + \dfrac{F_{enhanced}}{S_{enhanced}}}.
> $$

# Properties
- Used together with the [[CPU Performance Equation]] to evaluate potential hardware or software enhancements when the time consumed by the affected function and its potential speedup are known.
- Explains why speeding up only a small fraction of a program yields only a small overall improvement, no matter how large $S_{enhanced}$ is: as $S_{enhanced} \to \infty$, $\text{Speedup}_{overall} \to \dfrac{1}{1 - F_{enhanced}}$.
- Used to argue for practical limits on the number of useful parallel processors, since any serial (non-parallelizable) fraction of a [[Workload and Benchmark|program]] bounds the achievable [[Multicore Microprocessor|parallel speedup]].
- Pitfall: expecting the improvement of one aspect of a computer to increase overall performance by an amount proportional to the size of that improvement — the improvement is bounded by how much of the execution time it actually affects.
- Fallacy: Amdahl's Law does not stop applying just because a computer is parallel; any serial fraction of a program still bounds the overall speedup achievable from adding processors, so gains in [[Multiprocessor|parallel]] execution rate are wasted unless matched by comparable gains in sequential execution rate.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=72&annotation=2RTPZVSU)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=581&annotation=CE3KTC6Z)
