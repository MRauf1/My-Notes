---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Extreme Value Theorem)[^1]
> If $f$ is [[Continuous Function]] on a [[Interval Notation|closed interval]] $[a, b]$, then $f$ attains an [[Absolute Minimum]] $f(c)$ and [[Absolute Maximum]] $f(d)$ at some numbers $c, d \in [a, b]$.

> [!abstract] Theorem 2 (Extreme Value Theorem on [[Compact Metric Space]])[^2]
> Let $f$ be a continuous real function on a [[Compact Metric Space]] $X$, and
> $$
> \begin{align}
> M = \sup_{p \in X} f(p), \qquad m = \inf_{p \in X} f(p)
> \end{align}
> $$
> Then there exist points $p, q \in X$ such that $f(p) = M$ and $f(q) = m$.

Equivalently, $f(q) \leq f(x) \leq f(p)$ for all $x \in X$: $f$ attains its maximum (at $p$) and its minimum (at $q$). Definition 1 is the special case $X = [a, b]$.

# Properties
- Follows from [[Continuous Function Compact Metric Space Theorem]]: $f(X)$ is closed and bounded, so it contains its [[Supremum]] and [[Infimum]].
- Fails without compactness: [[Noncompact Subset of Real Line Continuous Function Theorem]]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=310)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=98)
