---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Domain of Dependence[^1]
> For the [[Wave Equation]], the domain of dependence (past history) of a point $(\mathbf{x}, t)$, $t > 0$, is the solid backward cone
> $$
> \begin{align}
> \{(\mathbf{y}, s) : 0 \le s \le t,\ |\mathbf{y} - \mathbf{x}| \le c(t - s)\},
> \end{align}
> $$
> bounded by the characteristics through $(\mathbf{x}, t)$. Its base on $t = 0$, the ball $|\mathbf{y} - \mathbf{x}| \le ct$, is the **interval (region) of dependence**: $u(\mathbf{x}, t)$ is determined by the initial data there alone. In 1D it is the triangle over $[x - ct, x + ct]$.

The "inverse" view of causality: instead of asking where a disturbance goes, ask how the number $u(\mathbf{x}, t)$ is synthesized from the initial data.

**Dimension dependence of what is actually used:**
- **1D** ([[D'Alembert's Formula]]): $\phi$ only at the two endpoints $x \pm ct$; $\psi$ on the whole interval $[x - ct, x + ct]$.
- **3D** (Kirchhoff's formula): $\phi$, $\nabla\phi$ and $\psi$ only on the sphere $|\mathbf{y} - \mathbf{x}| = ct$, i.e. only the boundary of the cone ([[Huygens's Principle]]).
- **2D** (Poisson's formula): $\phi$ and $\psi$ on the whole disk $|\mathbf{y} - \mathbf{x}| \le ct$, i.e. the full cone, which is why 2D waves leave a lingering tail.

# Properties
- The backward face of the [[Principle of Causality (Wave Equation)]]; dual to the [[Domain of Influence]].
- If two sets of initial data agree on the region of dependence, the solutions agree at $(\mathbf{x}, t)$.
- In numerical schemes for hyperbolic equations, the numerical domain of dependence must contain the true one (the CFL condition).
- For the [[Diffusion Equation]], $u(x, t)$ depends on $\phi(y)$ for all $y \in \mathbb{R}$, so the domain of dependence is the whole initial line.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=51&annotation=P3C4269S)
