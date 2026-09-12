---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Method (Python)[^1]
> A `def` statement coded inside a [[Class (Python)|class]] body; there is nothing syntactically special about it, but such a function automatically receives [[Self (Python)|self]] as its first argument when it is called through an instance.

# Properties
- Because a nested `def` is just another top-level assignment in the class body, the method name it creates becomes a class attribute inherited by every instance and subclass, giving them shared behavior[^2].
- Accessing a method through an [[Instance (Python)|instance]] versus through its class directly produces two different kinds of objects — see [[Bound Method (Python)]].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=998&annotation=RA3Y5Q2W)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=997&annotation=D756QJNU)
