---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Basic Block[^1]
> A sequence of instructions without branches, except possibly at the end, and without branch targets or branch labels, except possibly at the beginning.

# Properties
- Delimited by [[Conditional Branch|conditional branches]] and unconditional jumps: control can only enter at the start of a basic block and leave at its end.
- A fundamental unit of analysis in [[Compiler]] optimization, since every instruction inside a basic block is guaranteed to execute exactly once if the block executes at all.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=116&annotation=SABRXIVG)
