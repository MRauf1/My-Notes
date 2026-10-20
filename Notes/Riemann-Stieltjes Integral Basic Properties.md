---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Basic Properties of the [[Riemann-Stieltjes Integral]])[^1]
> Let $\alpha, \alpha_1, \alpha_2$ be monotonically increasing on $[a, b]$.
> 1) **Linearity in $f$**: if $f_1, f_2 \in \mathscr{R}(\alpha)$, then $f_1 + f_2 \in \mathscr{R}(\alpha)$ and $cf \in \mathscr{R}(\alpha)$ for every constant $c$, with
> $$
> \begin{align}
> \int_a^b (f_1 + f_2) \, d\alpha = \int_a^b f_1 \, d\alpha + \int_a^b f_2 \, d\alpha, \qquad \int_a^b cf \, d\alpha = c \int_a^b f \, d\alpha
> \end{align}
> $$
> 2) **Monotonicity**: if $f_1(x) \leq f_2(x)$ on $[a, b]$, then $\int_a^b f_1 \, d\alpha \leq \int_a^b f_2 \, d\alpha$.
> 3) **Interval additivity**: if $f \in \mathscr{R}(\alpha)$ on $[a, b]$ and $a < c < b$, then $f \in \mathscr{R}(\alpha)$ on $[a, c]$ and on $[c, b]$, and
> $$
> \begin{align}
> \int_a^c f \, d\alpha + \int_c^b f \, d\alpha = \int_a^b f \, d\alpha
> \end{align}
> $$
> 4) **Bound**: if $f \in \mathscr{R}(\alpha)$ and $|f(x)| \leq M$ on $[a, b]$, then $\left| \int_a^b f \, d\alpha \right| \leq M[\alpha(b) - \alpha(a)]$.
> 5) **Linearity in $\alpha$**: if $f \in \mathscr{R}(\alpha_1)$ and $f \in \mathscr{R}(\alpha_2)$, then $f \in \mathscr{R}(\alpha_1 + \alpha_2)$ and
> $$
> \begin{align}
> \int_a^b f \, d(\alpha_1 + \alpha_2) = \int_a^b f \, d\alpha_1 + \int_a^b f \, d\alpha_2
> \end{align}
> $$
> and if $c > 0$, then $f \in \mathscr{R}(c\alpha)$ and $\int_a^b f \, d(c\alpha) = c \int_a^b f \, d\alpha$.

The integral is thus bilinear in the pair $(f, \alpha)$. For interval additivity, the point is that (by passing to [[Refinement of Partition|refinements]]) one may restrict to partitions containing $c$.[^2]

# Properties
- Special case $\alpha(x) = x$: [[Definite Riemann Integral Basic Properties]].
- Parts 1, 3, and 5 extend coordinatewise to the [[Riemann-Stieltjes Integral of Vector-Valued Function]].
- Products and absolute values: [[Functions that are Riemann-Stieltjes Integrable Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=137&annotation=9UFKQN2Q)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=138&annotation=W4VRVI2F)
