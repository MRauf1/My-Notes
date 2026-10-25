---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Dini's Theorem)[^1]
> Suppose $K$ is [[Compact Set|compact]], and
> (a) $\{f_n\}$ is a [[Sequence of Function|sequence]] of [[Continuous Function|continuous functions]] on $K$,
> (b) $\{f_n\}$ [[Sequence of Function Pointwise Convergence|converges pointwise]] to a continuous function $f$ on $K$,
> (c) $f_n(x) \geq f_{n+1}(x)$ for all $x \in K$, $n = 1, 2, 3, \dots$
> Then $f_n \rightarrow f$ [[Sequence of Function Uniform Convergence|uniformly]] on $K$.

The converse of the [[Uniform Limit of Continuous Functions Theorem]] is false in general: continuous functions may converge pointwise to a continuous function without converging uniformly. Dini's theorem gives the case (monotone convergence on a compact set) in which the converse can be asserted.[^2]

By symmetry, the theorem also holds for increasing sequences $f_n(x) \leq f_{n+1}(x)$.

# Properties
- Compactness of $K$, continuity of $f$, and monotonicity are all necessary.
- [[Uniform Limit of Continuous Functions Theorem]]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=159&annotation=U2ZL7RD5)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=159&annotation=RXICR9DG)
