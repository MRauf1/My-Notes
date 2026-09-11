---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Register Use Convention (Procedure Call Convention)[^1]
> A software protocol governing how procedures use [[Register (Computer Architecture)|registers]] across a call, so that independently compiled or assembled procedures can cooperate correctly without needing to know each other's internals.

# Types
- Caller-saved register — saved (if it holds a value the caller still needs) by the calling routine before the call, since the callee is free to overwrite it.
- Callee-saved register — saved (if the callee uses it) by the called routine itself, since the caller expects its value to survive the call unchanged.

# Properties
- Splits the responsibility of preserving register values between caller and callee so that neither must save every register on every call, reducing unnecessary [[Register Spilling|spills]] to the [[Procedure Frame|procedure call frame]].
- Together with the [[Call Stack|stack]] and [[Program Counter]], defines the contract every compiled [[Procedure (Computer Science)|procedure]] must honor to interoperate, which is what makes recursive procedures — procedures that call themselves directly or through a chain of calls — work correctly: each active invocation gets its own frame and correctly preserved registers.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=619&annotation=NUYNAWBR)
