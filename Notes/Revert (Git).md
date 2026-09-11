---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Revert[^1]
> A revert is an operation that creates a new commit undoing the changes introduced by an earlier commit, by applying the inverse of that commit's patch, rather than removing or altering the original commit.

# Properties
- Unlike moving a branch pointer backward with [[Reset (Git)|reset]], which rewrites history and is unsafe on a shared branch, reverting adds new history on top of the old, making it the safe way to undo work that has already been published.
- Reverting a [[Merge Commit]] only undoes the code changes it introduced; the reverted commits remain part of the branch's ancestry, so naively merging the same source branch again afterward brings in only what has changed since the revert, not the branch's full original content, until the revert itself is undone to restore that ancestry path.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=289&annotation=Z86X5UQF)
