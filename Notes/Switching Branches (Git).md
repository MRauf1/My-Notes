---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Switching Branches[^1]
> Switching [[Branch (Git)|branches]] in Git resets the working directory to look like it did at the last commit on the branch being switched to, automatically adding, removing, and modifying files as needed.

# Properties
- If the working directory or staging area has uncommitted changes that would conflict with the branch being switched to, Git refuses to perform the switch, rather than silently discarding or overwriting that work; keeping a clean working state avoids this.
- Switching branches moves [[HEAD (Git)|HEAD]] itself to point at the new branch, whereas [[Reset (Git)|resetting]] instead moves the branch that a stationary HEAD points to.
- Because switching branches checks that it will not overwrite files with uncommitted changes, and effectively performs a trivial merge in the working directory so that unmodified files are simply updated, it is safe with respect to uncommitted work in a way that forcibly overwriting the working directory during a reset is not.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=74&annotation=GTJDRDGL)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=276&annotation=4CFUPEMR)
