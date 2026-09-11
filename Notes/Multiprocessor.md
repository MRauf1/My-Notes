---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Multiprocessor[^1]
> A computer system with at least two processors, in contrast with a uniprocessor, which has one — increasingly rare today given the shift to [[Multicore Microprocessor|multicore]] designs.

# Types
- Task-level (process-level) parallelism — utilizing multiple processors by running independent programs simultaneously.
- Parallel processing program — a single program that runs across multiple processors at once.

# Properties
- Distinguishes the application-level perspective of concurrency (independent tasks that could run at the same time) from the hardware-level perspective of parallelism (processors that actually execute simultaneously).
- Classified along several axes: by memory organization (see [[Shared Memory Multiprocessor]] versus [[Message-Passing Multiprocessor]]), by instruction/data stream structure (see [[Flynn's Taxonomy]]), and by physical scale, from a single [[Multicore Microprocessor|multicore]] chip up to a [[Cluster (Computing)|cluster]] of separate computers acting as one large multiprocessor.
- Speedup on a multiprocessor is measured as either strong or weak scaling; see [[Scaling (Parallel Computing)]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=525&annotation=UH4FETHY)
