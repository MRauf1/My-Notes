---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Orthogonal Complement)[^1]
> Let $U$ be a [[Vector Subspace|subspace]] of an [[Inner Product Space]] $V$. The orthogonal complement of $U$ is the subspace
> $$
> \begin{align}
> U^\perp = \{v \in V \mid \langle u, v \rangle = 0 \text{ for every } u \in U\}
> \end{align}
> $$
> That is, $U^\perp$ consists of all those vectors $v$ which are [[Orthogonal Vector|orthogonal]] to every vector in $U$.

# Properties
- $(U^\perp)^\perp = U$ for any subspace $U$ of a finite-dimensional [[Inner Product Space]].
- $dim(U) + dim(U^\perp) = dim(V)$ for any subspace $U$ of a finite-dimensional [[Inner Product Space]] $V$.
- [[Orthogonal Decomposition Theorem]]: $V = U \oplus U^\perp$.
- [[Adjoint Kernel Range Theorem]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=272)
