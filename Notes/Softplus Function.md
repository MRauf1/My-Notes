---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Softplus Function[^1]
> A smooth approximation of the [[ReLU Function|ReLU]] (Glorot et al., 2011):
> $$
> \begin{align}
> \mathrm{softplus}[z] = \log\left[1 + \exp[z]\right]
> \end{align}
> $$

# Properties
- Its derivative is the [[Sigmoid Function|sigmoid]] $\sigma[z]$, which is positive everywhere, avoiding the [[Dying ReLU Problem]].

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
