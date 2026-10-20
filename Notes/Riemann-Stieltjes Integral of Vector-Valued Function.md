---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Riemann-Stieltjes Integral of [[Vector-Valued Function]])[^1]
> Let $f_1, \dots, f_k$ be real functions on $[a, b]$ and $\mathbf{f} = (f_1, \dots, f_k)$ the corresponding mapping of $[a, b]$ into $\mathbb{R}^k$. If $\alpha$ increases monotonically on $[a, b]$, $\mathbf{f} \in \mathscr{R}(\alpha)$ means $f_j \in \mathscr{R}(\alpha)$ for $j = 1, \dots, k$. In that case,
> $$
> \begin{align}
> \int_a^b \mathbf{f} \, d\alpha = \left( \int_a^b f_1 \, d\alpha, \dots, \int_a^b f_k \, d\alpha \right)
> \end{align}
> $$
> i.e. the point of $\mathbb{R}^k$ whose $j$th coordinate is the [[Riemann-Stieltjes Integral]] $\int f_j \, d\alpha$.

Linearity, interval additivity, and linearity in $\alpha$ ([[Riemann-Stieltjes Integral Basic Properties]]), [[Riemann-Stieltjes Integral with Differentiable Integrator Theorem]], and both parts of the [[Fundamental Theorem of Calculus]] carry over by applying the scalar results coordinatewise.

> [!abstract] Theorem 2 ([[Fundamental Theorem of Calculus]])[^2]
> If $\mathbf{f}$ and $\mathbf{F}$ map $[a, b]$ into $\mathbb{R}^k$, $\mathbf{f} \in \mathscr{R}$ on $[a, b]$, and $\mathbf{F}' = \mathbf{f}$, then
> $$
> \begin{align}
> \int_a^b \mathbf{f}(t) \, dt = \mathbf{F}(b) - \mathbf{F}(a)
> \end{align}
> $$

> [!abstract] Theorem 3 ([[Triangle Inequality]])[^3]
> If $\mathbf{f}$ maps $[a, b]$ into $\mathbb{R}^k$ and $\mathbf{f} \in \mathscr{R}(\alpha)$ for some monotonically increasing $\alpha$ on $[a, b]$, then $|\mathbf{f}| \in \mathscr{R}(\alpha)$ and
> $$
> \begin{align}
> \left| \int_a^b \mathbf{f} \, d\alpha \right| \leq \int_a^b |\mathbf{f}| \, d\alpha
> \end{align}
> $$

Unlike the coordinatewise results, Theorem 3 does not follow by applying the scalar case to each coordinate; it needs a new argument (integrability of $|\mathbf{f}| = (f_1^2 + \dots + f_k^2)^{1/2}$ via [[Functions that are Riemann-Stieltjes Integrable Theorem|composition with a continuous function]], then the [[Cauchy-Schwarz Inequality]] with $\mathbf{y} = \int \mathbf{f}\,d\alpha$).

# Properties
- Scalar version of Theorem 3: [[Riemann Integral Triangle Inequality]].
- Used to compute the length of a $C^1$ curve, $\int_a^b |\gamma'(t)|\,dt$ ([[Rectifiable Curve]]).
- Parallels [[Derivative of Vector-Valued Function]] (also defined coordinatewise).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=144&annotation=4RKFCXTF)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=144&annotation=ESF5Z2BK)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=144&annotation=584LYVTG)
