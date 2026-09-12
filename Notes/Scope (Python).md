---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Scope (Python)[^1]
> The namespace a name lives in, determined entirely by where that name is assigned in the source code; Python uses lexical scoping, so a name's scope is fixed by the static location of its assignment rather than by which function calls which at runtime.

# Properties
- A name assigned inside a `def` or lambda is local to that function; a name assigned in a syntactically enclosing `def` or lambda is nonlocal to functions nested within it; a name assigned outside every function is global to its entire containing module[^1].
- Every call to a function creates a brand-new local scope, so each active call gets its own independent copy of that function's local names — a requirement for both recursion and [[Closure (Python)|closures]] to behave correctly[^2].
- Only an actual name assignment changes what scope a name belongs to; changing a [[Mutability (Python)|mutable]] object in place does not. For example, `L.append(x)` leaves `L` in whatever scope it already had, while `L = x` would make `L` local to the enclosing function[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=611&annotation=JUPRPHVI)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=613&annotation=3DHQXUJU)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=615&annotation=68NEQ9G8)
