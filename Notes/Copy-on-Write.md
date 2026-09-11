---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Copy-on-Write[^1]
> A technique that defers duplicating a resource until one of its copies is actually modified, so that until then both copies transparently share the same underlying memory.

# Properties
- Used by [[Fork and Exec|fork()]] to avoid immediately copying a process's memory: the child's address space initially shares the same physical pages as the parent, and a page is duplicated only once either process writes to it.
- Not used when creating a [[Thread]] via [[Clone (System Call)|clone]], since a new thread is meant to share its process's address space outright rather than receive a copy of it in the first place.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=131&annotation=U7Q4DELF)
