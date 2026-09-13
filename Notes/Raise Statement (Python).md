---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Raise Statement (Python)[^1]
> Consists of the word `raise`, followed by an exception instance, an exception class (which Python calls with no arguments to make an instance, equivalent to supplying the parentheses yourself), or nothing at all, which re-raises the exception most recently caught.

# Properties
- [[Exception (Python)|Exceptions]] are always identified by class instance objects, and only one is active at a time; once caught, an exception's life is over unless it is deliberately re-raised[^2].
- An `except` clause's optional `as name` gives the handler access to the caught exception instance itself; that name is automatically removed once the `except` block exits, so it should not be relied on afterward without first assigning it elsewhere[^3].
- An optional `from` clause lets one exception explicitly record another as its cause, so that if it goes uncaught, Python's error message discloses the full causal chain of exceptions involved[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1358&annotation=8TTH65P5)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1360&annotation=9JQ4GG6U)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1360&annotation=TMW72Z9X)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1362&annotation=BZCK4DKG)
