---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Underflow Level)[^1]
> The underflow level is the smallest positive normalized floating-point number in a [[Floating-Point Number System]]:
> $$
> \begin{align}
> \text{UFL} = \beta^L,
> \end{align}
> $$
> which has $1$ as the leading digit and $0$ for the remaining digits of the mantissa, and the smallest possible exponent.

# Properties
- No positive number smaller than $\text{UFL}$ can be represented in the floating-point system.
- Underflow is generally less serious than [[Overflow Level|overflow]], since zero is often a reasonable approximation for arbitrarily small numbers; an underflow may be silently set to zero without disrupting execution.
- Determined by the width of the exponent field, unlike [[Machine Epsilon]], which is determined by the width of the mantissa field. In all practical floating-point systems, $0 < \text{UFL} < \epsilon_{mach} < \text{OFL}$.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=39)
