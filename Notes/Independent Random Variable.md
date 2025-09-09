---
tags: statistics, bayesian_statistics
---

# Definition

> [!info] Definition 1 ([[Independent Events|Independent]] [[Random Variable]])[^1]
> Two [[Random Variable]] $X_1, X_2$ are independent iff
> $$
> \begin{align}
> f(x_1, x_2) = f_{X_1}(x_1) f_{X_2}(x_2)
> \end{align}
> $$

Two random variables are independent iff their [[Joint Probability Distribution]] factors into a product of their [[Marginal Distribution]].

# Properties
## [[Conditional Probability]]
- If $X_1, X_2$ are independent, then $f_{X_1 | X_2}(x_1 | X_2 = x_2) = \frac{f(x_1, x_2)}{f_{X_2}(x_2)} = f_{X_1}(x_1)$

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=26)