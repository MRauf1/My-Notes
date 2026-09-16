---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Proposition 1 (Proposition 5.16)[^1]
> Let $V$ and $W$ be [[Finite-Dimensional Vector Space|finite-dimensional]] [[Inner Product Space]]s and let $T \in \mathcal{L}(V, W)$. Then:
> 1. $\ker T^* = (\text{range } T)^\perp$
> 2. $\text{range } T^* = (\ker T)^\perp$

This gives a new proof of the [[Rank-Nullity Theorem]] in inner product spaces: $V$ orthogonally decomposes as
$$
V = \ker T \oplus (\ker T)^\perp = \ker T \oplus \text{range } T^*
$$
Taking dimensions of both sides gives $\dim V = null(T) + rank(T^*) = null(T) + rank(T)$, recovering the Rank-Nullity Theorem. The decomposition itself says more: every vector in $V$ splits into two orthogonal pieces, one in $\ker T$ and one in $\text{range } T^*$. The subspaces $\text{range } T$, $\ker T$, $\text{range } T^*$, and $\ker T^*$ are sometimes called the four fundamental subspaces associated to $T$.

# Properties
- [[Adjoint]]
- [[Kernel]]
- [[Linear Map Image]]
- [[Orthogonal Complement]]
- [[Rank-Nullity Theorem]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=335)
