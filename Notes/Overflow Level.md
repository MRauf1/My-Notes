---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Overflow Level)[^1]
> The overflow level is the largest floating-point number representable in a [[Floating-Point Number System]]:
> $$
> \begin{align}
> \text{OFL} = \beta^{U+1}(1 - \beta^{-p}),
> \end{align}
> $$
> which has $\beta - 1$ as the value of each digit of the mantissa and the largest possible exponent.

# Properties
- No number larger than $\text{OFL}$ can be represented in the floating-point system.
- Overflow is generally more serious than [[Underflow Level|underflow]], since there is no good floating-point approximation to arbitrarily large numbers; on many systems an overflow aborts the program with a fatal error.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=39)
