---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Eigenvector)[^1]
> Let $V$ be [[Vector Space]] over $\mathbb{F}$ and $T \in \mathcal{L}(V)$. [[Vector]] $v \in V$ is an eigenvector of $T$ with eigenvalue $\lambda \in \mathbb{F}$ if $v \neq 0$ and $Tv = \lambda v$.
> If $A \in M_n(\mathbb{F})$, the eigenvalues and eigenvectors of A are the eigenvalues and eigenvectors of the [[Linear Map]] in $\mathcal{L}(\mathbb{F}^n)$ defined by $v \rightarrow Av$.

They only exist for [[Square Matrix]].

Non-zero vectors on which $T$ acts by scalar multiplication. Geometrically, $T$ may change the length of the eigenvector, but not its direction (opposite direction is allowed though). Algebraically, the set $\langle v \rangle$ of all scalar multiples of $v$ is invariant under $T$ (if $w \in \langle v \rangle$, then $T(w) \in \langle v \rangle$).

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=89)