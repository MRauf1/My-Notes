---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Dependency (Software Design)[^1]
> Exists when a piece of code cannot be understood and modified in isolation, because it relates to some other code that must also be understood or modified in order to change the first piece of code.

# Properties
- One of the two underlying causes of [[Software Complexity]], alongside [[Obscurity (Software Design)]].
- Cannot be eliminated entirely; the goal of good design is to reduce the number of dependencies and to make the remaining ones as simple and obvious as possible.
- Leads to [[Change Amplification]] and [[Cognitive Load (Software Design)]].
- [[Information Leakage]] is a dependency between modules that arises from a shared design decision.
- [[Pass-Through Method|Pass-through methods]] and [[Pass-Through Variable|pass-through variables]] are concrete sources of dependency between classes.
- Combines with [[Obscurity (Software Design)|obscurity]] when the existence of a dependency itself is not obvious.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
