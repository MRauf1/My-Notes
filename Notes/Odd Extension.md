---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Odd Extension[^1]
> A function $\phi$ defined on $(0, l)$ extends in exactly one way to an [[Odd Function]] on $(-l, l)$, its image through the origin:
> $$
> \begin{align}
> \phi_{\text{odd}}(x) = \begin{cases} \phi(x) & 0 < x < l, \\ -\phi(-x) & -l < x < 0, \\ 0 & x = 0. \end{cases}
> \end{align}
> $$

# Properties
- Counterpart of the [[Even Extension]].
- The [[Fourier Sine Series]] of $\phi$ on $(0, l)$ is the full [[Fourier Series]] of $\phi_{\text{odd}}$; its sum is the odd $2l$-periodic extension ([[Periodic Extension]]).[^2]
- Corresponds to the [[Dirichlet Boundary Condition]] $u(0, t) = u(l, t) = 0$; it is the extension used by the [[Method of Reflection]] for Dirichlet problems.[^2]
- Has a jump at $x = 0$ (and at $x = l$ after periodic extension) unless $\phi(0^+) = 0$ (resp. $\phi(l^-) = 0$).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=127&annotation=D9ZNMGUU)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=127&annotation=UVTNWTAG)
