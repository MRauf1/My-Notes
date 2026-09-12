---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Match Statement (Python)[^1]
> A compound statement, added in Python 3.10, that evaluates a header expression and compares it, top to bottom, against the values in a series of indented `case` clauses, running the first matching clause's block and then exiting; a trailing `case _` supplies a fallback default.

# Properties
- At its basic level, it works like a "switch" statement in other languages and can replace both an [[If Statement (Python)|if/elif/else]] chain and dictionary-based branching for simple, fixed-value dispatch[^2].
- A `case` header can list several alternatives separated by `|` (matched if any one matches), and can bind the matched value to a name with `as`; any name bound during a successful match outlives the statement and remains usable in the enclosing scope[^1].
- Beyond this basic multiple-choice level, `match` also supports full structural pattern matching, which can destructure sequences, mappings, attributes, and instances by shape — a considerably more complex facility than ordinary branching logic[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=468&annotation=2ESVSX2I)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=467&annotation=GGLU26SP)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=470&annotation=5RZDUX54)
