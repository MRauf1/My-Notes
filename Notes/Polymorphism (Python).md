---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Polymorphism (Python)[^1]
> A general property of Python whereby the meaning of an operation depends on the [[Object (Python)|objects]] being operated on, rather than on the operation's syntax alone.

# Properties
- Python itself automatically overloads some operators so that they act differently depending on the type of the built-in objects involved: `+` performs addition on numbers but concatenation on sequence objects like strings and lists[^2].
- Any operator can further be overloaded — i.e., implemented — by a Python class or a C extension type, so its meaning on user-defined objects can be anything the class author chooses[^3].
- Underlies [[Duck Typing (Python)]]: code written against an object's interface, rather than its specific type, automatically works across any type that implements a compatible interface.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=105&annotation=X3L98WIF)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=151&annotation=JBFV8GHU)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=151&annotation=SZVY8YFP)
