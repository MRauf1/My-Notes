---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Comparison Properties of the Integral)[^1]
> For [[Riemann Integral|integrable]] $f, g$ on $[a, b]$ ($a \leq b$):
> 1. If $f(x) \geq 0$ for $a \leq x \leq b$, then $\int_a^b f(x)\,dx \geq 0$.
> 2. If $f(x) \geq g(x)$ for $a \leq x \leq b$, then $\int_a^b f(x)\,dx \geq \int_a^b g(x)\,dx$.
> 3. If $m \leq f(x) \leq M$ for $a \leq x \leq b$, then
> $$
> \begin{align}
> m(b - a) \leq \int_a^b f(x)\,dx \leq M(b - a)
> \end{align}
> $$

# Properties
- Property 1 follows from the [[Riemann Sum|Riemann sums]] being nonnegative; 2 follows from 1 applied to $f - g$ with [[Definite Riemann Integral Basic Properties|linearity]]; 3 follows from 2 with constant bounds.
- Consequence: $\left|\int_a^b f(x)\,dx\right| \leq \int_a^b |f(x)|\,dx$, from $-|f| \leq f \leq |f|$.
- With the [[Extreme Value Theorem]], property 3 gives the bounds $m = \min f$, $M = \max f$ for continuous $f$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=419)
