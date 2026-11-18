---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Tietze Extension Theorem)[^1]
> Let $X$ be a [[Metric Space]] (more generally, a [[Normal Space]]), $A \subseteq X$ [[Closed Set|closed]], and $f: A \rightarrow \mathbb{R}$ continuous. Then there exists a continuous $F: X \rightarrow \mathbb{R}$ with $F|_A = f$. If $|f| \leq M$ on $A$, then $F$ can be chosen with $|F| \leq M$ on $X$.

The special case $X = \mathbb{R}$ is [[Continuous Extension from Closed Subset of Real Line]], which has an elementary proof by linear interpolation. Applying the theorem componentwise ([[Continuous Function Component Theorem]]) gives the $\mathbb{R}^k$-valued version.

# Properties
- Closedness is necessary (see [[Continuous Extension from Closed Subset of Real Line]]).
- Contrast with [[Uniformly Continuous Function Extension of Function Theorem]], which extends from a [[Dense Subset]] rather than a closed one, and needs uniform continuity.
- Holds in exactly the [[Normal Space|normal spaces]] (equivalent to Urysohn's lemma).

[^1]: [Tietze extension theorem - Wikipedia](https://en.wikipedia.org/wiki/Tietze_extension_theorem)
