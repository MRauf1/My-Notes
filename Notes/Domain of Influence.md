---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Domain of Influence[^1]
> For the [[Wave Equation]], the domain of influence of a point $(\mathbf{x}_0, t_0)$ is the set of points in space-time that initial data (position, velocity, or both) at $(\mathbf{x}_0, t_0)$ can affect:
> $$
> \begin{align}
> \{(\mathbf{x}, t) : t > t_0,\ |\mathbf{x} - \mathbf{x}_0| \le c(t - t_0)\}.
> \end{align}
> $$
> In 1D this is the sector between the characteristics $x = x_0 \pm c(t - t_0)$. The domain of influence of a set $B$ is the union over its points; for an interval $|x| \le R$ it is the sector $|x| \le R + ct$.

It consists of all points reachable by a signal of speed $\le c$ leaving $\mathbf{x}_0$ at time $t_0$: the inside of the future [[Light Cone]].[^2]

# Properties
- The forward face of the [[Principle of Causality (Wave Equation)]]; dual to the [[Domain of Dependence]].
- In odd dimensions $n \ge 3$ it shrinks to the cone surface $|\mathbf{x} - \mathbf{x}_0| = c(t - t_0)$ ([[Huygens's Principle]]).
- For the [[Diffusion Equation]] the domain of influence of any point is all of space for every $t > 0$, since the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]] is strictly positive everywhere.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=51&annotation=PGNWDPZL)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=53&annotation=YDYFSSW9)
