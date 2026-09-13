---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Context Manager (Python)[^1]
> The object a `with expression [as variable]:` statement operates on, required to define `__enter__` and `__exit__` methods; Python evaluates `expression`, calls the result's `__enter__` (assigning its return value to `variable` if given), runs the nested block, and then calls `__exit__` regardless of whether that block raised an exception.

# Properties
- If the `with` block raises, `__exit__` receives the exception's type, value, and traceback and may suppress it by returning a true value — otherwise the exception is re-raised after `__exit__` returns; if the block raised nothing, `__exit__` still runs, but with all three arguments set to `None`[^2].
- A single `with` statement can list multiple context managers separated by commas, running every one's entry action on the way in and every one's exit action, in turn, on the way out — exception or not[^3].
- Narrower but often more concise than a [[Finally Clause (Python)|try/finally]] pair: it only works for objects that already implement the protocol (or a class written to do so), but it can additionally run startup actions and gives full access to Python's OOP tools ([[Operator Overloading (Python)|operator overloading]]) for managing a code block's context[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1370&annotation=YR4QK87K)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1370&annotation=CJJ5RT4I)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1372&annotation=C75W4RD3)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1367&annotation=A2A2EW4G)
