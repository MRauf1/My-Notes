---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Named Expression (Python)[^1]
> The `:=` ("walrus") operator: the expression `name := value` evaluates `value`, assigns the result to `name`, and also returns that result as the value of the overall expression.

# Properties
- Unlike an ordinary [[Assignment Statement (Python)|assignment]], `:=` can be nested inside contexts where a statement is not allowed, letting code fetch, assign, and test a value all within one expression — such as a `while` loop's header test[^2].
- Only a single, simple variable name is permitted on its left side; other assignment-statement forms and references to data-structure components, such as an index or attribute, are not allowed there[^3].
- Because `:=` binds tighter than comparison operators and is not itself permitted as a bare statement, it is conventionally wrapped in its own parentheses to set it off visually and avoid changing the meaning of the surrounding expression[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=436&annotation=87RJG5S8)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=405&annotation=RL33BPR7)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=436&annotation=AEASVGZ8)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=438&annotation=X4ZENPTN)
