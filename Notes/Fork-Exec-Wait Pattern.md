---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Fork-Exec-Wait Pattern[^1]
> A common pattern in which a process calls [[Fork and Exec|fork()]] to create a child, the child calls [[Fork and Exec|exec()]] to start a new program, and the parent calls [[Wait (System Call)|wait() or waitpid()]] to wait for that child to finish.

# Properties
- Lets the parent act as a monitor program: rather than replacing itself with the child's program, it remains free to do other work, modify system state, or read the child's output while the child runs.[^2]
- Underlies the [[System (Function)|system() function]], which performs the same sequence internally but hides its mechanics.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=108&annotation=W57YSKTM)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=109&annotation=QCD8QT69)
