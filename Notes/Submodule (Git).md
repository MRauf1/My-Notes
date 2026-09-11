---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Submodule[^1]
> A submodule is a [[Git]] repository kept as a subdirectory of another project's repository, letting the outer, "super" project reference a specific commit of the inner repository without merging their commit histories together.

# Properties
- Although a submodule's directory is physically present in the superproject's working directory, the superproject does not track the individual files inside it; it only records which single commit of the submodule's own repository is currently checked out there.
- Because the superproject stores only a reference to that commit rather than the submodule's actual content, the submodule's repository content must be separately fetched and checked out before its files appear in that directory.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=304&annotation=9Z5GXKKQ)
