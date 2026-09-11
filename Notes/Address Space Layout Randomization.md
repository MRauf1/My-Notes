---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Address Space Layout Randomization[^1]
> A security feature that randomizes where a process's segments (such as the text segment of its [[Process Memory Layout]]) are placed within its address space, rather than always starting from a fixed address.

# Properties
- Can be disabled to give a process a constant load address, for instance by compiling it with a DEBUG flag, trading away the security benefit for reproducibility while debugging.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=92&annotation=NGGKPNDP)
