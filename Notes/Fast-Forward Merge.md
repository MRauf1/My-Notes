---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Fast-Forward Merge[^1]
> A fast-forward merge occurs when the commit being merged in can already be reached by following the current branch's history; since there is no divergent work to reconcile, [[Git]] simply moves the current branch's pointer forward to that commit instead of creating a new commit.

# Properties
- Contrasts with a [[Three-Way Merge]], which is required when the two branches have diverged and a new commit must be created to combine them.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=79&annotation=N5QBTJ3Q)
