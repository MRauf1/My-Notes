---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Complete Orthogonal Set[^1]
> An infinite orthogonal set of functions $\{X_1(x), X_2(x), \dots\}$ on $(a, b)$ is **complete** if [[Parseval's Theorem|Parseval's equality]]
> $$
> \begin{align}
> \sum_{n=1}^\infty |A_n|^2 \int_a^b |X_n(x)|^2\, dx = \int_a^b |f(x)|^2\, dx, \qquad A_n = \frac{(f, X_n)}{(X_n, X_n)},
> \end{align}
> $$
> holds for every $f$ with $\int_a^b |f|^2\, dx < \infty$.

Equivalently, the generalized Fourier series of every square-integrable $f$ converges to $f$ in the [[Mean-Square Convergence|mean-square sense]]; equivalently, the only square-integrable function orthogonal to every $X_n$ is $f = 0$ (almost everywhere). A complete orthogonal set is an [[Orthogonal Basis]] of the [[Hilbert Space]] $L^2(a, b)$.[^2]

# Properties
- The eigenfunctions of $X'' + \lambda X = 0$ with any [[Symmetric Boundary Condition]] form a complete set ([[Fourier Series L2 Convergence Theorem]]); in particular the sines, the cosines, and the full trigonometric system are complete.[^1]
- Completeness is what [[Separation of Variables]] needs: if even one eigenfunction were missing, some initial data could not be represented.
- For any orthogonal set, complete or not, only [[Bessel's Inequality]] holds; completeness upgrades it to equality.
- Not to be confused with completeness of a metric space ([[Complete Metric Space]]), though $L^2$ is complete in that sense too.[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=145&annotation=E7B8KDWA)
[^2]: Added from general knowledge.
