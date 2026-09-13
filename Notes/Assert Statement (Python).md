---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Assert Statement (Python)[^1]
> `assert test, data` — shorthand for a conditional [[Raise Statement (Python)|raise]]: if `test` evaluates to false, Python raises the built-in `AssertionError`, using the optional `data` value as its constructor argument and hence its displayed message.

# Properties
- Intended mainly for trapping user-defined constraints and sanity checks during development, not for catching the kinds of errors Python already detects and raises on its own, such as out-of-bounds indexing or type mismatches[^2].
- Can be stripped from a program's compiled [[Python Bytecode|bytecode]] entirely, and hence not run at all, by running Python with its `-O` optimization flag, which sets the built-in `__debug__` name to `False`[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1364&annotation=ZY5CY4SC)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1366&annotation=BMTX3LS6)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1365&annotation=QSNIRDEZ)
