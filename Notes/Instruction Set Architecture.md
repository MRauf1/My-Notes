---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Instruction Set Architecture[^1]
> Also called architecture. An abstract interface between the hardware and the lowest-level software, encompassing all the information necessary to write a [[Machine Language]] program that will run correctly: instructions, registers, memory access, I/O, and so on.

# Properties
- The canonical example of [[Abstraction]] in computer design: it lets many implementations of varying cost and performance run identical software.
- An implementation is hardware that obeys the architecture's abstraction; maintaining a fixed instruction set architecture across implementations enables binary-compatible software, though it can preclude innovations that would require the interface itself to change.
- The [[Application Binary Interface]] extends the user portion of the instruction set with operating-system interfaces to define a standard for binary portability across computers.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=45&annotation=TKRK5IV4)
