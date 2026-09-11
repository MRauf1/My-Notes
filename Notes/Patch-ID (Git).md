---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Patch-ID[^1]
> A patch-ID is a checksum [[Git]] computes from just the patch, i.e. the content change, that a commit introduces, in addition to that commit's ordinary SHA-1 checksum over the whole commit.

# Properties
- Because it depends only on the change a commit introduces rather than on its full identity (parent, timestamp, etc.), two commits with different SHA-1 checksums but the same patch-ID can be recognized as introducing the same underlying change, such as before and after that commit was replayed via [[Rebasing (Git)|rebasing]].

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=108&annotation=F492AUMN)
