---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Swish Function[^1]
> An activation function found by an empirical search over function space for the best performance across a variety of [[Supervised Learning|supervised learning]] tasks (Ramachandran et al., 2017):
> $$
> \begin{align}
> \mathrm{Swish}[z] = \frac{z}{1 + \exp[-\beta z]} = z \cdot \sigma[\beta z]
> \end{align}
> $$
> where $\beta$ is a learned parameter and $\sigma$ is the [[Sigmoid Function|sigmoid]].

# Properties
- $\beta = 1$ gives the **sigmoid linear unit** (SiLU) $z\,\sigma[z]$ (Hendrycks & Gimpel, 2016; Elfwing et al., 2018), so Swish was a rediscovery; $\beta \to \infty$ recovers the [[ReLU Function|ReLU]] and $\beta = 0$ gives the linear $z/2$.
- Smooth, and avoids the [[Dying ReLU Problem]] while limiting the negative-side gradient.
- Approximated by the cheaper [[HardSwish Function]].

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
