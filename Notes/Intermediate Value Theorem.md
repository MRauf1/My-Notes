---
tags: mathematics, real_analysis
---

# Definition

> [!abstract] Theorem 1 (Intermediate Value Theorem)[^1]
> For a [[Continuous Function]] $f$ on the [[Interval Notation|interval]] $[a, b]$ and number $N$ such that $f(a) \leq N \leq f(b)$ with $f(a) \neq f(b)$, then there exists a number $c \in (a, b)$ such that $f(c) = N$.

Continuous function takes on every intermediate value.

If $f(a)$ and $f(b)$ have opposite signs, then the function has at least one zero between $x = a$ and $x = b$.

> [!abstract] Corollary 2 ([[Interval Notation]])
> If $f$ is [[Continuous Function]] on an interval $I$, then the [[Set]] $f(I)$ is also an interval or a single point.

> [!abstract] Theorem 3 (Intermediate Value Theorem for [[Derivative]])[^2]
> Let $f$ be [[Differentiable Function]] on $(a, b)$. If $a < x_1 < x_2 < b$ and if $c$ lies between $f'(x_1)$ and $f'(x_2)$, there exists at least one $x$ in $(x_1, x_2)$ such that $f'(x) = c$.

> [!abstract] Theorem 4 (Intermediate Value Theorem for [[Integral]])[^3]
> If $f$ is [[Continuous Function]] on $[a, b]$, then for at least one $x \in (a, b)$, we have
> $$
> \begin{align}
> f(x) = \frac{1}{b - a} \int_a^b f
> \end{align}
> $$

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=253)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=245)
[^3]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=296)