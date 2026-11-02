---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Surface Riemann Integral (Surface Integral of Scalar Function)[^1]
> Let $S$ be a surface divided into patches $S_{ij}$ of [[Surface Area|area]] $\Delta S_{ij}$, and let $P_{ij}^* \in S_{ij}$ be sample points. The surface integral of $f$ over $S$ is
> $$
> \begin{align}
> \iint_S f(x, y, z)\, dS = \lim_{m, n \to \infty} \sum_{i=1}^{m} \sum_{j=1}^{n} f(P_{ij}^*)\, \Delta S_{ij}
> \end{align}
> $$
> If $S$ is parametrized by $\mathbf{r}(u, v)$, $(u, v) \in D$, it reduces to a [[Double Riemann Integral|double integral]] over the parameter domain:
> $$
> \begin{align}
> \iint_S f(x, y, z)\, dS = \iint_D f(\mathbf{r}(u, v))\, \lvert \mathbf{r}_u \times \mathbf{r}_v \rvert\, dA
> \end{align}
> $$

It is the [[Riemann Integral]] over a 2-dimensional surface, analogous to the [[Line Riemann Integral|line integral]] over a curve.

# Properties
- The factor $\lvert \mathbf{r}_u \times \mathbf{r}_v \rvert$ (a [[Cross Product]] norm) is the area scaling of the parametrization; with $f \equiv 1$ the integral gives the area of $S$.
- For a graph $z = g(x, y)$ over $D$: $\displaystyle \iint_S f\, dS = \iint_D f(x, y, g(x, y)) \sqrt{1 + g_x^2 + g_y^2}\, dA$.
- The value doesn't depend on the parametrization chosen for $S$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5), §16.7 Surface Integrals
