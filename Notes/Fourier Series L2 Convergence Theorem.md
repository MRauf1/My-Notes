---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!abstract] Theorem ($L^2$ Convergence)[^1][^2]
> Let $\{X_n\}$ be the eigenfunctions associated with a [[Symmetric Boundary Condition]] on $(a, b)$. The [[Eigenfunction Expansion|Fourier series]] of $f$ converges to $f$ in the [[Mean-Square Convergence|mean-square sense]] in $(a, b)$ provided only that
> $$
> \begin{align}
> \|f\|^2 = \int_a^b |f(x)|^2\, dx < \infty,
> \end{align}
> $$
> that is,
> $$
> \begin{align}
> \Big\| f - \sum_{n \le N} A_n X_n \Big\| \to 0 \quad \text{as } N \to \infty.
> \end{align}
> $$
> The partial sums get nearer and nearer to $f$ in the [[L2 Norm|$L^2$ metric]].

A certain kind of convergence under a very weak assumption. The integral may even be the [[Lebesgue Integral (Measure Theory)|Lebesgue integral]]; in fact, the Lebesgue integral was invented so that this theorem would hold for the most general possible functions (the space of square-integrable functions is then complete, the Riesz–Fischer theorem).[^2][^3]

# Properties
- Equivalent to the statement that the eigenfunctions form a [[Complete Orthogonal Set]], i.e. [[Parseval's Theorem|Parseval's equality]] holds for every square-integrable $f$.[^4]
- $L^2$ convergence does not give pointwise convergence: the Fourier series of a continuous but nondifferentiable function is not guaranteed to converge pointwise; one needs information about $f'$ ([[Fourier Series Pointwise Convergence Theorem]]).[^5] Indeed there are continuous functions whose classical Fourier series diverge at a point (du Bois-Reymond, 1873).[^3]
- Up-to-date refinement (Carleson, 1966): the classical Fourier series of any $f \in L^2$ converges pointwise almost everywhere (Hunt, 1968: also for $L^p$, $p > 1$).[^3]
- The infinite-dimensional [[Spectral Theorem]]: the eigenfunctions of $-d^2/dx^2$ form an orthogonal basis of the [[Hilbert Space]] $L^2(a, b)$.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=140&annotation=EMRQV6A7)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=143&annotation=V339PMHF)
[^3]: Added from general knowledge.
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=145&annotation=E7B8KDWA)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=142&annotation=4N9KBAS6)
