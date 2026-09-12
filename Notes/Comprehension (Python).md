---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Comprehension (Python)[^1]
> Syntax that builds a new collection by running an expression on each item of a sequence or other [[Iterable and Iterator (Python)|iterable]], one at a time from left to right; a list comprehension is written in square brackets and produces a new [[Python List|list]].

# Properties
- Works over any iterable object, not just physically stored sequences, so comprehensions are more accurately thought of as general iteration tools[^2].
- The same syntax enclosed in parentheses instead produces a generator (see [[Iterable and Iterator (Python)]]), and enclosed in curly braces produces a [[Python Set|set]] comprehension or, with a `key: value` pair, a [[Python Dictionary|dictionary]] comprehension[^3].
- A comprehension's nested `for` can carry an associated `if` clause that filters out items for which the test is false, and its full syntax allows any number of `for` clauses — equivalent to nested loops — each with its own optional `if`[^4].
- Because its iteration runs inside the interpreter's own optimized internals rather than as manually interpreted Python bytecode, a list comprehension typically runs faster than the equivalent manual [[For Loop (Python)|for loop]] that builds the same list[^5].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=117&annotation=WJJM62HG)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=118&annotation=PT3WQGE7)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=119&annotation=5KT85PKW)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=548&annotation=L6FYBINV)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=546&annotation=J7YRBLQS)
