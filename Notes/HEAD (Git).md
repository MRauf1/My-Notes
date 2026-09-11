---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] HEAD[^1]
> HEAD is a special pointer that [[Git]] keeps to record which [[Branch (Git)|branch]] is currently checked out.

# Properties
- HEAD ordinarily points at a branch, which in turn points at a commit; moving HEAD directly to a commit instead of a branch produces a [[Detached HEAD]] state.
- Because HEAD points at the current branch's last commit, it will be the parent of the next commit created; HEAD can loosely be thought of as the snapshot of that last commit.
- HEAD is itself ordinarily a [[Symbolic Reference (Git)|symbolic reference]] — a reference that points to another reference (the current branch) rather than directly to a commit.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=71&annotation=4MLBI8BZ)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=257&annotation=T5G42RPA)
[^3]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=432&annotation=D8NEK76E)
