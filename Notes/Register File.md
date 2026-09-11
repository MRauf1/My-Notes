---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Register File[^1]
> A state element consisting of a set of [[Register (Computer Architecture)|registers]] that can be read and written by supplying a register number to be accessed.

# Properties
- A [[Datapath Element|state datapath element]], distinct from combinational elements such as the [[Arithmetic Logic Unit|ALU]].
- The [[Instruction Set Design Principles|regularity]] of an instruction format, which places source register fields in the same position across instruction types, lets the register file begin being read in parallel with decoding which type of instruction was fetched.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=275&annotation=FBSHSNZG)
