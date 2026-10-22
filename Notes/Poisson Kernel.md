---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Poisson Kernel[^1]
> For the disk of radius $a$,
> $$
> \begin{align}
> P(r, \theta) = \frac{a^2 - r^2}{a^2 - 2ar\cos\theta + r^2} = 1 + 2\sum_{n=1}^\infty \left(\frac{r}{a}\right)^n \cos n\theta, \qquad 0 \le r < a,
> \end{align}
> $$
> so that [[Poisson's Formula]] reads $u(r, \theta) = \int_0^{2\pi} P(r, \theta - \phi)\, h(\phi)\, \frac{d\phi}{2\pi}$.

# Properties
- **Positive:** $P(r, \theta) > 0$ for $r < a$, since $a^2 - 2ar\cos\theta + r^2 \ge (a - r)^2 > 0$.[^1]
- **Unit mass:** $\int_0^{2\pi} P(r, \theta)\, \frac{d\theta}{2\pi} = 1$, since $\int_0^{2\pi}\cos n\theta\, d\theta = 0$ for $n \ge 1$.[^2]
- **Harmonic:** $P$ is harmonic inside the circle, since each $(r/a)^n\cos n\theta$ is.[^2]
- **Concentration:** as $r \to a^-$, $P(r, \theta) \to 0$ uniformly on $\delta \le |\theta| \le \pi$, so $P(r, \cdot)$ is an approximate identity tending to the [[Dirac Delta Function]]; this is why $u \to h$ at the boundary.[^3]
- Elliptic analogue of the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]], with $r/a$ playing the role of the damping $e^{-kt}$ per frequency; contrast with the [[Dirichlet Kernel]], which lacks positivity.[^3]
- Its Fourier coefficients $(r/a)^{|n|}$ are the Abel summation weights of [[Abel's Theorem (Power Series Boundary Convergence)]].[^3]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=182&annotation=SFMWUDLF)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=183&annotation=KZBQLW6T)
[^3]: Added from general knowledge.
