---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Short-Circuit Evaluation (Python)[^1]
> The behavior of Python's `and` and `or` operators, which always return one of their actual operand objects — never a plain `True`/`False` — and stop evaluating operands from left to right as soon as the overall result is determined.

# Properties
- `or` evaluates its operands left to right and returns the first one that is true, since a true value on the left already makes the whole `or` true; if every operand is false, it returns the last one evaluated[^1].
- `and` evaluates its operands left to right and returns the first one that is false, since a false value on the left already makes the whole `and` false; if every operand is true, it returns the last one evaluated[^1].
- This differs from magnitude comparisons like `<` or `>`, which do return the actual `True`/`False` objects — themselves just customized versions of the integers 1 and 0[^1].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=482&annotation=HJ58F24H)
