---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Damped Wave Equation[^1]
> The [[Wave Equation]] with a resistance term proportional to the velocity $u_t$:
> $$
> \begin{align}
> u_{tt} - c^2 \Delta u + r u_t = 0, \qquad r > 0.
> \end{align}
> $$

Models a vibrating medium subject to significant air resistance (friction).

# Properties
- Linear, homogeneous, [[Hyperbolic Partial Differential Equation|hyperbolic]] (the first-order term does not affect the type).
- The term $r u_t$ dissipates energy, so oscillations decay in time.
- Special case of the telegraph equation $u_{tt} + (\alpha + \beta) u_t + \alpha\beta u = c^2 u_{xx}$ (with $\alpha\beta = 0$).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=25&annotation=BCC9SXSP)
