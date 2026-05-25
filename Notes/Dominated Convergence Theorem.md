---
tags: mathematics, real_analysis
---

# Definition

> [!abstract] Theorem 1 (Dominated Convergence Theorem)[^1]
> Suppose $(f_n)$ is a [[Sequence]] of [[Riemann Integrable Function]] on $[a, b]$ and $f_n$ [[Sequence of Function Pointwise Convergence|converge pointwise]] to $f$ where $f$ is [[Riemann Integrable Function]] on $[a, b]$. If there exists $M > 0$ such that $|f_n(x)| \leq M$ for all $n$ and all $x \in [a, b]$, then
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} \int_a^b f_n(x) dx = \int_a^b \lim_{n \rightarrow \infty} f_n(x) dx
> \end{align}
> $$

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=297)