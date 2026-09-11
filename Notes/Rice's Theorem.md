---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Rice's Theorem[^1]
> No non-trivial semantic property of a program's behavior (for example, which files it will try to open) can be decided without actually running the program.

# Properties
- Used to justify why operating systems favor [[Deadlock Detection]] over static deadlock prevention: since a program's actual resource requests cannot be determined in advance, the system cannot know that a deadlock will occur until it happens.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=199&annotation=Y522WCUD)
