---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Pseudoinstruction[^1]
> A common variation of an [[Assembly Language]] instruction, often treated by programmers as if it were an instruction in its own right, even though the underlying hardware does not implement it directly.

# Properties
- Expanded by the [[Assembler]] into one or more real machine instructions; for example, the assembler can synthesize a 32-bit constant from a 16-bit immediate field by combining `lui` with a logical-OR-immediate instruction, or replace an out-of-range [[Conditional Branch|conditional branch]] with an inverted branch around an unconditional jump.
- Lets an [[Instruction Set]] stay simple in hardware while still offering a convenient, more expressive assembly language to the programmer.
- Collectively, an assembler's pseudoinstructions present the programmer with a kind of virtual machine: a virtual computer that appears to have a richer instruction set (and simpler behavior, such as non-delayed branches and loads) than the underlying hardware actually implements.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=147&annotation=HHAVB6WJ)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=638&annotation=WMXKUDVS)
