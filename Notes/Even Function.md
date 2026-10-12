---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Even Function[^1]
> A function $\phi$ defined on an interval $(-l, l)$ symmetric about $x = 0$ is **even** if
> $$
> \begin{align}
> \phi(-x) = \phi(x) \quad \text{for all } x \in (-l, l).
> \end{align}
> $$
> Its graph is symmetric with respect to the $y$-axis: the left and right halves are mirror images.

# Properties
- Parity arithmetic: even $\times$ even $=$ even, odd $\times$ odd $=$ even, even $\times$ odd $=$ odd; the sum of two even functions is even. The sum of an even and an [[Odd Function]] can be anything.[^2][^3]
- Every function on $(-l, l)$ splits uniquely into an even and an odd part: $\phi(x) = \tfrac12[\phi(x) + \phi(-x)] + \tfrac12[\phi(x) - \phi(-x)]$.[^5]
- Differentiation and integration change parity: if $\phi$ is even, then $\phi'$ and $\int_0^x \phi(s)\, ds$ are odd (lower limit at the origin).[^4]
- If $\phi$ is differentiable at $0$, its graph crosses the $y$-axis horizontally: $\phi'(0) = 0$, since $\phi'$ is odd.[^6]
- $\int_{-l}^{l} \phi\, dx = 2\int_0^l \phi\, dx$.[^5]
- The left and right limits at $0$ coincide ([[One-Sided Limit of Even Function]]).
- Each $\cos(n\pi x/l)$ is even, so a convergent [[Fourier Cosine Series]] sums to an even function; a function on $(0, l)$ is made even by its [[Even Extension]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=S5ZX5QUE)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=VJCRFXJD)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=Y9ZRPBQF)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=NGQHHC4K)
[^5]: Added from general knowledge.
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=ZTYW8UHQ)
