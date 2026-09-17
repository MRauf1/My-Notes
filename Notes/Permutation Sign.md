---
tags:
  - mathematics
  - abstract_algebra
---

# Definition

> [!info] Definition 1 (Permutation Sign)
> Function $sign: S_n \rightarrow \{\pm 1\}$ such that
> 1) $sign(e) = 1$
> 2) $sign(\tau) = -1$, where $\tau$ is a [[Transposition]]
> 3) $sign(\sigma \circ \tau) = sign(\sigma) \cdot sign(\tau)$, where $\sigma, \tau \in S_n$

# Permutation Sign as Matrices

![[Screenshot 2025-06-24 160751.png]]

> [!info] Definition 2 (Sign via the Permutation Matrix)[^1]
> Let $\sigma \in S_n$ with [[Permutation Matrix]] $A_\sigma$. The sign of $\sigma$ is $sgn(\sigma) := \det(A_\sigma)$.

This agrees with Definition 1: $\det(A_e) = \det(I_n) = 1$, and swapping two coordinates corresponds to a single row swap of $I_n$, which negates the determinant ([[Elementary Matrix]]).

> [!abstract] Theorem 3 (Lemma 6.16 -- Sign of the Inverse)[^2]
> For $\sigma \in S_n$, $sgn(\sigma) = sgn(\sigma^{-1})$.

# Properties
- [[Permutation Matrix]]
- [[Leibniz Formula for Determinant]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=372)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=372)