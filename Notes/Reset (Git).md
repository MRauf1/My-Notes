---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Reset[^1]
> Reset is an operation that moves the branch [[HEAD (Git)|HEAD]] points to, to a different commit, and then optionally brings the staging area and the working directory in line with it too, stopping at whichever of these it is told to.

# Properties
- Moving just the branch pointer back to an earlier commit, without touching the staging area or working directory, effectively undoes a commit while leaving its changes staged and its files untouched.
- Going one step further to also update the staging area to match the new position of HEAD additionally unstages whatever was uniquely part of the abandoned commit(s), while still leaving the working directory's files as they were; this is reset's default extent when no further option is given.
- Going all the way and also overwriting the working directory to match is the only variant of reset capable of actually destroying data, since it forcibly discards any uncommitted changes in the working directory; every other extent of reset can be undone fairly easily.
- If a specific file path is given instead of moving the whole branch, HEAD is left untouched — a single pointer cannot meaningfully refer to only part of a commit — and only the staging area's, and optionally the working directory's, copy of that file is updated to match some commit's version; applied to the staging area, this is exactly what undoes staging that file.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=266&annotation=2ZMMPQXK)
