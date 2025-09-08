---
tags: mathematics, linear_algebra
---

# Definition

> [!info] Definition 1 (Upper Triangular Matrix)
> An $n \times n$ [[Matrix|matrix]] is upper triangular if $a_{ij} = 0$ when $i > j$. In matrix form, it looks like[^1]
> $$
> \begin{align}
> \begin{bmatrix}
> a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
> 0 & a_{22} & a_{23} & \dots & a_{2n} \\
> 0 & 0 & a_{33} & \dots & a_{3n} \\
> \vdots & \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & 0 & \dots & a_{mn}
> \end{bmatrix}
> \end{align}
> $$

> [!abstract] Theorem 1
> If $a_{ii} \neq 0$ for each $i$, then the [[Linear System of Equations|linear system]] is consistent.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=32)