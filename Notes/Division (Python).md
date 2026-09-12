---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Division (Python)[^1]
> Python distinguishes true division (`/`), which always retains any fractional remainder and returns a floating-point result, from floor division (`//`), which discards the fractional part by rounding down toward the next lower whole number.

# Properties
- Floor division is often called "truncating division," but this is only accurate for positive results; because it rounds toward negative infinity rather than toward zero, it differs from strict truncation for negative operands[^2].
- The result type of `//` follows its operands: it is a float if either operand is a float, and an integer otherwise; wrapping the expression in `int(...)` forces an integer result regardless[^3].
- The related `%` (modulus) operator returns the remainder of a `//` division, typed to match its operands, and the `divmod` built-in returns both the quotient and remainder together[^4].
- Relies on the same up-conversion rules as [[Numeric Type Coercion (Python)]] when its operands are of mixed numeric type.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=153&annotation=8529MG37)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=159&annotation=ZMG6FGV7)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=159&annotation=WI3TI47A)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=159&annotation=739H8TTA)
