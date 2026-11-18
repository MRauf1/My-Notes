---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Midpoint Rule)[^1]
> With $\Delta x = \frac{b - a}{n}$ and $\bar x_i = \frac{1}{2}(x_{i-1} + x_i)$ the midpoint of $[x_{i-1}, x_i]$,
> $$
> \begin{align}
> \int_a^b f(x)\,dx \approx M_n = \Delta x\,\big[f(\bar x_1) + \dots + f(\bar x_n)\big]
> \end{align}
> $$

# Properties
- A [[Riemann Sum]] with midpoints as sample points.
- Error bound: if $|f''(x)| \leq K$ on $[a, b]$, then $|E_M| \leq \frac{K(b - a)^3}{24 n^2}$.[^2]
- About half the error of the [[Trapezoidal Rule]] and of opposite sign; for concave-up $f$, $M_n \leq \int_a^b f \leq T_n$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=547)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=550)
