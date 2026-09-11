---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Rerere[^1]
> Rerere ("reuse recorded resolution") is a [[Git]] feature that records the before-and-after state of successfully resolved merge conflicts so that, if an identical conflict recurs, Git can automatically reapply the previously recorded resolution instead of requiring it to be resolved manually again.

# Properties
- It is particularly useful when doing extensive merging and rebasing, or maintaining a long-lived [[Topic Branch|topic branch]], since the same conflicts often recur repeatedly across those operations.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=168&annotation=3HDGVDBE)
