---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Parseval's Theorem[^1]
> For images $\ell_1, \ell_2$ of size $N \times M$ with [[Discrete Fourier Transform|DFTs]] $\mathscr{L}_1, \mathscr{L}_2$:
> $$
> \begin{align}
> \sum_{n=0}^{N-1} \sum_{m=0}^{M-1} \ell_1[n, m] \, \ell_2^*[n, m] = \frac{1}{NM} \sum_{u=0}^{N-1} \sum_{v=0}^{M-1} \mathscr{L}_1[u, v] \, \mathscr{L}_2^*[u, v]
> \end{align}
> $$

> [!info] Plancherel Theorem[^1]
> In particular, if $\ell_1 = \ell_2 = \ell$:
> $$
> \begin{align}
> \sum_{n=0}^{N-1} \sum_{m=0}^{M-1} \left| \ell[n, m] \right|^2 = \frac{1}{NM} \sum_{u=0}^{N-1} \sum_{v=0}^{M-1} \left| \mathscr{L}[u, v] \right|^2
> \end{align}
> $$

# Properties
- Holds because the DFT is a change of basis to an [[Orthogonal Basis|orthogonal basis]] ([[Discrete Complex Exponential]]), so the [[Inner Product|inner product]] and norm are preserved up to a constant factor ([[Inner Product and Vector Norm under Orthonormal Basis]]); with the normalized [[DFT Matrix]] the factor disappears.
- The [[Signal Energy|energy]] of a signal can be computed as the sum of the squared magnitudes of its Fourier transform.
- Continuous version (general knowledge): $\int_{-\infty}^{\infty} \ell_1(t) \ell_2^*(t) \, dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} \mathscr{L}_1(w) \mathscr{L}_2^*(w) \, dw$ ([[Fourier Transform]]).[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
