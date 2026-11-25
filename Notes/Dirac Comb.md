---
tags:
  - mathematics
  - real_analysis
  - cryoEM
---

# Definition
> [!info] Dirac Comb (Shah Function)[^1]
> The one-dimensional lattice of unit impulses ([[Dirac Delta Function]]), $\text{Ш}(x) = \sum_{n\in\mathbb{Z}}\delta(x - n)$. It is its own [[Fourier Transform]]. With spacing $a$,
> $$
> \begin{align}
> \sum_{n}\delta(x - na) \ \xrightarrow{\ \mathcal{F}\ }\ \frac{1}{a}\sum_{m}\delta\Big(u - \frac{m}{a}\Big).
> \end{align}
> $$

# Properties
- **Reciprocal lattice.** Spacing $a$ in real space becomes spacing $1/a$ in frequency space ([[Fourier Scaling Theorem]]). Comb functions model crystal lattices, so this is the origin of "reciprocal space" ([[X-Ray Crystallography]]).
- **Periodization.** Convolving with a comb makes periodic copies: $g * \text{Ш}_a = \sum_n g(x - na)$. Multiplying by a comb samples. So sampling in one domain periodizes in the other (aliasing).
- The self-transform property is the Poisson summation formula, $\sum_n g(n) = \sum_m G(m)$.

# Questions
> [!question]- Why does sampling a function on a grid of spacing $a$ make its spectrum periodic with period $1/a$?
> Sampling multiplies $g$ by $\sum_n\delta(x - na)$. By the convolution theorem, a product becomes a convolution of the transforms: $G * \frac1a\sum_m\delta(u - m/a) = \frac1a\sum_m G(u - m/a)$, which is periodic with period $1/a$. If $G$ is wider than $1/a$, the copies overlap (aliasing).

[^1]: [Sigworth, Fourier transform notes, p. 4](zotero://open-pdf/library/items/FEUF2XYA?page=4&annotation=8N69K2C5)
