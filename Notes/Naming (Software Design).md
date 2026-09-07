---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Naming (Software Design)[^1]
> The choice of identifiers is itself a design activity: good names form a kind of documentation, making code easier to understand, reducing [[Software Complexity|complexity]], and helping catch bugs and ambiguities.

# Properties
- A good name creates an image close to what the named thing actually is and does, ideally understandable before its documentation or implementation is read.
- Good names are precise and consistent; the same name should be reused for things that serve the same purpose in different places, which reduces [[Cognitive Load (Software Design)|cognitive load]].
- Imprecise names, such as `i` or `j` for loop counters, are acceptable only when the named thing is used in a small, easily inspected scope.
- Difficulty finding a name that is simultaneously simple, precise, and consistent is itself a red flag that the underlying design is not clean.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
