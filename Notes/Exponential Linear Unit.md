---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Exponential Linear Unit[^1]
> A smooth activation function (Clevert et al., 2015):
> $$
> \begin{align}
> \mathrm{ELU}[z] = \begin{cases} \alpha\left(\exp[z] - 1\right) & z < 0 \\ z & z \geq 0 \end{cases}
> \end{align}
> $$
> with $\alpha > 0$.

# Properties
- Saturates to $-\alpha$ for very negative inputs, limiting the negative-side gradient while avoiding the [[Dying ReLU Problem]].
- Scaled to give the [[Scaled Exponential Linear Unit]].

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
