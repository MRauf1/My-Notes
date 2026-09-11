---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Instruction Format[^1]
> A form of representation of an [[Instruction]] composed of fields of binary numbers. Each field's value, and the leading opcode field in particular, tells the hardware how to interpret the rest of the instruction.

# Types
- R-type — used for register-to-register instructions, with fields for an opcode, up to three registers, a shift amount, and a function code.
- I-type — used for instructions with an immediate constant or memory offset, with fields for an opcode, two registers, and a 16-bit constant.
- J-type — used for jump instructions, with fields for an opcode and a large address field.

# Properties
- The opcode is the field that denotes the operation and format of an instruction; it distinguishes which format (R-type, I-type, or J-type) the remaining fields should be interpreted as.
- Illustrates [[Good Design Demands Good Compromises]]: MIPS keeps all instructions the same fixed length while still needing multiple, similar formats for different kinds of instructions.
- The trade-off between having many [[Register (Computer Architecture)|registers]] and keeping instructions compact is a direct consequence of a fixed instruction length, since each additional register requires another bit in every register field.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=104&annotation=QXEET74N)
