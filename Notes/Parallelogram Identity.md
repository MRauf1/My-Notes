---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Proposition 1 (Parallelogram Identity)[^1]
> If $V$ is an [[Inner Product Space]], then for any $v, w \in V$,
> $$
> \lVert v + w \rVert^2 + \lVert v - w \rVert^2 = 2 \lVert v \rVert^2 + 2 \lVert w \rVert^2
> $$

Geometrically, the sum of the squares of the lengths of the four sides of the parallelogram spanned by $v$ and $w$ equals the sum of the squares of the lengths of its two diagonals ($v+w$ and $v-w$).

![[Parallelogram Identity.png]]

Although this is a theorem about inner product spaces, it directly involves only the norm, not the inner product itself. This means it can be used to check whether a given [[Normed Space|norm]] comes from an inner product: if any two vectors $v, w$ in a normed space fail to satisfy this identity, the norm cannot be the norm associated to any inner product.

# Properties
- [[Normed Space]]
- [[Strictly Convex Space]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=288)
