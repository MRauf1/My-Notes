---
tags: mathematics, real_analysis
---

# Definition

> [!abstract] Theorem 1 (Taylor's Theorem)[^1]
> Let $f$ be defined on $(a, b)$ where $a < c < b$ (we allow endpoints to be infinities). Suppose the [[Nth Derivative]] $f^{(n)}$ exists on $(a, b)$. Then for each $x \neq c$ in $(a, b)$, there is some $y$ between $c$ and $x$ such that
> $$
> \begin{align}
> R_n(x) = \frac{f^{(n)}(y)}{n!} (x - c)^n
> \end{align}
> $$
> where $R_n(x)$ is the remainder function of the [[Taylor Series]].

> [!abstract] Corollary 2 (Corollary)[^1]
> Let $f$ be defined on $(a, b)$ where $a < c < b$. If all the [[Derivative]] $f^{(n)}$ exist on $(a, b)$ and are bounded by a single constant $C$, then 
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} R_n(x) = 0, \forall x \in (a, b)
> \end{align}
> $$

> [!abstract] Theorem 3 (Taylor's Theorem Part 2)[^1]
> Let $f$ be defined on $(a, b)$ where $a < c < b$ and suppose [[Nth Derivative]] $f^{(n)}$ exists and is [[Continuous Function]] on $(a, b)$. Then, for $x \in (a, b)$
> $$
> \begin{align}
> R_n(x) = \int_c^x \frac{(x - t)^{n - 1}}{(n - 1)!} f^{(n)}(t) dt
> \end{align}
> $$

> [!abstract] Corollary 4 (Cauchy's Form of Remainder)[^1]
> If $f$ is as in Theorem 3, then for each $x \in (a, b)$ different from $c$, there is some $y$ between $c$ and $x$ such that
> $$
> \begin{align}
> R_n(x) = (x - c) \cdot \frac{(x - y)^{n - 1}}{(n - 1)!} f^{(n)}(y)
> \end{align}
> $$

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=259)