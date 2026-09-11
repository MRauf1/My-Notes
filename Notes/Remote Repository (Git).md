---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Remote Repository[^1]
> A remote repository is a version of a [[Git]] project that is hosted somewhere other than the local clone referencing it, whether or not that location is actually elsewhere on a network.

# Properties
- A remote repository can reside on the very same machine as the repository referencing it; "remote" means only "elsewhere," not necessarily "over a network."
- Synchronizing history with a remote repository, wherever it is located, always involves the same standard pushing, pulling, and fetching operations, carried out over one of several [[Git Transfer Protocol|transfer protocols]].
- Since it exists only as a collaboration point rather than a place to edit files, a remote repository is generally kept as a [[Bare Repository]].
- The default name given to a remote when cloning a repository (conventionally "origin") carries no special meaning to Git; it is merely a configurable convention, just as the default initial [[Branch (Git)|branch]] name carries no special meaning.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=56&annotation=438ET2KZ)
