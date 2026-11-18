---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Trapezoidal Rule)[^1]
> With $\Delta x = \frac{b - a}{n}$ and $x_i = a + i\Delta x$,
> $$
> \begin{align}
> \int_a^b f(x)\,dx \approx T_n = \frac{\Delta x}{2}\big[f(x_0) + 2f(x_1) + \dots + 2f(x_{n-1}) + f(x_n)\big]
> \end{align}
> $$

# Properties
- $T_n = \frac{1}{2}(L_n + R_n)$, the average of the left and right [[Riemann Sum|Riemann sums]]; geometrically it sums trapezoid areas.
- Error bound: if $|f''(x)| \leq K$ on $[a, b]$, then $|E_T| \leq \frac{K(b - a)^3}{12 n^2}$.[^2]
- Compare [[Midpoint Rule]]; Simpson's rule $S_{2n} = \frac{1}{3}T_n + \frac{2}{3}M_n$ ([[Simpson's Rule]]).

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=548)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=550)
