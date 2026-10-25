---
tags:
  - mathematics
  - complex_analysis
---

# Definition

> [!info] Definition 1 (Dirichlet Test)[^1]
> For an [[Infinite Series]] $\sum_{n = 0}^{\infty} a_n b_n$, assume that the partial sums of the [[Infinite Series]] $\sum_{n=0}^{\infty} a_n$ is [[Bounded Sequence]]. Also assume that $b_1 \geq b_2 \geq \dots \geq b_n \geq \dots \geq 0$ and $\lim_{n \rightarrow \infty} b_n = 0$. Then the [[Infinite Series]] converges (but not necessarily [[Absolutely Convergent Infinite Series]]).

Proved via [[Summation by Parts]].

> [!abstract] Theorem 2 (Uniform Dirichlet Test)[^2]
> Suppose $\{f_n\}$, $\{g_n\}$ are defined on $E$, and
> (a) $\sum f_n$ has [[Sequence of Function Uniformly Bounded|uniformly bounded]] partial sums;
> (b) $g_n \rightarrow 0$ [[Sequence of Function Uniform Convergence|uniformly]] on $E$;
> (c) $g_1(x) \geq g_2(x) \geq g_3(x) \geq \cdots$ for every $x \in E$.
> Then $\sum f_n g_n$ converges uniformly on $E$.

# Properties
- [[Summation by Parts]]
- [[Infinite Series Alternating Series Test]] is a special case, taking $a_n = (-1)^n$.
- [[Abel's Theorem (Power Series Boundary Convergence)]] is a consequence, taking $a_n = z^n$ for $|z|=1$.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=80)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=176&annotation=K7CBHZEQ)
