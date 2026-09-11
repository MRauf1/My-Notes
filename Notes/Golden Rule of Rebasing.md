---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Golden Rule of Rebasing[^1]
> Never rebase commits that have already been made public and that other people may have based their own work on; only rebase commits that exist solely in your own local repository, or that have been pushed but that no one else has yet built upon.

# Properties
- [[Rebasing (Git)|Rebasing]] abandons the original commits and creates new, similar-but-different commits in their place; if collaborators already pulled the original commits and built work on top of them, republishing the rewritten history forces them to reconcile two diverging histories of the same work, which becomes messy.
- Rebasing local changes before pushing them for the first time is safe, and lets a contributor clean up their own work; the rule is only violated by rewriting and re-pushing commits that others have already pulled and built upon.
- If a branch that others may have already built upon really does need to be cleaned up by rebasing, it is safer to push the rebased result as a new branch and open a new request to integrate it, closing the original, than to force-push the rewritten history over the original branch.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=106&annotation=DXC4XVFS)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=188&annotation=BKE6K7A9)
