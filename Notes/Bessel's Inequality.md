---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Theorem 1 (Bessel's Inequality)[^1]
> If $(e_1, \dots, e_n)$ is an [[Orthonormal Vector|orthonormal]] list in an [[Inner Product Space]] $V$, then for every $v \in V$,
> $$
> \begin{align}
> \sum_{i=1}^n |\langle v, e_i \rangle|^2 \leq \lVert v \rVert^2
> \end{align}
> $$

The [[Pythagorean Theorem for Inner Product Space|Pythagorean Theorem]] is a special case of this inequality: if the orthonormal list is extended to an [[Orthonormal Basis]] of $V$, then $v = \sum_{i=1}^n \langle v, e_i \rangle e_i$ and equality holds.

# Properties
- Equality holds if and only if $v \in \operatorname{span}(e_1, \dots, e_n)$.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=260)
