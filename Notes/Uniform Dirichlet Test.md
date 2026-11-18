---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Uniform Dirichlet Test)[^1]
> Suppose $\{f_n\}$, $\{g_n\}$ are defined on $E$, and
> (a) $\sum f_n$ has [[Sequence of Function Uniformly Bounded|uniformly bounded]] partial sums;
> (b) $g_n \rightarrow 0$ [[Sequence of Function Uniform Convergence|uniformly]] on $E$;
> (c) $g_1(x) \geq g_2(x) \geq g_3(x) \geq \cdots$ for every $x \in E$.
> Then $\sum f_n g_n$ converges uniformly on $E$.

# Properties
- The uniform version of the [[Dirichlet Test]]: taking every $f_n$, $g_n$ constant on $E$ recovers it.
- Proved like the [[Dirichlet Test]]: [[Summation by Parts]] bounds $\left|\sum_{k=m}^{n} f_k g_k\right| \le 2M g_m(x) \le 2M \sup_E g_m$, where $M$ bounds the partial sums, and the [[Cauchy Criterion for Uniform Convergence Theorem]] finishes.
- Covers series that do not converge absolutely, where the [[Weierstrass M-Test]] fails.

# Questions
> [!question]- Why does the uniform test need $g_n \to 0$ *uniformly*, when the pointwise [[Dirichlet Test]] only needs $g_n(x) \to 0$ at each $x$?
> The summation-by-parts bound $\left|\sum_{k=m}^{n} f_k g_k\right| \le 2M\, g_m(x)$ is uniform in $x$ only if $\sup_E g_m \to 0$. With pointwise convergence alone, the tail estimate depends on $x$, so it yields only pointwise convergence of $\sum f_n g_n$, not uniform convergence.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=176&annotation=K7CBHZEQ)
