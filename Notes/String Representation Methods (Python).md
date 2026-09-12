---
tags:
  - computer_science
  - python
---

# Definition
> [!info] String Representation Methods (Python)[^1]
> Two [[Operator Overloading (Python)|operator-overloading]] methods let a class control how its instances display as text: `__str__`, tried first by `print` and the `str` built-in and meant to return a user-friendly display; and `__repr__`, used everywhere else — interactive echoes, the `repr` built-in, and nested appearances inside other objects — as well as by `print`/`str` themselves whenever no `__str__` is defined.

# Properties
- `__repr__` should generally give either an as-code string that could recreate the object or a detailed display aimed at developers, while `__str__` should favor a friendlier, higher-level display[^1].
- Defining just one of the two still leaves the other available: coding only `__repr__` still gives `print`/`str` a usable fallback display, and coding only `__str__` leaves `repr`, interactive echoes, and nested appearances to fall back on the default inherited from [[Object (Python)]][^1].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1157&annotation=CHTUVGPA)
