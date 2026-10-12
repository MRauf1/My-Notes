---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fourier Sine Series[^1]
> Any (sufficiently regular) function $\ell(t)$ defined on $t \in (0, \pi)$ can be expressed as an infinite linear combination of harmonically related sines:
> $$
> \begin{align}
> \ell(t) = a_1 \sin(t) + a_2 \sin(2t) + a_3 \sin(3t) + \dots = \sum_{n=1}^{\infty} a_n \sin(nt)
> \end{align}
> $$
> where each coefficient is the (scaled) area under the curve $\ell(t) \sin(nt)$:
> $$
> \begin{align}
> a_n = \frac{2}{\pi} \int_0^{\pi} \ell(t) \sin(nt) \, dt
> \end{align}
> $$
> More generally, on $(0, L)$: $\ell(t) = \sum_{n=1}^{\infty} a_n \sin\left(\frac{n\pi t}{L}\right)$ with $a_n = \frac{2}{L} \int_0^L \ell(t) \sin\left(\frac{n\pi t}{L}\right) dt$.[^2]

**PDE form.**[^3][^4][^5] On $(0, l)$, $\phi(x) = \sum_{n=1}^\infty A_n \sin\frac{n\pi x}{l}$. Since $\int_0^l \sin\frac{n\pi x}{l} \sin\frac{m\pi x}{l}\, dx = 0$ for distinct positive integers $m \neq n$ (and $= l/2$ for $m = n$), multiplying by $\sin(m\pi x/l)$ and integrating forces
$$
\begin{align}
A_m = \frac2l \int_0^l \phi(x) \sin\frac{m\pi x}{l}\, dx.
\end{align}
$$
These are the only possible coefficients; whether the series then converges to $\phi$ is a separate question ([[Fourier Series Pointwise Convergence Theorem]]).

# Properties
- A special case of the [[Fourier Series]].
- The expansion in [[Eigenfunction|eigenfunctions]] of the [[Dirichlet Eigenvalue Problem on an Interval]]; arises in [[Separation of Variables]].
- The sum is only guaranteed to converge to $\ell(t)$ within $(0, \pi)$. For any values $a_n$, the resulting sum is a [[Periodic Function|periodic function]] with period $2\pi$ that is anti-symmetric (odd) about $t = 0$; i.e. the series represents the odd $2\pi$-periodic extension of $\ell$.
- The coefficient formula follows from the orthogonality $\int_0^\pi \sin(nt)\sin(mt)\,dt = \frac{\pi}{2}\delta_{nm}$ ([[Kronecker Delta]]).[^2]
- The sine and [[Fourier Cosine Series|cosine series]] of the same function agree only on $(0, \pi)$; outside that interval they give different periodic extensions (odd vs. even).
- Each term is an [[Odd Function]] of period $2l$, so the series expands an arbitrary odd $2l$-periodic function on $\mathbb{R}$, namely the [[Odd Extension]] of $\phi$ extended periodically; this matches the [[Dirichlet Boundary Condition]].[^6]
- For the [[Wave Equation on a Finite Interval]] with Dirichlet ends, the initial velocity gives $\frac{m\pi c}{l} B_m = \frac2l \int_0^l \psi(x) \sin\frac{m\pi x}{l}\, dx$.[^7]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=116&annotation=WLDUM4I8)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=117&annotation=LYCBMHLU)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=117&annotation=8QN49W2R)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=127&annotation=UVTNWTAG)
[^7]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=118&annotation=JKCPVALG)
