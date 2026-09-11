---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Program Counter (PC)[^1]
> The register containing the address of the instruction in the program currently being executed.

# Properties
- A direct consequence of the [[Stored-Program Concept]]: since instructions reside in memory like data, some register must track which instruction is executing.
- Used as the base for [[Addressing Mode|PC-relative addressing]] in [[Conditional Branch|conditional branches]].
- A jump-and-link [[Instruction]] saves the address of the following instruction (PC + 4) into the [[Register (Computer Architecture)|return-address register]] to set up a procedure's return; see [[Procedure (Computer Science)]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=121&annotation=QEVHYALR)
