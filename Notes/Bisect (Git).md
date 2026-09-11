---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Bisect[^1]
> Bisect is a technique for finding which commit introduced a regression by performing a binary search through the commit history between a known-good and a known-bad commit.

# Properties
- This narrows the search exponentially, making it practical to identify the offending commit even when there are dozens or hundreds of intervening commits, without testing each one individually.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=302&annotation=4Y3UBGBC)
