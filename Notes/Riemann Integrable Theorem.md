---
tags: [mathematics, real_analysis]
---

# Definition

> [!abstract] Theorem 1 ([[Riemann Integral]] Theorem)[^1]
> [[Bounded Function]] $f$ is Riemann integrable on $[a, b]$ if there exists $r = \int_a^b f(x) dx$, such that for each $\epsilon > 0$, there exists $\delta > 0$ such that
> $$
> \begin{align}
> mesh(P) < \delta \implies |S - r| < \epsilon
> \end{align}
> $$
> where $S$ is the [[Riemann Sum]] of $f$ associated with a [[Partition]] $P$.

> [!abstract] Theorem 2 (Connection to [[Darboux Integral]])
> [[Bounded Function]] $f$ on $[a, b]$ is Riemann integrable if and only if it is Darboux integrable.

> [!abstract] Corollary 3 (Convergence of Riemann Sums)
> Let $f$ be a [[Bounded Function]] that is Riemann integrable on $[a, b]$. Suppose $(S_n)$ is a [[Sequence]] of Riemann sums, with corresponding [[Partition]] $P_n$ satisfying $\lim_{n \rightarrow \infty} mesh(P_n) = 0$. Then the [[Sequence]] $(S_n)$ converges to $\int_a^b f(x) dx$.
> Remark: if one ignores the end intervals of the partitions, the "almost Riemann sums" still converge to the integral.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=286)