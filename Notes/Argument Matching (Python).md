---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Argument Matching (Python)[^1]
> By default, a [[Function (Python)|function]] call's argument values are matched to the definition's parameter names by position, left to right; a call may instead match an argument by name using `name=value` keyword syntax, and a definition may supply a default value for a parameter the caller omits.

# Properties
- Keyword arguments can be freely mixed with positional ones in a call, as long as every positional argument precedes any keyword argument; matching by name means the caller's argument order no longer has to follow the definition's order for those arguments.
- A definition can mark some parameters keyword-only, by placing them after a bare `*` or a `*name` collector (see [[Arbitrary Argument List (Python)]]) — the caller must then pass them by name — or positional-only, by placing them before a `/`, so the caller must pass them by position only.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=665&annotation=LXPEDMZT)
