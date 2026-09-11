---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Call Stack[^1]
> The region of memory used to spill registers and store local data across [[Procedure (Computer Science)|procedure]] calls, organized as a [[Stack]]: a last-in-first-out data structure. A stack pointer register denotes the most recently allocated address in the stack, showing where the next procedure should spill registers or where old register values can be found; in MIPS it is register `$sp`.

# Properties
- By historical convention, a call stack grows from higher addresses toward lower addresses: pushing subtracts from the stack pointer, and popping adds to it.
- Holds each active procedure's [[Procedure Frame]], containing its saved registers and local variables.
- Has a predefined size limit; exceeding it (for example, through unbounded recursion) causes a stack overflow.
- One of the segments of a running program's address space; see [[Process Memory Layout]].
- Deallocating a procedure's automatic variables on return is fast, since it only requires restoring the stack pointer to the previous value saved on the stack, rather than explicitly freeing anything.[^2]

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=121&annotation=ML4E6AGR)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=132&annotation=5YB49G8N)
