---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Git File States[^1]
> A tracked file in [[Git]] is at any moment in one of three states — modified, staged, or committed — corresponding to the three main sections of a Git project: the working tree, the staging area, and the Git directory, respectively.

# Properties
- The working tree is a single checkout of one version of the project: files are pulled out of the compressed database in the Git directory and placed on disk to be used or modified; a file that has been changed since checkout but not yet staged is modified.
- The staging area is a file, generally kept inside the Git directory, that records what will go into the next commit; a modified file that has been marked to be included in the next commit is staged.
- The Git directory stores the project's metadata and object database; it is the most important part of a Git project and is what gets copied when a repository is cloned. Once a version of a file is recorded there, it is committed.
- More broadly, every file in the working tree is either tracked or untracked. Tracked files are files that were part of the last snapshot or have since been staged, so they can be unmodified, modified, or staged; untracked files are everything else — files present in the working tree that were neither in the last snapshot nor placed in the staging area.[^2]
- Staging a file records its exact content at the moment it is staged; if the file is modified again afterward, the newer changes are not reflected in the staging area until the file is staged again.[^3]

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=23&annotation=9S2RYEDB)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=34&annotation=78Z9M59Y)
[^3]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=37&annotation=HMU5EED8)
