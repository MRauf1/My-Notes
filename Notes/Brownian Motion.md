---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Brownian Motion[^1]
> The random motion of particles in space (the continuum limit of a [[Random Walk]]). In 1D, with diffusion constant $k$, a particle starting at $x$ lies in $(a, b)$ at time $t$ with probability
> $$
> \begin{align}
> P = \int_a^b S(x - y, t)\, dy, \qquad S(x, t) = \frac{1}{\sqrt{4\pi k t}} e^{-x^2/4kt},
> \end{align}
> $$
> where $S$ is the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]]. Hence the probability density $u(x, t)$ of the particle's position satisfies the [[Diffusion Equation]] $u_t = k u_{xx}$, with $u(x, 0) = \phi(x)$ the initial density.

# Properties
- The displacement after time $t$ is distributed $N(0, 2kt)$ ([[Normal Distribution]]), so the typical distance travelled grows like $\sqrt{t}$ ([[Random Walk Mean Squared Displacement]]).
- Standard Brownian motion (variance $t$) corresponds to $k = \tfrac12$, i.e. $u_t = \tfrac12 u_{xx}$.
- An irreversible process: its density evolves by diffusion, which is ill-posed backward in time ([[Diffusion Equation Well-Posedness]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=63&annotation=L44DXV7Z)
