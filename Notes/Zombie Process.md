---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Zombie Process[^1]
> A terminated child process that its parent has not yet waited on. A zombie still occupies a slot in the kernel's process table, which records its PID, exit status, and how it was killed.

# Properties
- The only way to remove a zombie is for its parent to wait on it, using [[Wait (System Call)|wait or waitpid]].
- A parent that never waits on its children can eventually exhaust its ability to fork, since terminated children remain as zombies indefinitely.
- A child that is orphaned becomes a zombie only briefly, since the [[Init Process]] inherits it and automatically waits on all of its children.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=104&annotation=R4NSQIAY)
