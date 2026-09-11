---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Subword Parallelism (SIMD)[^1]
> A form of parallelism obtained by partitioning the carry chains within a single wide adder (e.g. 128 bits) so it can perform simultaneous operations on several shorter operands packed into one word — for example, sixteen 8-bit, eight 16-bit, four 32-bit, or two 64-bit operands at once — at a small hardware cost. Also called vector or SIMD (single instruction, multiple data), since one instruction operates on multiple data elements simultaneously.

# Properties
- A special case of the more general concept of data-level parallelism, the same principle exploited at larger grain by [[Vector Architecture|vector architectures]] and [[Graphics Processing Unit|GPUs]]; see [[Flynn's Taxonomy]].
- Applies to both integer and floating-point data; one of the [[Great Ideas in Computer Architecture|great ideas]] of performance via parallelism realized within a single word rather than across separate processors, contrasted with the coarser-grained parallelism of a [[Multicore Microprocessor]].
- Illustrated by roughly a fourfold speedup of double-precision matrix multiplication when using subword-parallel instructions that perform four floating-point operations at a time.
- Fallacy: parallel execution strategies that work for integer data do not automatically work for floating-point data, since [[Floating-Point Number System|floating-point]] addition is not associative — reordering operations across parallel lanes can change the rounded result, a central concern of numerical analysis.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=245&annotation=UGVHWUVI)
