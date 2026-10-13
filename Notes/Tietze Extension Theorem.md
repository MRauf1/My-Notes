---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Continuous Extension from a [[Closed Set]] of $\mathbb{R}$)[^1]
> If $f$ is a real [[Continuous Function]] defined on a [[Closed Set]] $E \subseteq \mathbb{R}$, then there exist continuous real functions $g$ on $\mathbb{R}$ such that $g(x) = f(x)$ for all $x \in E$. Such $g$ are called continuous [[Extension of Function|extensions]] of $f$ from $E$ to $\mathbb{R}$.
> The result is false if $E$ is not closed, and it extends to [[Real Vector-Valued Function|vector-valued]] functions $f: E \rightarrow \mathbb{R}^k$.

> [!abstract] Theorem 2 (Tietze Extension Theorem)[^2]
> Let $X$ be a [[Metric Space]] (more generally, a [[Normal Space]]), $A \subseteq X$ [[Closed Set|closed]], and $f: A \rightarrow \mathbb{R}$ continuous. Then there exists a continuous $F: X \rightarrow \mathbb{R}$ with $F|_A = f$. If $|f| \leq M$ on $A$, then $F$ can be chosen with $|F| \leq M$ on $X$.

Theorem 1 is the special case $X = \mathbb{R}$. The vector-valued version follows by extending each component ([[Continuous Function Component Theorem]]).

# Properties
- Closedness is necessary: on a non-closed set, a continuous function can blow up or oscillate near a [[Limit Point]] outside the set.
- Contrast with [[Uniformly Continuous Function Extension of Function Theorem]], which extends from a [[Dense Subset]] rather than a closed one, and needs uniform continuity.
- Holds in exactly the [[Normal Space|normal spaces]] (equivalent to Urysohn's lemma).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=108)
[^2]: [Tietze extension theorem - Wikipedia](https://en.wikipedia.org/wiki/Tietze_extension_theorem)
