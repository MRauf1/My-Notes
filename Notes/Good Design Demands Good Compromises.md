---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Good Design Demands Good Compromises (Design Principle 3)[^1]
> No single, uniform representation is optimal for every conflicting design goal; a good instruction set architecture accepts a compromise, such as using multiple similar instruction formats rather than one.

# Properties
- One of the [[Instruction Set Design Principles]].
- Illustrated by MIPS keeping all instructions the same length while still requiring distinct [[Instruction Format|instruction formats]] (R-type, I-type, J-type) for different kinds of instructions, and by the trade-off between having more [[Register (Computer Architecture)|registers]] and keeping the instruction format compact.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=106&annotation=LU7DVHVF)
