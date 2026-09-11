---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Distributed Version Control System[^1]
> A distributed version control system (DVCS) is a [[Version Control System]] in which clients do not merely check out the latest snapshot of a project's files, but instead fully mirror the repository, including its complete history.

# Properties
- Because every clone is effectively a full backup of all the project's data, if a central server that clients were collaborating through fails, any client's repository can be copied back up to restore it.
- Because every clone is a full peer rather than a mere checkout, any developer can act as both a consumer of others' work and a hub maintaining their own public repository that others can contribute to and build upon, unlike in a [[Centralized Version Control System|centralized system]], where every developer is simply a consuming node of one central hub. This flexibility is the basis for the various [[Git Collaboration Workflow|collaboration workflows]] built on top of Git.
- [[Git]] is a widely used implementation of this model.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=18&annotation=YYKXCWEK)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=132&annotation=HQGHWLFB)
