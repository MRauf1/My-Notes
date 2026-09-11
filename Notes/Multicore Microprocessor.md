---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Multicore Microprocessor[^1]
> A microprocessor containing multiple processors ("cores") per chip. Rather than continuing to decrease the response time of a single program on a single processor, desktop and server companies have shipped multicore microprocessors since 2006, where the benefit is often more on throughput than on response time.

# Properties
- Reflects performance via parallelism, one of the [[Great Ideas in Computer Architecture]]: parallel [[Central Processing Unit|processors]] are used to keep improving performance as [[Moore's Law|single-core clock rate growth]] has slowed.
- For programmers to get significant improvement in response time on multicore hardware, they must rewrite programs to be explicitly parallel, and continue improving that parallelism as the number of cores grows.
- Explicitly parallel programming is difficult for two main reasons: it is inherently performance programming, and it requires dividing an application so that each processor has roughly the same amount of work at the same time, without the overhead of scheduling, synchronization, and communication eroding the potential speedup.
- [[Amdahl's Law]] bounds the speedup achievable by adding more parallel processors, since any serial fraction of the program limits overall speedup.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=66&annotation=3AFGGJVA)
