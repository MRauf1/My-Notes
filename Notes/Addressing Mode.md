---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Addressing Mode[^1]
> One of several addressing regimes, delimited by their varied use of operands and/or addresses, used by an instruction to identify its operands.

# Types
- PC-relative addressing — the address is the sum of the [[Program Counter]] and a constant in the instruction; used for conditional branches, whose destinations tend to be nearby, since branches are found within loops and if statements.
- Base (or displacement) addressing — the address is the sum of a constant offset and the contents of a base [[Register (Computer Architecture)|register]]; used by [[Data Transfer Instruction|data transfer instructions]].
- Immediate addressing — the operand is a constant embedded directly within the instruction.
- Register addressing — the operand is the value held in a register.
- Pseudo-direct addressing — a large address field (as in a J-type jump) is combined with high-order bits of the program counter to form a full address, since jump-and-link instructions invoke procedures with no reason to be near the call site.

# Properties
- MIPS stretches the reach of PC-relative and pseudo-direct addressing by interpreting their address fields as word addresses rather than byte addresses, since every MIPS instruction is 4 bytes long.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=139&annotation=8E38KDVB)
