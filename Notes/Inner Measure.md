---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Inner Measure[^1]
> Let $\mu^*$ be an [[Outer Measure]] on $X$ induced from a finite [[Premeasure]] $\mu_0$. The inner measure of $E \subseteq X$ is
> $$
> \begin{align}
> \mu_*(E) = \mu_0(X) - \mu^*(E^c).
> \end{align}
> $$

Approximation of $E$ from the inside, obtained as the total size minus the outside approximation of the complement (the "inner area" idea behind [[Outer Measure]]).

# Properties
- $E$ is [[Carathéodory Measurable Set|$\mu^*$-measurable]] if and only if $\mu_*(E) = \mu^*(E)$.[^1]
- $\mu_*(E) \leq \mu^*(E)$ always.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=45&annotation=63LJDDBS)
