---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Periodic Extension[^1]
> A function defined only on an interval of length $p$ extends in exactly one way to a [[Periodic Function]] of period $p$ on $\mathbb{R}$. For $\phi$ on $(-l, l)$, the periodic extension (period $2l$) is
> $$
> \begin{align}
> \phi_{\text{per}}(x) = \phi(x - 2lm) \quad \text{for } -l + 2lm < x < l + 2lm, \quad m \in \mathbb{Z}.
> \end{align}
> $$
> The definition leaves the values at the endpoints $x = l + 2lm$ unspecified; the extension has [[Jump Discontinuity|jumps]] there unless $\phi(l^-) = \phi(-l^+)$.

# Types
- [[Odd Extension]] followed by periodic extension: the odd $2l$-periodic extension of a function on $(0, l)$.
- [[Even Extension]] followed by periodic extension: the even $2l$-periodic extension of a function on $(0, l)$.

# Properties
- Every term of the full [[Fourier Series]] on $(-l, l)$ has period $2l$, so its sum (if it converges) does too: the full Fourier series is equally an expansion of a function on $(-l, l)$ or of a $2l$-periodic function on $\mathbb{R}$, namely $\phi_{\text{per}}$.[^2][^3]
- Corresponds to the [[Periodic Boundary Condition]] $u(-l, t) = u(l, t)$, $u_x(-l, t) = u_x(l, t)$.[^4]
- The pointwise limit of the Fourier series on all of $\mathbb{R}$ is $\tfrac12[\phi_{\text{per}}(x^+) + \phi_{\text{per}}(x^-)]$, so jumps of the extension at the endpoints produce midpoint values there ([[Fourier Series Pointwise Convergence Theorem]]).
- In image processing, the implicit periodic extension of a finite signal by the [[Discrete Fourier Transform]] creates artificial edges at the borders whenever the opposite ends do not match.[^5]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=125&annotation=3SZEFNXK)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=125&annotation=FBU7VNRG)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=PVFXJPIN)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=127&annotation=UVTNWTAG)
[^5]: Added from general knowledge.
