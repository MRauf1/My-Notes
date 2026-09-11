---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Tree[^1]
> A tree is the [[Git Object]] type corresponding to a Unix directory entry: it contains one or more entries, each pairing the SHA-1 hash of a [[Blob (Git)|blob]] or of another tree (a subtree) with that entry's mode, type, and filename.

# Properties
- Pairing blobs with trees this way is what lets a single snapshot record both a file's content and its filename and directory placement, since a blob alone carries no name.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=423&annotation=XRTR3DCK)
