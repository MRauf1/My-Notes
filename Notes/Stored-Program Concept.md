---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Stored-Program Concept[^1]
> The idea that instructions and data of many types can be stored in memory as numbers, leading to the stored-program computer. It rests on two key principles: instructions are represented as numbers indistinguishable from data, and programs reside in alterable memory just like data.

# Properties
- Because instructions are numbers, [[Main Memory]] can simultaneously hold the source code of a program, its compiled [[Machine Language]], the data it operates on, and even the [[Compiler]] that produced it.
- A direct consequence is that programs can be shipped as files of binary numbers; "binary compatibility" with an existing [[Instruction Set Architecture]] lets a computer run ready-made software, which is one reason the industry aligns around a small number of instruction set architectures.
- Implicitly requires a [[Program Counter]]: a register holding the address of the instruction currently being executed.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=86&annotation=FBDZ5FAR)
