---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Detached HEAD[^1]
> Detached HEAD is a state of a [[Git]] repository in which [[HEAD (Git)|HEAD]] points directly at a specific commit rather than at a [[Branch (Git)|branch]].

# Properties
- A commit created while HEAD is detached does not belong to any branch and, once HEAD moves elsewhere, becomes unreachable except by its exact commit hash.
- To keep new work reachable by name, such as when fixing a bug at an older point in history, a branch should be created from that point rather than committing directly while HEAD is detached.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=66&annotation=68TQF2QM)
