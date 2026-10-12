---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Even Extension[^1]
> A function $\phi$ defined on $(0, l)$ extends in exactly one way to an [[Even Function]] on $(-l, l)$, its mirror image:
> $$
> \begin{align}
> \phi_{\text{even}}(x) = \begin{cases} \phi(x) & 0 < x < l, \\ \phi(-x) & -l < x < 0. \end{cases}
> \end{align}
> $$
> It is not necessarily defined at the origin.

# Properties
- Counterpart of the [[Odd Extension]].
- The [[Fourier Cosine Series]] of $\phi$ on $(0, l)$ is the full [[Fourier Series]] of $\phi_{\text{even}}$; its sum is the even $2l$-periodic extension ([[Periodic Extension]]).[^2]
- Corresponds to the [[Neumann Boundary Condition]] $u_x(0, t) = u_x(l, t) = 0$.[^2]
- Continuous at $x = 0$ automatically (equal one-sided limits), so the even periodic extension of a continuous $\phi$ on $[0, l]$ is continuous; this is why cosine expansions (e.g. the discrete cosine transform) avoid boundary jumps.[^3]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=127&annotation=D9ZNMGUU)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=127&annotation=UVTNWTAG)
[^3]: Added from general knowledge.
