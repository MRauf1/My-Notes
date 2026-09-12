---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Lambda Expression (Python)[^1]
> An expression, `lambda arg1, arg2, ...: expression`, that creates a [[Function (Python)|function]] object and returns it as its result rather than assigning it to a name; the code after the colon is a single expression that serves as both the function's body and its implicit return value.

# Properties
- Because it is an expression rather than a statement, a lambda can appear in places where a `def` is not syntactically allowed, such as directly inside a function call's arguments or an object literal[^2].
- Limited to a single expression with no statements, a lambda is strictly less general than `def`; it is meant for small, inline pieces of deferred code, while `def` handles larger tasks[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=600&annotation=SGMXHRR6)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=729&annotation=K6YCEVZ7)
