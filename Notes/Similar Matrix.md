---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Similar [[Matrix]])[^1]
> A [[Matrix]] $A \in M_n(\mathbb{F})$ is similar to $B \in M_n(\mathbb{F})$ if there is an [[Invertible Linear Map]] $S \in M_n(\mathbb{F})$ such that $B = SAS^{-1}$.

The [[Matrix]] $A, B$ represent the same [[Linear Map]], but with respect to two different [[Basis]].

> [!abstract] Theorem 2 (Theorem)
> If $\mathcal{B}, \mathcal{B}'$ are both [[Basis]] of $V$, $T \in \mathcal{L}(V)$, $A = [T]_{\mathcal{B}}$, and $B = [T]_{\mathcal{B}'}$, then $A, B$ are similar.
> Conversely, suppose that $A, B \in M_n(\mathbb{F})$ are similar, $\mathcal{B}$ is a [[Basis]] of $V$, and $A = [T]_{\mathcal{B}}$. Then there is a [[Basis]] $\mathcal{B}'$ of $V$ such that $B = [T]_{\mathcal{B}'}$.

# Properties
- [[Invariant of Matrix]]
- [[Similar Matrix Eigenvalue]]
- [[Similar Matrix Rank-Nullity]]
- [[Similar Matrix Trace]]
- [[Similar Matrix Geometric Multiplicity of Eigenvalue]]
- [[Similar Matrix Matrix Transpose]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=223)