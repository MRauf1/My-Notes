---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Rearrangement of a Series)[^1]
> Let $\{k_n\}_{n=1}^\infty$ be a sequence in which every positive integer appears exactly once (i.e. a bijection $k: \mathbb{N} \to \mathbb{N}$). Given a series $\sum_{n=1}^\infty a_n$, put $a_n' = a_{k_n}$. The series $\sum_{n=1}^\infty a_n'$ is called a rearrangement of $\sum a_n$.

In general, the sequence of partial sums of a rearrangement $\sum a_n'$ is an entirely different sequence from that of $\sum a_n$, so a rearrangement need not converge to the same sum — or even converge at all.

> [!abstract] Theorem 2 (Absolutely Convergent Series — Rearrangement Invariance)[^2]
> If $\sum a_n$ is a series of complex numbers that converges [[Absolutely Convergent Infinite Series|absolutely]], then every rearrangement of $\sum a_n$ converges, and all of them converge to the same sum.

# Properties
- [[Riemann Series Theorem]]: by contrast, a conditionally (non-absolutely) convergent series of real numbers can be rearranged to converge to any prescribed value, or to diverge.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=85)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=87)
