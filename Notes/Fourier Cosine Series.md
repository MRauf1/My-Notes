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

# Properties
- A special case of the [[Fourier Series]].
- The expansion in [[Eigenfunction|eigenfunctions]] of the [[Neumann Eigenvalue Problem on an Interval]]; arises in [[Separation of Variables]].
- Converges to $\ell(t)$ within $(0, \pi)$; outside, the sum is the even (symmetric about $t = 0$) $2\pi$-periodic extension of $\ell$.[^2]
- The cosine and [[Fourier Sine Series|sine series]] of the same function are only equal on $(0, \pi)$ and result in different periodic extensions outside that interval.

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Coefficient formula and even extension added from general knowledge.
