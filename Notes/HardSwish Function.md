---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] HardSwish Function[^1]
> A piecewise approximation of the [[Swish Function]] (Howard et al., 2019) with a very similar shape but faster to compute:
> $$
> \begin{align}
> \mathrm{HardSwish}[z] = \begin{cases} 0 & z < -3 \\ z(z + 3)/6 & -3 \leq z \leq 3 \\ z & z > 3 \end{cases}
> \end{align}
> $$

# Properties
- Avoids evaluating the exponential in the [[Sigmoid Function|sigmoid]].

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
