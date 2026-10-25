---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Helly's Selection Theorem)[^1]
> Let $\{f_n\}$ be a [[Sequence of Function|sequence]] of [[Monotonic Function|monotonically increasing]] functions on $\mathbb{R}$ with $0 \leq f_n(x) \leq 1$ for all $x$ and all $n$. Then
> (a) there is a function $f$ and a [[Subsequence]] $\{f_{n_k}\}$ such that $f(x) = \lim_{k \rightarrow \infty} f_{n_k}(x)$ for every $x \in \mathbb{R}$ ([[Sequence of Function Pointwise Convergence|pointwise convergence]]);
> (b) if, moreover, $f$ is [[Continuous Function|continuous]], then $f_{n_k} \rightarrow f$ [[Sequence of Function Uniform Convergence|uniformly]] on [[Compact Set|compact sets]].

Monotonicity substitutes for [[Equicontinuity]]: a diagonal subsequence converging on the rationals ([[Pointwise Bounded Sequence Countable Set Subsequence Theorem]]) automatically converges at every continuity point of the limit, and a monotone limit has at most [[Countable Set|countably]] many discontinuities.

# Properties
- In probability, it gives tightness/weak-convergence compactness for sequences of cumulative distribution functions.
- Compare [[Arzelà-Ascoli Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=176&annotation=N43IKDF9)
