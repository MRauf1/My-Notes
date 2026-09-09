---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Orthogonal Direct Sum)[^1]
> Suppose that $U_1, \dots, U_m$ are subspaces of an [[Inner Product Space]] $V$. $V$ is the orthogonal direct sum of $U_1, \dots, U_m$ if:
> 1) Every vector $v \in V$ can be written as $v = u_1 + \dots + u_m$ for some $u_1 \in U_1, \dots, u_m \in U_m$, and
> 2) Whenever $u_j \in U_j$ and $u_k \in U_k$ for $j \neq k$, $u_j$ and $u_k$ are [[Orthogonal Vector|orthogonal]].
>
> In that case we write $V = U_1 \oplus \dots \oplus U_m$.

# Properties
- The decomposition $v = u_1 + \dots + u_m$ of each $v \in V$ is unique.
- $dim(V) = dim(U_1) + \dots + dim(U_m)$.
- [[Orthogonal Decomposition Theorem]] is the special case $m = 2$ with $U_1 = U$ and $U_2 = U^\perp$.
- If $U$ is a subspace of a finite-dimensional [[Inner Product Space]] with $U = U_1 \oplus \dots \oplus U_m$, then $P_U = P_{U_1} + \dots + P_{U_m}$, where $P_U$ denotes the [[Orthogonal Projection]] onto $U$.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=274)
