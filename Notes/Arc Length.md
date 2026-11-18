---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Arc Length Formula)[^1]
> If $f'$ is continuous on $[a, b]$, the length of the curve $y = f(x)$, $a \leq x \leq b$, is
> $$
> \begin{align}
> L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx
> \end{align}
> $$
> For $x = g(y)$, $c \leq y \leq d$: $L = \int_c^d \sqrt{1 + [g'(y)]^2}\,dy$.

# Properties
- Defined as the limit of the lengths of inscribed polygons; the [[Mean Value Theorem]] turns each segment length into $\sqrt{1 + f'(x_i^*)^2}\,\Delta x$, a [[Riemann Sum]].
- Arc length function: $s(x) = \int_a^x \sqrt{1 + [f'(t)]^2}\,dt$, so $ds = \sqrt{1 + (dy/dx)^2}\,dx$ ([[Differential (Calculus)]]).[^2]
- The integrand rarely has an elementary antiderivative; exact cases are built so that $1 + f'^2$ is a perfect square. Otherwise use [[Simpson's Rule]].
- For a parametrized curve $\alpha$ in $\mathbb{R}^n$ it becomes $\int_a^b \|\alpha'(t)\|\,dt$: [[Curve Arc Length]] (differential geometry).

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=577)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=579)
