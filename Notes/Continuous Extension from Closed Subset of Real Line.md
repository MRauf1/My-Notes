---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Continuous Extension from a [[Closed Set]] of $\mathbb{R}$)[^1]
> If $f$ is a real [[Continuous Function]] defined on a [[Closed Set]] $E \subseteq \mathbb{R}$, then there exist continuous real functions $g$ on $\mathbb{R}$ such that $g(x) = f(x)$ for all $x \in E$. Such $g$ are called continuous [[Extension of Function|extensions]] of $f$ from $E$ to $\mathbb{R}$.
> The result is false if $E$ is not closed, and it extends to [[Real Vector-Valued Function|vector-valued]] functions $f: E \rightarrow \mathbb{R}^k$.

# Properties
- Proof idea: $E^c$ is open, so it is a countable disjoint union of open intervals ([[Open Subset of Real Line Theorem]]). On each bounded interval $(a, b)$, whose endpoints lie in $E$, let $g$ be linear from $f(a)$ to $f(b)$; on an unbounded one, let $g$ be constant.
- The vector-valued version follows by extending each component ([[Continuous Function Component Theorem]]).
- Closedness is necessary: on a non-closed set, a continuous function can blow up or oscillate near a [[Limit Point]] outside the set (e.g. $1/x$ or $\sin(1/x)$ on $(0, 1]$).
- The special case $X = \mathbb{R}$ of the [[Tietze Extension Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=108)
