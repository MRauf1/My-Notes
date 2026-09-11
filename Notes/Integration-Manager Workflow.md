---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Integration-Manager Workflow[^1]
> An integration-manager workflow is a [[Git Collaboration Workflow]] built around multiple public repositories, in which each contributor has write access only to their own public clone and read access to everyone else's, contributing changes by pushing to their own clone and asking the maintainer of a canonical repository to pull those changes in via a [[Pull Request (Git)|pull request]].

# Properties
- The maintainer of the canonical repository can add a contributor's repository as a remote, test the proposed changes locally, merge them in, and push the result back to the canonical repository.
- Because a contributor can keep pushing to their own repository at any time and the maintainer can pull from it whenever they choose, each party works at its own pace, rather than the contributor having to wait for their changes to be accepted before continuing.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=133&annotation=Y2ZRPN5I)
