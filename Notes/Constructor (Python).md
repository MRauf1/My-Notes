---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Constructor (Python)[^1]
> The `__init__` method: automatically called by Python each time an [[Instance (Python)|instance]] is generated from a [[Class (Python)|class]], receiving the new instance as [[Self (Python)|self]] and any values passed in the class call as further arguments, so the instance can be initialized without an extra method call.

# Properties
- Optional: if a class defines no `__init__` and inherits none, calling it simply returns an empty, uninitialized instance[^1].
- The most commonly seen example of an [[Operator Overloading (Python)|operator-overloading]] method — a specially named, double-underscore method Python invokes automatically rather than through an explicit call[^1].
- A subclass that redefines `__init__` must generally call its superclass's own `__init__` explicitly, through the superclass's name, if it still needs that superclass's construction logic to run: Python's inheritance only looks up and calls the single lowest `__init__` in the class tree automatically[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=999&annotation=DYZJL9LT)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1057&annotation=Z6EWXHX9)
