---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Conditional Branch[^1]
> An [[Instruction]] that requires the comparison of two values and allows for a subsequent transfer of control to a new address in the program, based on the outcome of that comparison.

# Properties
- Contrasted with an unconditional branch (a jump), which the processor always follows regardless of any comparison.
- Typically uses [[Addressing Mode|PC-relative addressing]], since its target tends to be a nearby instruction within the same loop or if statement.
- Together with unconditional jumps, forms the boundaries of a [[Basic Block]].
- Comparisons for equality (as in MIPS `beq`/`bne`) can be combined with a "set on less than" instruction and the constant zero to synthesize every relative condition: equal, not equal, less than, less than or equal, greater than, greater than or equal.
- A multi-way branch, such as a switch statement, can be compiled either as a chain of conditional branches or, more efficiently, using a [[Jump Address Table]].
- The branch target address is the address that becomes the new [[Program Counter]] if the branch is taken; in MIPS it is the sum of the instruction's offset field and the address of the instruction following the branch.
- A branch is taken when its condition is satisfied and the PC becomes the branch target (every unconditional jump is a taken branch); it is not taken (untaken) when the condition is false and the PC becomes the address of the sequentially following instruction.
- Resolving which outcome occurred is a source of a [[Control Hazard]] in a pipelined processor.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=114&annotation=Q6EXGRDY)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=277&annotation=CDUWAQMG)
