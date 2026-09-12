---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Global Statement (Python)[^1]
> A declaration inside a [[Function (Python)|function]] that tells Python one or more listed names refer to the enclosing module's scope, so that assigning them changes that module-level name instead of creating a new local one.

# Properties
- Only required for names a function assigns; a function can read a global name freely, without declaring it, per the [[LEGB Rule (Python)|LEGB rule]][^1].
- Accepted practice favors having functions communicate through arguments and return values rather than through global state: because a global variable's value can depend on the order of calls to arbitrarily distant functions, relying on globals tends to make programs harder to debug and reason about[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=624&annotation=TSKTB9GL)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=626&annotation=SG6CZK48)
