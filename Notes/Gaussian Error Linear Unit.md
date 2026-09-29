---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Gaussian Error Linear Unit[^1]
> A smooth activation function (Hendrycks & Gimpel, 2016) that weights the input by the standard normal [[Cumulative Distribution Function|CDF]] $\Phi$:
> $$
> \begin{align}
> \mathrm{GELU}[z] = z \cdot \Phi[z]
> \end{align}
> $$

# Properties
- Approximates the [[ReLU Function|ReLU]] for large $|z|$ but is smooth and slightly negative for small negative $z$, avoiding the [[Dying ReLU Problem]] while limiting the negative-side gradient.
- Closely approximated by the [[Swish Function|SiLU]] $z\,\sigma[1.702 z]$.

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
