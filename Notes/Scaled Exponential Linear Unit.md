---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Scaled Exponential Linear Unit[^1]
> A scaled [[Exponential Linear Unit|ELU]] (Klambauer et al., 2017):
> $$
> \begin{align}
> \mathrm{SELU}[z] = \lambda \cdot \begin{cases} \alpha\left(\exp[z] - 1\right) & z < 0 \\ z & z \geq 0 \end{cases}
> \end{align}
> $$
> with fixed constants $\lambda \approx 1.0507$ and $\alpha \approx 1.6733$.

# Properties
- Helps stabilize the variance of the activations across layers when the input variance has a limited range (self-normalizing networks).

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
