---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Register Spilling[^1]
> The process of putting less commonly used variables (or those needed later) into memory, because many programs have more variables than a computer has [[Register (Computer Architecture)|registers]].

# Properties
- The [[Compiler]] tries to keep the most frequently used variables in registers and spills the rest to [[Main Memory]] using [[Data Transfer Instruction|loads and stores]].
- During a procedure call, registers whose values must survive the call are commonly spilled onto the [[Call Stack]]; the associated memory region is part of the [[Procedure Frame]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=94&annotation=LS67FWMV)
