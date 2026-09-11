---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Tracking Branch[^1]
> A tracking branch is a local [[Branch (Git)|branch]] that has a direct relationship to a [[Remote-Tracking Branch|remote-tracking branch]]; the remote branch it tracks is called its upstream branch.

# Properties
- Because a tracking branch already knows which upstream branch it corresponds to, synchronizing it automatically determines which remote server to contact and which remote branch to merge in, without that information needing to be specified again.
- Checking out a local branch from a remote-tracking branch automatically creates a tracking branch.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=99&annotation=87K5K5FT)
