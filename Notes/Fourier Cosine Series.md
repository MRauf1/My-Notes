---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fourier Cosine Series[^1]
> Any (sufficiently regular) function $\ell(t)$ defined on $t \in (0, \pi)$ can be expressed as an infinite linear combination of harmonically related cosines:[^2]
> $$
> \begin{align}
> \ell(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos(nt), \qquad a_n = \frac{2}{\pi} \int_0^{\pi} \ell(t) \cos(nt) \, dt
> \end{align}
> $$
> More generally, on $(0, L)$: $\ell(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos\left(\frac{n\pi t}{L}\right)$ with $a_n = \frac{2}{L} \int_0^L \ell(t) \cos\left(\frac{n\pi t}{L}\right) dt$.

**PDE form.**[^3][^4] On $(0, l)$, $\phi(x) = \tfrac12 A_0 + \sum_{n=1}^\infty A_n \cos\frac{n\pi x}{l}$, corresponding to the [[Neumann Boundary Condition|Neumann conditions]]. Since $\int_0^l \cos\frac{n\pi x}{l} \cos\frac{m\pi x}{l}\, dx = 0$ for distinct nonnegative integers $m \neq n$, for all $m \geq 0$
$$
\begin{align}
A_m = \frac2l \int_0^l \phi(x) \cos\frac{m\pi x}{l}\, dx.
\end{align}
$$
The factor $\tfrac12$ on $A_0$ lets this single formula cover $m = 0$ (where $\int_0^l 1\, dx = l$ rather than $l/2$).

# Properties
- A special case of the [[Fourier Series]].
- The expansion in [[Eigenfunction|eigenfunctions]] of the [[Neumann Eigenvalue Problem on an Interval]]; arises in [[Separation of Variables]].
- Converges to $\ell(t)$ within $(0, \pi)$; outside, the sum is the even (symmetric about $t = 0$) $2\pi$-periodic extension of $\ell$.[^2]
- The cosine and [[Fourier Sine Series|sine series]] of the same function are only equal on $(0, \pi)$ and result in different periodic extensions outside that interval.
- Each term is an [[Even Function]] of period $2l$, so the series expands an arbitrary even $2l$-periodic function on $\mathbb{R}$, namely the [[Even Extension]] of $\phi$ extended periodically.[^5]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Coefficient formula and even extension added from general knowledge.
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=118&annotation=RD39Q4L2)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=118&annotation=MZIK3DMX)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=127&annotation=UVTNWTAG)
