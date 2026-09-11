---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Dynamic Pipeline Scheduling[^1]
> Hardware support for choosing which instructions to execute next, reordering them at runtime, so as to avoid stalls that a strictly in-order pipeline would otherwise incur.

# Properties
- Enables a superscalar processor to perform out-of-order execution: an instruction blocked from executing (for example, waiting on an operand) does not stall the instructions that follow it, which may proceed if their own operands are ready.
- Organized around three major units: an instruction fetch-and-issue unit, multiple functional units (each often fronted by a reservation station, a buffer holding an operation's operands until it can execute), and a commit unit.
- The commit unit decides when it is safe to release a completed, out-of-order result to the programmer-visible registers or memory, holding results meanwhile in a reorder buffer; in-order commit writes results back in the same order instructions were originally fetched, even though they may have executed out of order, which helps produce a [[Exception (Computer Architecture)|precise exception]] model.
- Preferred over relying solely on compile-time scheduling because not all stalls are predictable at compile time, because [[Dynamic Branch Prediction|dynamic branch prediction]] makes the true instruction order unknowable until runtime, and because the best static schedule for a given code sequence depends on pipeline latency and issue width, which vary across implementations.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=362&annotation=FLZ4XJ9K)
