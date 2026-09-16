---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Corollary 1 (Corollary 5.24 -- The Schur Decomposition)[^1]
> Let $V$ be a finite-dimensional complex [[Inner Product Space]] and $T \in \mathcal{L}(V)$. Then there is an [[Orthonormal Basis]] $\mathcal{B}$ of $V$ such that $[T]_{\mathcal{B}}$ is [[Upper Triangular Matrix|upper triangular]]. Equivalently, if $A \in M_n(\mathbb{C})$, then there exist a [[Unitary Matrix|unitary]] matrix $U \in M_n(\mathbb{C})$ and an upper triangular matrix $R \in M_n(\mathbb{C})$ such that
> $$
> A = URU^*
> $$

While the [[Spectral Theorem]] can only unitarily *diagonalize* [[Normal Matrix|normal]] operators, every operator on a complex inner product space can be unitarily *triangularized* — the next-best universal result once normality fails. This only works over $\mathbb{C}$: triangularizing every matrix at all (with any basis, orthonormal or not) already requires the base field to be [[Algebraically Closed Field|algebraically closed]] (see [[Triangular Matrix Algebraically Closed Field Similar Matrix]]).

In practice, the Schur decomposition of a matrix is computed by an iterative version of the [[QR Decomposition|QR algorithm]], rather than the inductive, basis-by-basis construction used to prove Corollary 1.[^2]

# Properties
- [[Upper Triangular Matrix]]
- [[Unitary Matrix]]
- [[Triangular Matrix Algebraically Closed Field Similar Matrix]]
- [[Spectral Theorem]]
- [[QR Decomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=347)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=349)
