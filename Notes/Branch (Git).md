---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Branch[^1]
> A branch in [[Git]] is a lightweight, movable pointer to a commit; branching means diverging from the main line of development to continue work without disturbing that main line.

# Properties
- A branch is a particular kind of [[Reference (Git)|reference]], kept under its own dedicated namespace; only references in this namespace are recognized as branches and retrieved automatically by an ordinary clone or fetch.
- A branch is stored as a simple file containing the 40-character SHA-1 checksum of the commit it points to, so creating or destroying a branch is as cheap as writing that checksum to a file.
- Because each commit already records its parent(s), finding a proper common ancestor between two branches for merging is done automatically and easily.
- These properties make branching and switching between branches nearly instantaneous, so Git — unlike many other version control systems — encourages workflows that branch and merge often, even many times a day.
- The default name given to a repository's initial branch (conventionally "master" or "main") carries no special meaning to Git; it is merely a configurable convention.
- Renaming a branch that other collaborators are already using, especially a shared default branch, can break their local setups as well as any integrations, services, or build/release scripts that reference it by name, so it should only be done after coordinating with collaborators and updating all references to the old name.

# Types
- [[Topic Branch]]
- [[Long-Running Branch]]
- [[Remote-Tracking Branch]]
- [[Tracking Branch (Git)]]

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=69&annotation=9CYNWC3R)
