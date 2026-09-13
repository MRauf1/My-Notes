---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Exception Class Hierarchy (Python)[^1]
> A raised [[Exception (Python)|exception]] matches an `except` clause if that clause names the exception's own class or any [[Superclass and Subclass (Python)|superclass]] of it — so an exception hierarchy lets a superclass act as a whole category, caught by naming just that superclass, while its subclasses represent specific kinds of exception within that category.

# Properties
- User-defined exceptions are ordinary classes that must inherit, directly or indirectly, from the built-in `Exception` class — the root of nearly all application-level exceptions — rather than from `BaseException`, the true topmost root, reserved for the language's own system-exit-style events; naming `Exception` in an `except` clause therefore catches essentially everything except those system events, which should normally be left to propagate[^2].
- Unless a class replaces the default [[Constructor (Python)|constructor]] it inherits from `BaseException`, any arguments passed when an exception instance is created are automatically stored in its `args` tuple attribute and automatically included in its printed display[^3].
- Because it is a class, an exception can also carry its own attributes and methods beyond this default, giving handlers a natural place to find extra context about what went wrong[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1379&annotation=LG3FI8GG)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1387&annotation=J7S32ZGA)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1389&annotation=IHCZZK98)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1378&annotation=9KIQ7K8Y)
