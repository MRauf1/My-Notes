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

# Properties
- **Discrete version** (unit step): $u[t] = 0$ for $t < 0$ and $1$ otherwise. It appears in the impulse responses of [[Causal Filter|causal]] [[Infinite Impulse Response Filter|IIR filters]], e.g. $h[t] = \alpha^t u[t]$.[^2]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=119)
[^2]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
