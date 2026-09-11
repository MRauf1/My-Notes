---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Git Stash[^1]
> A stash takes the dirty state of the working directory — modified tracked files and any staged changes — and saves it on a stack of unfinished changes that can be reapplied at any later time, even on a different branch, without having to make a commit of half-finished work.

# Properties
- Reapplying a stash can produce a merge conflict if the file it touches has since been modified again; the conflict must then be resolved like any other.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=236&annotation=H47375CG)
