---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] L2 Norm[^1]
> The $L^2$ norm of a function $f$ on $(a, b)$ is the [[Norm]] induced by the [[L2 Inner Product]]:
> $$
> \begin{align}
> \|f\| = (f, f)^{1/2} = \left[\int_a^b |f(x)|^2\, dx\right]^{1/2}.
> \end{align}
> $$
> The **$L^2$ metric** measures the "distance" between two functions:
> $$
> \begin{align}
> \|f - g\| = \left[\int_a^b |f(x) - g(x)|^2\, dx\right]^{1/2}.
> \end{align}
> $$

The idea is to treat orthogonality as a geometric property: with this distance, Fourier analysis becomes Euclidean geometry in infinitely many dimensions. Among the [[Metric|metrics]] on functions it is the nicest one, because it comes from an inner product, so the [[Pythagorean Theorem for Inner Product Space|Pythagorean theorem]], projections, and the [[Parallelogram Identity]] are available.[^1][^2]

# Properties
- Convergence in this metric is [[Mean-Square Convergence]].[^1]
- The continuous analogue of the Euclidean [[Vector Norm]] and of the [[L2 Loss]] / root-mean-square error; the special case $p = 2$ of the [[p-Norm|$L^p$ norms]].[^2]
- $\|f\|^2$ is the energy of a signal; [[Parseval's Theorem]] equates it with the energy of the Fourier coefficients.
- A function can have small $L^2$ norm while being large on a small set, which is why $L^2$ convergence does not imply pointwise convergence ([[Gibbs Phenomenon]]).[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=143&annotation=IUGLNC6N)
[^2]: Added from general knowledge.
