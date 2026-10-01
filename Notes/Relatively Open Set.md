---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Open Set Relative to a Subspace)[^1]
> Let $(X, d)$ be a [[Metric Space]] and $Y \subseteq X$ (so $Y$ is itself a metric space under the restriction of $d$). A set $E \subseteq Y$ is open relative to $Y$ if, for every $p \in E$, there exists $r > 0$ such that $q \in E$ whenever $q \in Y$ and $d(p, q) < r$.

> [!abstract] Theorem 2 (Relative Openness Characterization)[^2]
> Let $(X, d)$ be a [[Metric Space]] and $Y \subseteq X$. A subset $E$ of $Y$ is open relative to $Y$ if and only if $E = Y \cap G$ for some [[Open Set|open]] subset $G$ of $X$.

My interpretation: whether a set is open or closed is relative to the ambient space it is viewed inside, not an absolute property of the set. If $Y$ is treated as its own metric space, it is always both open and closed in itself (it is [[Clopen Set|clopen]] relative to itself), but its openness/closedness relative to a larger space $X$ depends on how $Y$ sits inside $X$. For example, with $X = \mathbb{R}$:
- $Y = [0, 1)$ is neither open nor closed in $X$ (though it is clopen in itself).
- $Y = [0, 1]$ is closed but not open in $X$.
- $Y = (0, 1)$ is open but not closed in $X$.

# Properties
- [[Clopen Set]]
- Unlike openness and closedness, [[Compact Set|compactness]] does not depend on the embedding space.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=44)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=45)
