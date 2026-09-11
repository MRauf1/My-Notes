---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Reflog[^1]
> The reflog is a log [[Git]] keeps in the background of where [[HEAD (Git)|HEAD]] and each branch reference have pointed over the last several months, updated every time a branch tip changes for any reason.

# Properties
- Reflog entries can be used to refer back to commits that are no longer reachable from any current branch or tag.
- The reflog is strictly local: it records only activity that happened in one's own repository, is not transferred by cloning or fetching, and starts out empty immediately after a fresh clone.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=226&annotation=MJUS5NLK)
