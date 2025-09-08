---
tags: mathematics, linear_algebra
---

# Definition

> [!info] Definition 1 (Lower Triangular Matrix)
> An $n \times n$ [[Matrix|matrix]] is lower triangular if $a_{ij} = 0$ when $i < j$. In matrix form, it looks like[^1]
> $$
> \begin{align}
> \begin{bmatrix}
> a_{11} & 0 & 0 & \dots & 0 \\
> a_{21} & a_{22} & 0 & \dots & 0 \\
> a_{31} & a_{32} & a_{33} & \dots & 0 \\
> \vdots & \vdots & \vdots & \ddots & \vdots \\
> a_{m1} & a_{m2} & a_{m3} & \dots & a_{mn}
> \end{bmatrix}
> \end{align}
> $$

> [!abstract] Theorem 1
> If $a_{ii} \neq 0$ for each $i$, then the [[Linear System of Equations|linear system]] is consistent.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=32)