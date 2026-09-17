---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Corollary 6.7 -- [[Similar Matrix]] [[Determinant]])[^1]
> If $A, B \in M_n(\mathbb{F})$ are similar, then $\det(A) = \det(B)$.

> [!abstract] Theorem 2 (Corollary -- Basis-Independence)
> If $T \in \mathcal{L}(V)$ and $\mathcal{B}, \mathcal{B}'$ are any two bases of $V$, then $\det([T]_{\mathcal{B}}) = \det([T]_{\mathcal{B}'})$.

Theorem 2 follows from Theorem 1 together with the fact that matrices of $T$ with respect to different bases are always similar ([[Similar Matrix]]). This is exactly what makes $\det(T)$ ([[Determinant]]) well-defined: it does not matter which basis is used to compute it, the answer is always the same.

# Properties
- [[Determinant]]
- [[Similar Matrix]]
- [[Invariant of Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=359)
