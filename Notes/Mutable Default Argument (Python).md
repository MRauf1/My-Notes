---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Mutable Default Argument (Python)[^1]
> A well-known pitfall: if a [[Function (Python)|function's]] default argument value is a [[Mutability (Python)|mutable]] object, that same single object is created once and reused on every call that doesn't override it, so any in-place change made to it during one call persists and is visible on the next.

# Properties
- To reset such a default on every call instead, create the object fresh inside the function body rather than in the header, so a new object is built each time the function runs.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=674&annotation=LGU7T6RZ)
