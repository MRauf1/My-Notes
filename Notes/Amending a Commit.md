---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Amending a Commit[^1]
> Amending a commit in [[Git]] replaces the most recent commit entirely with a new commit built from the current staging area, rather than modifying the old commit in place.

# Properties
- If nothing has changed since the last commit, amending with the same staged content produces an identical snapshot, and only the commit message changes.
- The new commit pushes the old one out of the way entirely, as if it had never happened, so the superseded commit no longer appears in the repository's history.
- Because of this, only commits that are still local and have not been pushed elsewhere should be amended; amending and force-pushing an already-shared commit rewrites history that collaborators may have already built on.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=53&annotation=TLSSVV2C)
