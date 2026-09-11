---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Git Rename Detection[^1]
> [[Git]] does not explicitly record that a file was renamed as part of its stored history; instead, it infers renames after the fact by detecting that a new file's content is highly similar to a file that disappeared in the same snapshot.

# Properties
- This is a consequence of the [[Git Snapshot Model|snapshot-based, content-addressed data model]]: Git records what files look like at each commit rather than named operations performed on them, so it has no explicit "rename" event to store in the first place.
- Unlike many other version control systems, which do store an explicit rename operation, Git's detection is purely a heuristic comparison performed when the history is inspected.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=45&annotation=MRAUDX9I)
