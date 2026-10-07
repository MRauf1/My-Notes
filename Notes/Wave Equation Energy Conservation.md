---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Wave Equation Energy Conservation[^1][^2]
> For an infinite string $\rho u_{tt} = T u_{xx}$ (with $u_t, u_x \to 0$ as $|x| \to \infty$), the energy
> $$
> \begin{align}
> E = \frac{1}{2}\int_{-\infty}^{\infty} \left(\rho u_t^2 + T u_x^2\right) dx
> \end{align}
> $$
> is constant in $t$. In $\mathbb{R}^n$, for $\rho u_{tt} = T \Delta u$,
> $$
> \begin{align}
> E = \frac{1}{2}\int_{\mathbb{R}^n} \left(\rho u_t^2 + T |\nabla u|^2\right) d\mathbf{x}
> \end{align}
> $$
> is conserved.

The first term is the [[Kinetic Energy]] and the second the [[Potential Energy]] (stretching); mathematically only the total matters.[^3] The wave never loses anything: energy just sloshes between motion and stretching and moves around in space. This is the opposite of diffusion, which dissipates ([[Wave and Diffusion Equation Comparison]]).

# Properties
- Proof: multiply the equation by $u_t$ and integrate; $\rho u_t u_{tt} = \partial_t(\tfrac12\rho u_t^2)$ and $T u_t u_{xx} = \partial_x(T u_t u_x) - \partial_t(\tfrac12 T u_x^2)$, and the flux term vanishes at infinity.
- $E \ge 0$, and a constant rescaling of $E$ does not affect conservation.
- Implies uniqueness: the difference of two solutions with the same data has $E \equiv 0$, hence is constant, hence zero.
- Can be used to derive the [[Principle of Causality (Wave Equation)]] by tracking the energy inside shrinking balls.
- In $n \ge 2$, total energy is conserved yet the amplitude decays (like $t^{-(n-1)/2}$) because the energy spreads over an expanding wavefront.
- The mathematical counterpart of physical [[Conservation of Energy]]; with damping ([[Damped Wave Equation]]) $E$ decreases.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=52&annotation=6JPAFPZN)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=52&annotation=YASVIB7G)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=52&annotation=WC6QZAT8)
