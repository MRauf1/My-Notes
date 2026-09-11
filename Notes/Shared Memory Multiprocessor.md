---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Shared Memory Multiprocessor (SMP)[^1]
> A [[Multiprocessor]] that offers every processor a single, shared physical address space — arguably better named a shared-address multiprocessor, since the memory itself may still be physically distributed.

# Types
- Uniform memory access (UMA) — latency to any word of main memory is about the same regardless of which processor requests it.
- Nonuniform memory access (NUMA) — a single-address-space multiprocessor in which access latency depends on which processor requests which word, since some memory is physically nearer to some processors than others; harder to program than UMA but able to scale to larger sizes and to give lower latency for nearby memory.

# Properties
- The typical organization of a [[Multicore Microprocessor|multicore]] chip: cores are connected by a fast, low-latency, high-bandwidth on-chip (or multichip) memory interconnect, which is what gives shared-memory systems better communication performance than a [[Message-Passing Multiprocessor|message-passing]] alternative like a [[Cluster (Computing)|cluster]].
- Requires synchronization — coordinating the behavior of processes that may run on different processors — commonly built from a lock, a device that restricts access to a piece of data to one processor at a time; see [[Mutual Exclusion]] and [[Atomic Operation]] for the underlying hardware primitives.
- Programmed with shared-memory APIs such as OpenMP (compiler directives, a library, and runtime support for C, C++, and Fortran) or the lower-level Pthreads library; OpenMP is easy to write simple parallel code in but offers limited debugging support compared to more sophisticated parallel programming systems.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=526&annotation=EQRINZNF)
