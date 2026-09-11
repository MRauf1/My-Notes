---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Flynn's Taxonomy[^1]
> A classification of computer hardware by its number of independent instruction streams and data streams.

# Types
- SISD (Single Instruction stream, Single Data stream) — a uniprocessor.
- SIMD (Single Instruction stream, Multiple Data streams) — the same instruction is applied simultaneously to many data streams, as in a [[Vector Architecture|vector processor]] or [[Subword Parallelism|subword-parallel]] hardware.
- MIMD (Multiple Instruction streams, Multiple Data streams) — a [[Multiprocessor]], where independent processors can execute different instructions on different data at once.
- SPMD (Single Program, Multiple Data streams) — the conventional MIMD programming model, in which a single program's copy runs across all processors, each following its own control flow through that same program.

# Properties
- SIMD achieves data-level parallelism — parallelism from performing the same operation on independent data — and works best on array-oriented, identically structured computation such as `for` loops; it is weakest on case/switch-style control flow, where each execution unit would need to follow a different path depending on its own data.
- A [[Graphics Processing Unit|GPU]] combines both levels: it is an MIMD machine composed of many multithreaded SIMD processors.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=532&annotation=TYTR2VPG)
