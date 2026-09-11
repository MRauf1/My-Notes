---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Three-Way Merge[^1]
> A three-way merge is the process [[Git]] uses to integrate two branches that have diverged: it combines the two latest snapshots of the branches together with the most recent commit common to both of them, producing a merged snapshot.

# Properties
- Since no simple pointer move can reconcile diverging histories, this process produces a [[Merge Commit]] rather than a [[Fast-Forward Merge]].
- The resulting snapshot is the same as the final snapshot [[Rebasing (Git)|rebasing]] the same two branches would produce; only the recorded history differs between the two approaches.
- While a conflict from this process is being resolved, the staging area temporarily holds three versions of each conflicted file at once — the common ancestor's version, the current branch's version, and the version from the branch being merged in — so that a tool can compare all three while resolving the conflict.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=101&annotation=5LZKEMA6)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=281&annotation=WMDGJFVZ)
