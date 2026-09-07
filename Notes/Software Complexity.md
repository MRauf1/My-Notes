---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Software Complexity[^1]
> Anything related to the structure of a software system that makes the system hard to understand and modify. The complexity contributed by a given part of the system is weighted by the fraction of time developers spend working on that part, so isolating complexity where it will rarely be encountered is nearly as good as eliminating it outright.

# Properties
- Manifests in three ways: [[Change Amplification]], [[Cognitive Load (Software Design)]], and [[Unknown Unknowns]].
- Caused by two underlying factors: [[Dependency (Software Design)]] and [[Obscurity (Software Design)]].
- Accumulates incrementally from many small design decisions rather than from a single large mistake, which is why [[Strategic Programming|strategic programmers]] treat every small increase in complexity with "zero tolerance."
- Good design is a system that is obvious and clear to the developers working on it.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
