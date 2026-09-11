---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Procedure[^1]
> A stored subroutine that performs a specific task based on the parameters with which it is provided.

# Properties
- The caller is the program that instigates a procedure and provides its parameter values; the callee is the procedure that executes based on those parameters and returns control to the caller.
- Executing a procedure call follows a fixed sequence: place parameters where the procedure can access them, transfer control to the procedure (a jump-and-link [[Instruction]] that also saves the [[Program Counter|return address]]), acquire the storage needed by the procedure, perform the task, place results where the caller can access them, and return control to the caller.
- A leaf procedure is one that does not call any other procedure.
- Registers needed by the caller across the call, or by the callee beyond its allotted argument and temporary registers, must be spilled and restored using the [[Call Stack]]; see [[Register Spilling]] and [[Procedure Frame]].
- Procedure inlining — copying a called procedure's code directly into its caller instead of using a call and return — can avoid call overhead but increases code size, which can hurt performance if it increases the cache miss rate.
- Some recursive procedures can be rewritten iteratively, improving performance by removing the overhead of repeated procedure calls.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=119&annotation=9BQW779J)
