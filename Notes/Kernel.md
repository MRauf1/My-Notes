---
tags:
  - mathematics
  - abstract_algebra
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Kernel)
> For a [[Group Homomorphism]] $\phi: G \rightarrow H$, its kernel is
> $$
> \begin{align}
> ker(\phi) := \{g \in G | \phi(g) = e_H\} \leq G
> \end{align}
> $$

> [!info] Definition 2 (Kernel of [[Linear Map]])[^1]
> Let $T \in \mathcal{L}(V, W)$. The kernel/nullspace of $T$ is the [[Set]] $ker(T) := \{v \in V | T(v) = 0\}$. The kernel/nullspace of $A \in M_{m, n}(\mathbb{F})$ is the kernel of the [[Linear Map]] from $\mathbb{F}^n$ to $\mathbb{F}^m$ represented by $A$.
> It is the [[Set]] of solutions to the [[Homogeneous Linear System]] $Ax = 0$.

Since $0$ is the identity element of [[Vector Space]] (since the main [[Operation]] in [[Vector Space]] is [[Addition]]), the two terms are synonymous.

# Properties
- [[Linear Map Injective Kernel]]
- [[Kernel Linear System]]

## [[Subgroup]]/[[Vector Subspace]]
- $ker(\phi)$ is a [[Normal Subgroup]]
- [[Kernel Vector Subspace]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=138)