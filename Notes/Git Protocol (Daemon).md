---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Git Protocol[^1]
> The Git protocol is a [[Git Transfer Protocol]] served by a dedicated daemon bundled with Git, providing the same kind of data-transfer mechanism as the [[SSH Protocol (Git)|SSH protocol]] but with no authentication or encryption.

# Properties
- Because there is no authentication, a repository served this way is either openly cloneable by anyone or not served at all; push access can be enabled, but is rarely used, since anyone who finds the project's URL could then push to it.
- With no encryption or authentication overhead, it is typically the fastest of Git's transfer protocols, which makes it attractive for serving high-traffic or very large public projects that don't need authenticated read access.
- Because it provides no transport encryption, cloning over this protocol can expose a client to an arbitrary code execution vulnerability, so it should be avoided unless this risk is well understood.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=115&annotation=9BIZUZ4V)
