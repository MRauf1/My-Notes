---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Refspec[^1]
> A refspec is a mapping, configured for a remote, between [[Reference (Git)|reference]] names on that remote and reference names under the local Git directory, which determines which of the remote's references a fetch retrieves and where it stores them locally.

# Properties
- A remote's default refspec maps everything under its branch namespace (`refs/heads/`) to a local namespace under `refs/remotes/<remote>/`, which is how ordinary [[Remote-Tracking Branch|remote-tracking branches]] are created and kept up to date on every fetch.
- Additional refspecs can be configured to also fetch references that live outside the default branch namespace, storing them locally under references of the user's choosing; once configured, these behave much like remote-tracking branches themselves — read-only, and refreshed on every fetch.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=203&annotation=RZB5VVA5)
