---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Decorator (Python)[^1]
> A callable object — typically a function — that processes another function or class, applied with `@decorator` syntax directly above a `def` or `class` statement; a decorator automatically rebinds the name being defined to the decorator's result at the end of that statement, rather than leaving it bound to the original [[Function (Python)|function]] or [[Class (Python)|class]] itself.

# Properties
- Comes in two flavors: a function decorator rebinds a function's name at the end of its `def`, typically installing a wrapper ("call proxy") that intercepts later calls to it; a class decorator rebinds a class's name at the end of its `class` statement, typically installing a wrapper ("interface proxy") that intercepts later instance-creation calls[^2].
- Because it runs once, when the function or class is defined, rather than needing to be invoked at every call site, a decorator applies the same augmentation — tracing, timing, access control, and the like — more explicitly and less error-pronely than manually wrapping every call by hand[^3].
- Need not wrap its target in a proxy at all: it may instead manage the function or class object directly and simply return it — unchanged or augmented — as a plain post-creation step[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1557&annotation=36FESDA2)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1558&annotation=47FIUPPW)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1560&annotation=YMB95BAD)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1559&annotation=NALEYE89)
