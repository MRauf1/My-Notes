---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!abstract] Theorem 1 ($m$th [[Moment (Statistics)|Moment]] Existence Theorem)[^1]
> Let $X$ be a [[Random Variable]], $m \in \mathbb{N}$, and $E[X^m]$ exists. Then for all positive integers $k \leq m$, $E[X^k]$ exists.

Proof idea: $|x|^k \leq 1 + |x|^m$ for all $x$ when $k \leq m$, so $E|X|^k \leq 1 + E|X|^m < \infty$.

# Properties
- In particular, a finite [[Variance]] implies that the mean exists, which is the hypothesis used in [[Chebyshev's Inequality]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=94)