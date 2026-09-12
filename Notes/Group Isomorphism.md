---
tags:
  - mathematics
  - abstract_algebra
---

# Definition

> [!info] Definition 1 (Isomorphism)
> [[Bijective Function]] $\phi: G \rightarrow H$ ($G, H$ are [[Group]]) such that
> $$
> \begin{align}
> \phi(ab) = \phi(a) \phi(b)
> \end{align}
> $$
> $\forall a, b \in G$
> Notice that the first product is a product in $G$, while the second product is a product in $H$
> Isomorphism between the two groups is denoted as $G \cong H$

Isomorphism is a [[Group Homomorphism]] that is [[Bijective Function]].

# Types
- [[Group Automorphism]]

# Properties

## Inverse
- $\phi: G \rightarrow H$ is an isomorphism $\implies$ $\phi^{-1}: H \rightarrow G$ is an isomorphism

## Theorems
- [[Group Isomorphism Theorem]]
- [[Diamond Group Isomorphism Theorem]]

## [[Abelian Group]]
- $G \cong H \implies (G$ is abelian $\iff H$ is abelian)

# Examples
- $D_3$ ([[Symmetry]] of [[Equilateral Triangle]]) and $S_3$ ([[Permutation]] of $\{1, 2, 3\}$)
- $(Z_4, +)$ ([[Set of Congruence Classes Modulo n]]) and $\Phi(5, \cdot)$ ($\Phi$ being the [[Group of Modular Units]]) are both cyclic of order 4
- [[Symmetry]] of [[Rectangle]] and $\Phi(8, \cdot)$ are both isomorphic to the Klein four-group $\mathbb{Z}_2 \times \mathbb{Z}_2$ (not to $(Z_4, +)$, since neither has an element of order 4)