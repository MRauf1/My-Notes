---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Packfile[^1]
> A packfile is a single binary file into which [[Git]] periodically consolidates many loose [[Git Object|objects]], storing similar objects as deltas against each other instead of each in full, to save space and improve efficiency.

# Properties
- Git packs accumulated loose objects together into a packfile when there are too many of them lying around, when housekeeping is run manually, or when pushing to a remote.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=436&annotation=62CHTYIH)
