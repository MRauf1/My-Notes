---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Graphics Processing Unit (GPU)[^1]
> An accelerator that supplements a CPU as a coprocessor, built as an MIMD machine composed of many multithreaded SIMD processors (see [[Flynn's Taxonomy]]), specialized for data-level-parallel workloads rather than general-purpose computation.

# Properties
- Since a GPU only needs to accelerate a CPU rather than replace it, it need not implement every task a CPU can perform, and it typically works on problem sizes of hundreds of megabytes to a few gigabytes rather than the hundreds of gigabytes to terabytes a CPU-based server might handle.
- Relies on [[Hardware Multithreading|hardware multithreading]], not deep [[Multilevel Cache|multilevel caching]], to hide memory latency: while one memory request is in flight, hundreds or thousands of other independent threads keep execution units busy, which is why GPU memory is designed for bandwidth rather than low latency — though the latest GPUs (like vector processors) have begun adding caches too.
- The unit of scheduling is a thread of SIMD instructions (a "SIMD thread"): an ordinary thread that contains exclusively SIMD instructions; GPU hardware schedules at two levels, assigning SIMD threads to multithreaded SIMD processors and then scheduling individual SIMD instructions within each.
- On-chip Local Memory is private to a single multithreaded SIMD processor and shared only among its own SIMD lanes; off-chip GPU Memory (DRAM) is shared across the whole GPU and all thread blocks.
- Works well only on data-level-parallel problems, mirroring the strengths and weaknesses of [[Vector Architecture|vector architectures]]; for general-purpose (GPGPU) computation, overall performance must also account for the time spent transferring data between separate CPU and GPU memories, though "fused" designs sharing a single memory between CPU and GPU have emerged to reduce this cost.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=547&annotation=X6ZVDPAT)
