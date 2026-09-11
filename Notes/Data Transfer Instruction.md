---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Data Transfer Instruction[^1]
> A command that moves data between [[Main Memory]] and [[Register (Computer Architecture)|registers]]. Since arithmetic operations act only on registers in a load/store architecture like MIPS, an instruction set must include such instructions to move data in and out of registers.

# Types
- Load — copies data from memory to a register (e.g. MIPS `lw`, load word).
- Store — copies data from a register to memory (e.g. MIPS `sw`, store word).

# Properties
- Supplies a [[Memory Address]] as the sum of a constant, called the offset, and the contents of a base register.
- Subject to any [[Alignment Restriction]] the architecture imposes on the addresses it may access.
- The [[Compiler]] allocates data structures such as arrays and structures to memory locations and places the correct starting address into these instructions.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=91&annotation=P3RPV2D8)
