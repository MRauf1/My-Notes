---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Group Homomorphism)
> [[[Function]] $\phi: G \rightarrow H$ ($G, H$ are [[Group]]) such that
> $$
> \begin{align}
> \phi(ab) = \phi(a) \phi(b)
> \end{align}
> $$
> $\forall a, b \in G$
> Notice that the first product is a product in $G$, while the second product is a product in $H$

# Properties
- [[Image]]
- [[Kernel]]

## Applying Homomorphism
- $\phi(e_G) = e_H$
- $\phi(a^{-1}) = \phi(a)^{-1}$

## Homomorphism Composition
- $\phi: G \rightarrow H, \psi: H \rightarrow K$ are homomorphisms, then $\psi \circ \phi: G \rightarrow K$ is a homomorphism

## Theorems
- [[Group Homomorphism Theorem]]

## Other
- $\phi$ is [[Injective Function]] $\iff$ $ker(\phi) = \{e_G\}$

# Types
- [[Group Isomorphism]]
