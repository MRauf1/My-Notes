---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] system() Function[^1]
> A library call that forks, spawns a shell to execute the given command string, and blocks the calling (parent) process until that command finishes.

# Properties
- More overhead than calling [[Fork and Exec|exec()]] directly, since it also creates an intervening shell; that shell resolves the command using the [[PATH (Environment Variable)|PATH]] environment variable.
- Hides the mechanics of the [[Fork-Exec-Wait Pattern|fork-exec-wait pattern]], which is preferable to learn and use directly beyond simple run-this-command needs.
- A significant security risk, since it grants access to a full shell environment.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=108&annotation=JH344GAP)
