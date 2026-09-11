---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Git Object[^1]
> A Git object is a piece of content stored in [[Git]]'s content-addressable object store; inserting any content into this store returns a unique key, the SHA-1 hash of that content and its header, which can later be used to retrieve it.

# Types
- [[Blob (Git)]]
- [[Tree (Git)]]
- [[Commit (Git)]]
- [[Annotated Tag|Tag Object]]

# Properties
- Git initially stores each object on disk as its own individual, compressed file, in what is called the "loose" object format; see [[Packfile]] for how these are later consolidated.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=421&annotation=YKZGQCV5)
