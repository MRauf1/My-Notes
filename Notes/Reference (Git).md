---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Reference[^1]
> A reference (ref) is a name, stored under the [[Git File States|Git directory]], that resolves to a commit or to another reference; [[Branch (Git)|branches]] and [[Git Tag|tags]] are both kinds of references, kept in their own separate namespaces.

# Properties
- Only references kept under the branch namespace (`refs/heads/`) are treated as branches and retrieved automatically by an ordinary clone or fetch; references kept under other namespaces exist on the remote but are ignored by a normal fetch unless a [[Refspec|refspec]] is configured to retrieve them.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=203&annotation=M9ZDRFPH)
