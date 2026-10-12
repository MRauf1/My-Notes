---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!abstract] Theorem (Uniform Convergence)[^1][^2]
> Let $\{X_n\}$ be the eigenfunctions of $X'' + \lambda X = 0$ on $(a, b)$ with a [[Symmetric Boundary Condition]]. The [[Eigenfunction Expansion|Fourier series]] $\sum A_n X_n(x)$ of $f$ converges to $f(x)$ uniformly on $[a, b]$ provided that
> 1. $f$, $f'$, and $f''$ exist and are continuous on $[a, b]$, and
> 2. $f$ satisfies the given boundary conditions.
>
> For the classical Fourier series (full, sine, and cosine), $f''$ need not exist.

For the classical series the conditions can be weakened to: $f$ continuous with piecewise continuous $f'$, and the relevant extension of $f$ ([[Periodic Extension|periodic]], [[Odd Extension|odd]], or [[Even Extension|even]]) continuous; then $\sum |A_n| < \infty$ and the [[Weierstrass M-Test]] gives uniform convergence.[^3]

# Properties
- The strongest of the three modes: implies pointwise convergence and [[Mean-Square Convergence]].
- The boundary conditions matter: the [[Fourier Sine Series]] of a function with $f(0) \neq 0$ or $f(l) \neq 0$ cannot converge uniformly on $[0, l]$, since every partial sum vanishes at the endpoints (a [[Gibbs Phenomenon]] at the boundary).[^3]
- Companions: [[Fourier Series L2 Convergence Theorem]] (weakest hypotheses) and [[Fourier Series Pointwise Convergence Theorem]] (intermediate).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=140&annotation=EV3FN263)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=140&annotation=H6SYYP2E)
[^3]: Added from general knowledge.
