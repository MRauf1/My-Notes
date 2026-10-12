---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] L2 Inner Product[^1][^2]
> For real-valued continuous functions $f, g$ on $a \leq x \leq b$,
> $$
> \begin{align}
> (f, g) = \int_a^b f(x)\, g(x)\, dx.
> \end{align}
> $$
> For complex-valued functions,
> $$
> \begin{align}
> (f, g) = \int_a^b f(x)\, \overline{g(x)}\, dx,
> \end{align}
> $$
> where the bar denotes the [[Complex Conjugate]]. The functions are **orthogonal** if $(f, g) = 0$.

The terminology is borrowed from the dot product of ordinary vectors: the integral is the continuous limit of $\sum_i f(x_i) \overline{g(x_i)}\, \Delta x$, so functions behave as vectors with a continuum of components ([[Function Space]]).

# Properties
- An [[Inner Product]], making continuous functions on $[a, b]$ an [[Inner Product Space]]; its completion is the [[Hilbert Space]] $L^2(a, b)$ of square-integrable functions (with the [[Lebesgue Integral (Measure Theory)|Lebesgue integral]]).[^3]
- No continuous function is orthogonal to itself except $f \equiv 0$.[^1]
- Induces the [[L2 Norm]] $\|f\| = (f, f)^{1/2}$ and the $L^2$ metric $\|f - g\|$.
- The key property behind every Fourier coefficient formula is the orthogonality of eigenfunctions in this inner product ([[Symmetric Boundary Condition Orthogonality Theorem]]).[^1]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=130&annotation=C326VLDR)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=133&annotation=TPG9WBYP)
[^3]: Added from general knowledge.
