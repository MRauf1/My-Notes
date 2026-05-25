---
tags: mathematics, real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Infinite Series]] [[Riemann Integral]] Test)[^1]
> Suppose that $f(x)$ is a [[Continuous Function]], positive, and [[Decreasing Function]] on the [[Interval Notation|interval]] $[k, \infty)$ and that $f(n) = a_n$, then
> 1) If $\int_{k}^{\infty} f(x) dx$ converges, then so does $\sum_{n=k}^{\infty} a_n$
> 2) If $\int_{k}^{\infty} f(x) dx$ diverges, then so does $\sum_{n=k}^{\infty} a_n$

> [!abstract] Theorem 2 ([[Error]] Bounding)[^2]
> Take $f$ from above, and let $\sum a_n$ be convergent. If $R_n = s - s_n$ ($s$ is the limit of series, $s_n$ is the sequence of partial sums), then
> $$
> \begin{align}
> \int_{n+1}^{\infty} f(x)dx \leq R_n \leq \int_n^{\infty} f(x)dx
> \end{align}
> $$

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=118)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=755)