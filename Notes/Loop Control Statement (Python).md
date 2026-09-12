---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Loop Control Statement (Python)[^1]
> The statements that alter a loop's normal flow from within its body: `break` jumps out of the closest enclosing loop entirely, `continue` jumps back to the top of the closest enclosing loop, and `pass` does nothing at all, serving as an empty statement placeholder.

# Properties
- `break` bypasses any [[Loop Else Clause (Python)|loop else clause]], since that clause runs only when the loop is not exited via `break`.
- `pass` is commonly used to stub out the body of a function or block that will be filled in later, since Python requires every compound statement to have a non-empty body[^2].
- The `...` ellipsis literal can serve the same "to be filled in later" role as `pass`, since any expression — including `...` — is a valid statement on its own[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=494&annotation=UEGZVTC4)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=495&annotation=DAFYQEIQ)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=496&annotation=XAWTJ329)
