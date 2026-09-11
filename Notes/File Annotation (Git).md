---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] File Annotation[^1]
> File annotation is a way of inspecting a tracked file that shows, for every line, the most recent commit that last modified it.

# Properties
- This makes it possible to trace a buggy line of code back to the specific commit that introduced it.
- The same after-the-fact code-movement detection that lets Git infer renamed files (see [[Git Rename Detection]]) can also be applied while annotating a file, to trace a line back to a different file it may originally have been copied or moved from.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=301&annotation=C4EZTPRB)
