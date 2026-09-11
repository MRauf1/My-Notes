---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Loop Unrolling[^1]
> A technique for extracting more performance from loops that access arrays, in which the compiler makes multiple copies of the loop body and interleaves instructions from different iterations, reducing per-iteration loop-control overhead and exposing more independent work.

# Properties
- Supplies [[Multiple Issue|multiple-issue]] hardware with more independent instructions to schedule together, helping fill issue slots that data dependences within a single iteration would otherwise leave empty.
- Combined with [[Register Renaming]] to resolve the antidependences that arise when several unrolled iterations reuse the same registers.
- Illustrated a more than twofold performance improvement (6.4 to 14.6 GFLOPS) in an optimized matrix-multiply routine, on top of the gains from subword parallelism; see [[Subword Parallelism]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=361&annotation=62Z9I6YP)
