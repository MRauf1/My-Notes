---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Arithmetic Intensity[^1]
> The ratio of floating-point operations performed by a program to the number of data bytes it accesses from main memory.

# Properties
- The central figure of merit in the roofline performance model: a kernel's arithmetic intensity determines whether its performance is bound by computational throughput (high intensity) or by [[Memory Hierarchy|memory]] bandwidth (low intensity), and thus which class of optimization can help.
- Computational bottlenecks (for a compute-bound, high-intensity kernel) are best addressed by improving the floating-point operation mix and by improving [[Instruction-Level Parallelism]] together with applying [[Subword Parallelism|SIMD]]; memory bottlenecks (for a memory-bound, low-intensity kernel) are better addressed by software [[Prefetching]] and by memory affinity — placing data close, in a [[Shared Memory Multiprocessor|NUMA]] system, to the processor that will use it most.
- Fallacy: peak performance tracks observed performance — a kernel's low arithmetic intensity, or unaddressed memory bottlenecks, routinely keeps achieved performance far below a machine's theoretical peak.
- Pitfall: failing to adapt software to take advantage of, or to optimize for, a multiprocessor's architecture squanders most of the performance the hardware could otherwise deliver.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=566&annotation=MLJIH323)
