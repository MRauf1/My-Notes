---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Regrouping of a Series)[^1]
> Let $\sum_{n} a_n$ be a series of complex numbers and let $\{J_l\}_{l \in L}$ be a partition of $\mathbb{N}$ into nonempty sets, with $L$ [[Countable Set|countable]]. The regrouping of $\sum a_n$ along the partition is the iterated series
> $$
> \begin{align}
> \sum_{l \in L} \left( \sum_{n \in J_l} a_n \right),
> \end{align}
> $$
> where each block $J_l$ may be finite or infinite and there may be infinitely many blocks.

> [!abstract] Theorem 1 (Regrouping of Nonnegative Series)[^1]
> Let $p_n \geq 0$ for all $n$, and let $\{J_l\}_{l \in L}$ be any partition of $\mathbb{N}$. Then, in $[0, \infty]$,
> $$
> \begin{align}
> \sum_{n} p_n = \sum_{l \in L} \sum_{n \in J_l} p_n,
> \end{align}
> $$
> where the right side is $+\infty$ if some block sum is $+\infty$.

> [!abstract] Theorem 2 (Associative Law for [[Absolutely Convergent Infinite Series]])[^1]
> Let $\sum_n |a_n| < \infty$ and let $\{J_l\}_{l \in L}$ be any partition of $\mathbb{N}$. Then each block series $\sum_{n \in J_l} a_n$ converges absolutely, $\sum_{l \in L} \left| \sum_{n \in J_l} a_n \right| < \infty$, and
> $$
> \begin{align}
> \sum_{n} a_n = \sum_{l \in L} \sum_{n \in J_l} a_n.
> \end{align}
> $$

Theorem 1 needs no hypothesis: a sum of nonnegative terms is the supremum of its finite partial sums ([[Unordered Sum]]), and a supremum does not depend on how the terms are grouped. Theorem 2 follows by splitting $a_n$ into real and imaginary parts and each of those into positive and negative parts, then applying Theorem 1 to each of the (finitely many, all finite) nonnegative series.

# Properties

> [!abstract] Theorem 3 (Interchange of Summation for Double Series)[^2]
> Let $(a_{ij})_{i, j \geq 1}$ be a double sequence of complex numbers with $\sum_{j=1}^\infty |a_{ij}| = b_i$ for each $i$ and $\sum_i b_i$ convergent. Then
> $$
> \begin{align}
> \sum_{i=1}^\infty \sum_{j=1}^\infty a_{ij} = \sum_{j=1}^\infty \sum_{i=1}^\infty a_{ij}.
> \end{align}
> $$

- Theorem 3 is Theorem 2 applied twice on $\mathbb{N} \times \mathbb{N}$ (enumerated by a bijection with $\mathbb{N}$): once to the partition into rows, once to the partition into columns. By Theorem 1 the hypothesis is $\sum_{i, j} |a_{ij}| = \sum_i b_i < \infty$.
- With singleton blocks, a regrouping is a rearrangement, so Theorem 2 contains the rearrangement invariance of absolutely convergent series ([[Rearrangement (Series)]], Theorem 2).
- Grouping into *finite consecutive* blocks (inserting parentheses) preserves the sum of any convergent series, absolutely convergent or not: the partial sums of the grouped series are a subsequence of the original partial sums.
- Theorem 1 is the [[Counting Measure|counting-measure]] case of Tonelli's theorem, and Theorems 2–3 are the counting-measure case of [[Fubini's Theorem]].
- Grouping by the fibres $\{x : g(x) = y\}$ is the key step in proving $E[g(X)] = \sum_x g(x)\, p_X(x)$ for a discrete random variable ([[Expectation]], Theorem 1).

# Questions

> [!question]- Theorem 2 needs $\sum |a_n| < \infty$ but Theorem 1 needs nothing. Why does the hypothesis fail for a conditionally convergent series?
> For $p_n \geq 0$, both sides of Theorem 1 equal $\sup_{F \text{ finite}} \sum_{n \in F} p_n$, so the grouping cannot matter. For signed terms an infinite block can already diverge. The alternating harmonic series $\sum_{n \geq 1} (-1)^{n+1}/n$ converges, but along the partition into odd and even indices the block sum $\sum_{k \geq 1} \frac{1}{2k-1}$ is $+\infty$, so the regrouping is undefined ($\infty - \infty$). Only finite consecutive blocks are safe without absolute convergence.

> [!question]- How do you reduce Theorem 2 to Theorem 1?
> Write $a_n = (u_n^+ - u_n^-) + i\,(v_n^+ - v_n^-)$ with $u_n^\pm, v_n^\pm \geq 0$ and each $\leq |a_n|$. Each of the four nonnegative series is finite, and Theorem 1 regroups each one along $\{J_l\}$. Because every quantity involved is finite, the four identities can be combined linearly, which gives the identity for $a_n$. Absolute convergence of each block and of the outer sum follows from Theorem 1 applied to $|a_n|$.

> [!question]- Connection: what measure-theoretic statement is Theorem 2?
> Define $\nu(A) = \sum_{n \in A} a_n$ for $A \subseteq \mathbb{N}$. When $\sum |a_n| < \infty$, $\nu$ is a complex measure (the complex-valued analogue of a [[Measure (Measure Theory)|measure]]) on $2^{\mathbb{N}}$: it has density $a_n$ with respect to [[Counting Measure|counting measure]]. Theorem 2 is exactly countable additivity, $\nu\left(\bigsqcup_l J_l\right) = \sum_l \nu(J_l)$. Dictionary: partition $\leftrightarrow$ countable disjoint union, absolute convergence $\leftrightarrow$ finite total variation, Theorem 1 $\leftrightarrow$ countable additivity of a positive measure. Where it breaks: a conditionally convergent series does not define a complex measure, because $\nu(\text{odd indices})$ is undefined. This is why only absolutely convergent series behave like integrals.

[^1]: [Some Simplifications in the Presentations of Complex Power Series and Unordered Sums, Thm 5.1 and Cor. 5.2](https://arxiv.org/abs/1207.1472)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=184)
