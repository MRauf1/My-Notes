---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!abstract] Theorem 1 ([[Matrix]] of [[Linear Map]])[^1]
> Let $T \in \mathcal{L}(\mathbb{F}^n, \mathbb{F}^m)$. Then there is a unique [[Matrix]] $A \in M_{m, n}(\mathbb{F})$ such that for every $v \in \mathbb{F}^n$, $T(v) = Av$.
> We call $A$ the matrix of $T$ or say that $T$ is represented by $A$.
> In particular, every [[Finite-Dimensional Linear Operator]] can be represented by its own unique [[Matrix]].
> In particular, there is an [[Linear Map Isomorphism]] between $\mathcal{L}(\mathbb{F}^n, \mathbb{F}^m)$ and $M_{m, n}(\mathbb{F]})$. Addition and scalar multiplication of linear maps correspond to addition and scalar multiplication of matrices.

> [!abstract] Theorem 2 (Generalized Version)[^2]
> Suppose that $dim(V) = n, dim(W) = m$, and $\mathcal{B}_V, \mathcal{B}_W$ are the [[Basis]] of $V, W$ respectively. Then the [[Linear Map]] $C_{\mathcal{B}_V, \mathcal{B}_W}: \mathcal{L}(V, W) \rightarrow M_{m, n}(\mathbb{F})$ defined by $C_{\mathcal{B}_V, \mathcal{B}_W}(T) = [T]_{\mathcal{B}_V, \mathcal{B}_W}$ is a [[Linear Map Isomorphism]].

> [!abstract] Theorem 3 (Corollary)
> Let $V, W$ be [[Finite-Dimensional Vector Space]]. Then $dim(\mathcal{L}(V, W)) = dim(V) \cdot dim(W)$.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=103)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=210)