---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Strong and Weak Scaling[^1]
> Strong scaling is the speedup achieved on a [[Multiprocessor]] without increasing the size of the problem being solved. Weak scaling is the speedup achieved while increasing the problem size proportionally to the increase in the number of processors.

# Properties
- Strong scaling is bounded by [[Amdahl's Law|Amdahl's Law]], since a fixed problem's non-parallelizable fraction stays fixed in absolute time as processors are added; weak scaling can sidestep some of that limit by growing the parallel portion of the work alongside the processor count.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=530&annotation=UCEG4T5S)
