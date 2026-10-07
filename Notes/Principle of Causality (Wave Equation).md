---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Principle of Causality (Wave Equation)[^1]
> For the [[Wave Equation]], no part of a solution travels faster than the wave speed $c$. Initial data at a point $\mathbf{x}_0$ can affect $u(\mathbf{x}, t)$ only where $|\mathbf{x} - \mathbf{x}_0| \le ct$, and $u(\mathbf{x}, t)$ is determined by the initial data on the ball $|\mathbf{y} - \mathbf{x}| \le ct$ alone. In 1D:
> $$
> \begin{align}
> \phi = \psi = 0 \text{ for } |x| > R \implies u(x, t) = 0 \text{ for } |x| > R + ct.
> \end{align}
> $$

Causality has two dual faces:
- **Forward**: what a point can affect, its [[Domain of Influence]], a cone opening upward.
- **Backward**: what a point depends on, its [[Domain of Dependence]] (past history), a cone opening downward.

Both are bounded by the characteristics through the point: the lines $x \pm ct = \text{const}$ in 1D, and the characteristic cone $|\mathbf{x} - \mathbf{x}_0| = c|t - t_0|$ in $n$-D.

**Physical meaning.** Each component of the electric and magnetic fields satisfies the 3D wave equation with $c$ the speed of light, so causality says no signal can outrun light: it is the cornerstone of [[Special Relativity]], and the characteristic cone is the [[Light Cone]].[^2]

# Properties
- In 1D, the initial position travels at exactly speed $c$, while the initial velocity contributes a wave that spreads at every speed $\le c$, so part of the wave lags behind ([[D'Alembert's Formula]]).
- In odd dimensions $n \ge 3$, causality sharpens to [[Huygens's Principle]]: signals travel at exactly $c$, never slower.
- Can be derived from the [[Wave Equation Energy Conservation|energy]] by integrating the energy density over shrinking balls (energy cannot flow into the cone from outside).
- Holds for all [[Hyperbolic Partial Differential Equation|hyperbolic equations]] (finite speed of propagation) and fails for the [[Diffusion Equation]], whose speed of propagation is infinite ([[Wave and Diffusion Equation Comparison]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=51&annotation=BPYUW8YS); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=51&annotation=PGNWDPZL)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=52&annotation=QLZHHF54); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=53&annotation=YDYFSSW9)
