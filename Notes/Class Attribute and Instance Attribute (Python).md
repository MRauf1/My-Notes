---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Class Attribute and Instance Attribute (Python)[^1]
> Where an attribute-creating assignment is physically run determines whose namespace it lands in: an assignment at the top level of a class statement's body attaches a class attribute, shared by every instance and subclass, while an assignment to an attribute of [[Self (Python)|self]] inside a method attaches an instance attribute, private to that one instance.

# Properties
- Because [[Attribute Inheritance (Python)|inheritance search]] runs only on reference and never on assignment, an instance attribute of the same name as a class attribute simply shadows the class's version for that one instance, without altering or replacing it in the class or in any other instance[^2].
- Any attribute, wherever it lives, can still be reached directly and unambiguously by qualifying the exact object that holds it — e.g., `ClassName.attr` always fetches the class's own version, bypassing the usual instance-first search order[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=997&annotation=D756QJNU)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1088&annotation=J9E64Y6L)
