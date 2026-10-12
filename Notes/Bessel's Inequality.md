---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Theorem 1 (Bessel's Inequality)[^1]
> If $(e_1, \dots, e_n)$ is an [[Orthonormal Vector|orthonormal]] list in an [[Inner Product Space]] $V$, then for every $v \in V$,
> $$
> \begin{align}
> \sum_{i=1}^n |\langle v, e_i \rangle|^2 \leq \lVert v \rVert^2
> \end{align}
> $$

The [[Pythagorean Theorem for Inner Product Space|Pythagorean Theorem]] is a special case of this inequality: if the orthonormal list is extended to an [[Orthonormal Basis]] of $V$, then $v = \sum_{i=1}^n \langle v, e_i \rangle e_i$ and equality holds.

> [!info] Theorem 2 (Bessel's Inequality for Functions)[^2]
> Let $\{X_n\}$ be any orthogonal set of functions on $(a, b)$ and $\int_a^b |f|^2\, dx < \infty$. With Fourier coefficients $A_n = (f, X_n)/(X_n, X_n)$, the series below converges and
> $$
> \begin{align}
> \sum_{n=1}^\infty |A_n|^2 \int_a^b |X_n(x)|^2\, dx \leq \int_a^b |f(x)|^2\, dx.
> \end{align}
> $$

It follows from the [[Best Approximation Theorem|least-squares property]] of the partial sums: $0 \le \|f - \sum_{n \le N} A_n X_n\|^2 = \|f\|^2 - \sum_{n \le N} |A_n|^2 \|X_n\|^2$, so the partial sums of a positive series are bounded.

# Properties
- Equality holds if and only if $v \in \operatorname{span}(e_1, \dots, e_n)$.
- Equality for every $f$ ([[Parseval's Theorem|Parseval's equality]]) holds iff the set is a [[Complete Orthogonal Set]].
- Consequence: $|A_n|^2 \|X_n\|^2 \to 0$; for the trigonometric system the Fourier coefficients of a square-integrable function tend to zero.[^3]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=260)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=144&annotation=N97UGDA3); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=145&annotation=MQC7UR7D)
[^3]: Added from general knowledge.
