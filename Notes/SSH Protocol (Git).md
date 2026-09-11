---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] SSH Protocol[^1]
> The SSH protocol is a [[Git Transfer Protocol]] that authenticates and encrypts all transferred data using SSH, and is commonly used to access self-hosted repositories.

# Properties
- Because it is both authenticated and encrypted, and SSH access is already widely available and simple to enable wherever it exists, this protocol is an efficient and secure default for private, self-hosted repositories.
- It does not support anonymous access: anyone accessing a repository over SSH, even read-only, needs SSH access to the host, making it a poor fit on its own for projects meant to be openly cloneable.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=114&annotation=NKAKUB6Y)
