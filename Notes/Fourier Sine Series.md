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

# Properties
- A special case of the [[Fourier Series]].
- The expansion in [[Eigenfunction|eigenfunctions]] of the [[Dirichlet Eigenvalue Problem on an Interval]]; arises in [[Separation of Variables]].
- The sum is only guaranteed to converge to $\ell(t)$ within $(0, \pi)$. For any values $a_n$, the resulting sum is a [[Periodic Function|periodic function]] with period $2\pi$ that is anti-symmetric (odd) about $t = 0$; i.e. the series represents the odd $2\pi$-periodic extension of $\ell$.
- The coefficient formula follows from the orthogonality $\int_0^\pi \sin(nt)\sin(mt)\,dt = \frac{\pi}{2}\delta_{nm}$ ([[Kronecker Delta]]).[^2]
- The sine and [[Fourier Cosine Series|cosine series]] of the same function agree only on $(0, \pi)$; outside that interval they give different periodic extensions (odd vs. even).

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
