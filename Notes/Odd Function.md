---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Odd Function[^1]
> A function $\phi$ defined on an interval $(-l, l)$ symmetric about $x = 0$ is **odd** if
> $$
> \begin{align}
> \phi(-x) = -\phi(x) \quad \text{for all } x \in (-l, l).
> \end{align}
> $$
> Its graph is symmetric with respect to the origin.

# Properties
- Parity arithmetic: odd $\times$ odd $=$ even, odd $\times$ even $=$ odd; the sum of two odd functions is odd. The sum of an odd and an [[Even Function]] can be anything.[^2][^3]
- Differentiation and integration change parity: if $\phi$ is odd, then $\phi'$ and $\int_0^x \phi(s)\, ds$ are even (lower limit at the origin).[^4]
- If defined at the origin, the graph passes through it: setting $x = 0$ gives $\phi(0) = 0$.[^5]
- $\int_{-l}^{l} \phi\, dx = 0$; this is why the products of distinct sines and cosines integrate to zero over symmetric intervals.[^6]
- Each $\sin(n\pi x/l)$ is odd, so a convergent [[Fourier Sine Series]] sums to an odd function; a function on $(0, l)$ is made odd by its [[Odd Extension]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=S5ZX5QUE)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=VJCRFXJD)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=Y9ZRPBQF)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=NGQHHC4K)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=ZTYW8UHQ)
[^6]: Added from general knowledge.
