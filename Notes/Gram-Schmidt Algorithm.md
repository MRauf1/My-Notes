---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!abstract] Theorem 1 (The [[Gram-Schmidt Algorithm|Gram-Schmidt]] [[Algorithm]])[^1]
> Let $V$ be an [[Inner Product Space]], and let $(v_1, \dots, v_k)$ be a [[Linearly Independent]] list of [[Vector|vectors]] in $V$. Define
> $$
> \begin{align}
> u_1 &= v_1, & e_1 &= \frac{u_1}{\lVert u_1 \rVert}
> \end{align}
> $$
> and for $j = 2, \dots, k$,
> $$
> \begin{align}
> u_j &= v_j - \sum_{i=1}^{j-1} \langle v_j, e_i \rangle e_i, & e_j &= \frac{u_j}{\lVert u_j \rVert}
> \end{align}
> $$
> Then $(e_1, \dots, e_k)$ is an [[Orthonormal Vector|orthonormal]] list of [[Vector|vectors]] in $V$, and for each $j = 1, \dots, k$,
> $$
> \begin{align}
> \operatorname{span}(e_1, \dots, e_j) = \operatorname{span}(v_1, \dots, v_j)
> \end{align}
> $$

This [[Algorithm]] can be used to check for [[Linearly Dependent]] [[Vector]]. If you end up with a 0 [[Vector]] before the process ends, then the list is [[Linearly Dependent]].

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=264)
