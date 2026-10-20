---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Heaviside [[Function]])[^1]
> $$
> \begin{align}
> H(t) = \begin{cases}0 & t < 0 \\ 1 & t \geq 0\end{cases}
> \end{align}
> $$

> [!info] Definition 2 (Unit Step Function, Rudin's Convention)[^3]
> $$
> \begin{align}
> I(x) = \begin{cases}0 & x \leq 0 \\ 1 & x > 0\end{cases}
> \end{align}
> $$

$I$ differs from $H$ only at $0$ ($I$ is left-continuous, $H$ right-continuous). Used as an integrator, $\int_a^b f\,dI(x - s) = f(s)$ for $f$ continuous at $s \in (a, b)$ ([[Riemann-Stieltjes Integral with Step Function Integrator Theorem]]).

# Properties
- **Discrete version** (unit step): $u[t] = 0$ for $t < 0$ and $1$ otherwise. It appears in the impulse responses of [[Causal Filter|causal]] [[Infinite Impulse Response Filter|IIR filters]], e.g. $h[t] = \alpha^t u[t]$.[^2]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=119)
[^2]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=138&annotation=YRTZFHNH)
