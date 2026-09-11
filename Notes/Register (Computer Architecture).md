---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Register[^1]
> A limited number of special storage locations built directly into hardware, used to hold the operands of arithmetic and most other instructions. Registers are primitives of hardware design that remain visible to the programmer once the computer is complete.

# Properties
- Unlike variables in a [[High-Level Programming Language]], the number of registers is small and fixed — typically 32 general-purpose registers on current architectures, like MIPS — a consequence of [[Smaller Is Faster]].
- Faster to access, higher throughput, and more energy-efficient than [[Main Memory]], since there are fewer of them and they sit closer to the [[Central Processing Unit|processor]]'s datapath.
- Data structures such as arrays and structures do not fit in registers and are instead kept in memory; [[Register Spilling]] moves less frequently used variables from registers into memory.
- A [[Word (Computer Architecture)|word]] corresponds to the size of a register in the MIPS architecture.
- The stack pointer, frame pointer, and program counter are all specific registers with reserved architectural roles — see [[Call Stack]], [[Procedure Frame]], and [[Program Counter]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=89&annotation=IEZTS7UL)
