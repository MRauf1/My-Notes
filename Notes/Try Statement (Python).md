---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Try Statement (Python)[^1]
> The [[Compound Statement (Python)|compound statement]] that catches [[Exception (Python)|exceptions]]: Python runs the statements nested under its header, then behaves according to one of three cases — an exception occurs and matches a named `except`, an exception occurs but matches none, or no exception occurs at all.

# Properties
- Exception and match: Python runs the topmost `except` clause that matches the raised exception, optionally binding the exception object to a name via `as`, then resumes execution after the entire try statement[^2].
- Exception and no match: the exception instead propagates out of the try statement entirely, to be matched against handlers elsewhere — see [[Exception Propagation (Python)]][^3].
- No exception: Python runs the optional `else` clause, if present, then resumes after the statement — giving explicit code for "nothing went wrong," which is otherwise indistinguishable from "something went wrong but was silently handled"[^4].
- An `except` clause can name a single exception class, a tuple of classes, or omit a name entirely to match anything; a raised exception matches a named class if it is that class or any subclass of it — see [[Exception Class Hierarchy (Python)]][^5].
- Must include at least one of `except`, `else`, or `finally`; an `else` requires at least one `except` to be present, and whichever parts do appear must be ordered `try -> except -> else -> finally`[^6].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1341&annotation=3AGZ73M3)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1341&annotation=32VG6J3B)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1341&annotation=S4989YFU)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1345&annotation=B92C49TD)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1342&annotation=UHEZB9XA)
[^6]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1354&annotation=DVE73PK5)
