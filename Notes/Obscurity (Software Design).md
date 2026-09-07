---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Obscurity (Software Design)[^1]
> Exists when important information about a software system is not obvious to the developers working on it.

# Properties
- One of the two underlying causes of [[Software Complexity]], alongside [[Dependency (Software Design)]].
- Can combine with dependency when the existence of a dependency itself is not obvious.
- Inconsistency, including inconsistent [[Naming (Software Design)|naming]], is a common source of obscurity.
- Usually a symptom of poor [[Comments (Software Design)|documentation]] or of a design that is inherently complex and non-obvious; too much documentation is itself a red flag that the underlying design needs simplifying, since simplifying the design is the best way to reduce obscurity.
- Leads to [[Unknown Unknowns]].

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
