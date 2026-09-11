---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Procedure Frame (Activation Record)[^1]
> The segment of the [[Call Stack]] containing a procedure's saved registers and local variables, such as local arrays or structures that do not fit in registers.

# Properties
- Appears on the call stack for every active procedure invocation, whether or not the procedure uses an explicit frame pointer.
- A frame pointer register can offer a stable base register for referencing a procedure's local variables, since the stack pointer itself may change during the procedure's execution while the frame pointer stays fixed at the start of the frame.
- Also holds the values passed to the procedure as formal parameters — the variables standing in for a procedure's (or [[Macro|macro's]]) arguments, bound to the actual arguments once the call (or macro expansion) occurs — alongside any registers the [[Register Use Convention]] requires the procedure to save.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=126&annotation=LM76Z7K7)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=613&annotation=A3H4RXHJ)
