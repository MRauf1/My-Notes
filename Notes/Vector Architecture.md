---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Vector Architecture[^1]
> A SIMD architecture (see [[Flynn's Taxonomy]]) that collects data elements from memory into a large set of vector registers, operates on them sequentially through pipelined execution units, and writes the results back to memory, rather than issuing one scalar instruction per element.

# Properties
- A vector register holds many elements — for example, 32 vector registers of 64 64-bit elements each — letting a single vector instruction replace what would otherwise be dozens or hundreds of scalar instructions (in one comparison, 6 vector instructions versus almost 600 scalar MIPS instructions for the same loop), which also reduces energy spent on instruction fetch and decode.
- Reduces [[Pipeline Hazard|pipeline hazard]] frequency relative to the equivalent scalar (conventional instruction set) code: a vector instruction stalls only once, for its first element, after which the rest of the vector flows smoothly through the pipeline, instead of stalling on every dependent scalar instruction.
- Supports both strided access, loading every $n$th element from memory, and indexed access (gather-scatter), where a vector register supplies the addresses to load from or store to — gathering scattered elements from memory into a contiguous vector register, or scattering a contiguous vector register's elements out across memory — data movement patterns not generally available to multimedia SIMD extensions.
- A vector lane consists of one or more vector functional units plus a slice of the vector register file; multiple lanes execute vector operations in parallel, but pay off only for long vectors, since short vectors run out of independent work quickly, requiring the [[Instruction-Level Parallelism]] techniques used for scalar code to keep enough vector instructions flowing.
- Compared to multimedia extensions such as x86 SIMD instructions, vector architectures are a more efficient way to execute data-parallel programs, are a better match for compiler technology, and are easier to extend over time.
- Fallacy: good vector performance can be had without also providing adequate memory bandwidth, since vector code's throughput is fundamentally limited by how fast operands can move between memory and the vector registers.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=533&annotation=PUHSCSAH)
