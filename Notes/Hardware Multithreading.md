---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Hardware Multithreading[^1]
> A technique that increases the utilization of a processor by switching to another [[Thread]] whenever the current one stalls, rather than leaving the processor idle.

# Types
- Fine-grained multithreading — switches between threads after every instruction.
- Coarse-grained multithreading — switches between threads only after a significant stall event, such as a last-level cache miss.
- Simultaneous multithreading (SMT) — lowers the cost of multithreading by reusing the resources already present in a [[Multiple Issue|multiple-issue]], dynamically scheduled microarchitecture (see [[Dynamic Pipeline Scheduling]]), issuing instructions from several threads within the same clock cycle rather than switching wholesale between them; Intel's [[Hyperthreading]] is an implementation of this technique.

# Properties
- The dominant technique [[Graphics Processing Unit|GPUs]] use to hide long memory latency: while one group of threads waits on a memory request, hundreds or thousands of other independent threads keep the processor's execution units busy, in place of the deep [[Multilevel Cache|multilevel caches]] CPUs rely on for the same purpose.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=539&annotation=I8B6NJ7T)
