---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Sequence of Function Uniform Convergence]] of [[Riemann Integral]] Theorem)[^1]
> Let $(f_n)$ be [[Sequence of Function|sequence of]] [[Continuous Function]] on $[a, b]$, and suppose $f_n \rightarrow f$ uniformly on $[a, b]$. Then
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} \int_a^b f_n(x) dx = \int_a^b f(x) dx
> \end{align}
> $$

> [!abstract] Theorem 2 ([[Riemann-Stieltjes Integral]] Version)[^2]
> Let $\alpha$ be [[Monotonic Function|monotonically increasing]] on $[a, b]$. Suppose $f_n \in \mathscr{R}(\alpha)$ on $[a, b]$ for $n = 1, 2, 3, \dots$, and suppose $f_n \rightarrow f$ uniformly on $[a, b]$. Then $f \in \mathscr{R}(\alpha)$ on $[a, b]$, and
> $$
> \begin{align}
> \int_a^b f \, d\alpha = \lim_{n \rightarrow \infty} \int_a^b f_n \, d\alpha
> \end{align}
> $$
> The existence of the limit is part of the conclusion.

> [!abstract] Corollary 3 (Term-by-Term Integration)[^3]
> If $f_n \in \mathscr{R}(\alpha)$ on $[a, b]$ and if
> $$
> \begin{align}
> f(x) = \sum_{n=1}^{\infty} f_n(x) \quad (a \leq x \leq b)
> \end{align}
> $$
> the series converging uniformly on $[a, b]$, then
> $$
> \begin{align}
> \int_a^b f \, d\alpha = \sum_{n=1}^{\infty} \int_a^b f_n \, d\alpha
> \end{align}
> $$
> In other words, the series may be integrated term by term.

Theorem 1 is the special case $\alpha(x) = x$ with continuous $f_n$.

# Properties
- [[Interchangeability of Limit and Integral Theorem]]
- [[Integral of Power Series]]
- Uniform convergence can be weakened to domination: [[Dominated Convergence Theorem]].
- Used to give a short proof of the [[Uniform Limit of Derivatives Theorem]] when the $f_n'$ are continuous.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=211)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=160&annotation=9U5XQIQB)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=161&annotation=NHD9Q9YL)
