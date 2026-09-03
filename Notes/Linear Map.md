---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 ([[Linear]] Map)[^1]
> Let $V, W$ be [[Vector Space]]. A [[Function]] $T: V \rightarrow W$ is a linear map (linear transformation, [[Linear Operator]]) if it satisfies the following properties:
> 1) Additivity: For each $u, v \in V$, $T(u + v) = T(u) + T(v)$
> 2) Homogeneity: For each $v \in V, a \in \mathbb{F}$, $T(av) = a T(v)$
> The set of all linear maps from $V$ to $W$ is denoted as $\mathcal{L}(V, W)$. When $V, W$ are the same, we write $\mathcal{L}(V) := \mathcal{L}(V, V)$.
> If $S, T$ are linear maps, then their sum and scalar product is
> 3) $(S + T)(v) = S(v) + T(v)$
> 4) $(cT)(v) = c(T(v))$

Linear maps respect the vector space structure - performing vector space operations (addition, scalar multiplication) work the same whether you do it before or after the transformation.

# Examples
- [[Reflection]]
- [[Rotation]]

# Representation
- [[Matrix of Linear Map]]

# Types
- [[Invertible Linear Map]]
- [[Diagonalizable Linear Map]]

# Properties
- [[Linear Map Image]]
- [[Linear Map Isomorphism]]
- [[Linear Map of Zero]]
- [[Linear Map Composition]]
- [[Two Linear Maps Sum and Product]]
- [[Kernel]]
- [[Eigenspace]]
- [[Linear Map Distributive Law]]
- [[Linear Map Injective Kernel]]
- [[Linear Map Injective Linear Independence]]
- [[Basis Unique Linear Map]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=84)