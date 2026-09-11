---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Control Unit[^1]
> The hardware unit that takes an [[Instruction]] as input and determines how to set the control lines of the datapath's functional units and [[Multiplexor|multiplexors]] for that instruction.

# Properties
- Because the [[Instruction Set Design Principles|regularity and simplicity]] of an [[Instruction Set|instruction set]] such as MIPS puts a small, fixed opcode field (see [[Instruction Format]]) in the same position across formats, the control unit can decode which control lines to set with a simple lookup, often expressed as a [[Truth Table]].
- One [[Multiplexor]] — selecting whether the next [[Program Counter]] value is PC + 4 or a [[Conditional Branch|branch]] target — is instead controlled directly by the ALU's zero output rather than by the control unit, since that decision depends on a runtime comparison result rather than solely on the instruction's opcode.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=270&annotation=9HPLIXT7)
