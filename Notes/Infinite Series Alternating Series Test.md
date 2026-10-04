---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Infinite Series]] [[Alternating Series]] Test)[^1]
> If $a_1 \geq \dots \geq a_n \geq \dots \geq 0$ and $\lim a_n = 0$, then the [[Alternating Series]] $\sum (-1)^n a_n$ converges. Moreover, the partial sums $s_n = \sum_{k=1}^n (-1)^k a_k$ satisfies $|s_n - s| \leq a_n$ for all $n$, where $s = \lim_{n \rightarrow \infty} s_n$.

This is a special case of the [[Dirichlet Test]], taking the oscillating factor to be $(-1)^n$ (whose partial sums are bounded by $1$) and the decreasing-to-zero factor to be $a_n$. This test (also called the Leibniz test) is due to Leibniz.[^2]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=120)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=80)