---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Change Amplification[^1]
> A manifestation of [[Software Complexity]] in which a seemingly simple change requires code modifications in many different places.

# Properties
- A hallmark of good design is that it reduces the amount of code affected by any single design decision, so good design should not require many modifications for a simple change.
- Primarily driven by [[Dependency (Software Design)|dependencies]] between modules.
- More tedious than dangerous, unlike [[Unknown Unknowns]], since the developer at least knows which places need to change.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
