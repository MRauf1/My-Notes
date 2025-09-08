---
tags: mathematics, linear_algebra
---

# Definition

> [!info] Definition 1 ([[Vector|Vector]] Space)[^1]
> A vector space over a [[Field|field]] $\mathbb{F}$ is the [[Set|set]] $V$ with [[Operation|operations]] $+$ ([[Vector Addition|vector addition]]) and $\cdot$ ([[Vector Scalar Multiplication|vector scalar multiplication]]) and an element $\mathbf{0} \in V$ such that
> 1) Vector space is closed under vector addition: $\forall \mathbf{v}, \mathbf{w} \in V, \mathbf{v} + \mathbf{w} \in V$
> 2) Vector space is closed under vector scalar multiplication: $\forall c \in \mathbb{F}, \forall \mathbf{v} \in V, c \cdot \mathbf{v} \in V$
> 3) Vector addition is [[Commutative Property|commutative]]: $\forall \mathbf{v}, \mathbf{w} \in V, \mathbf{v} + \mathbf{w} = \mathbf{w} + \mathbf{v}$
> 4) Vector addition is [[Associative Property|associative]]: $\forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in V, \mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w}$
> 5) $\mathbf{0}$ vector is the additive identity: $\forall \mathbf{v} \in V, \mathbf{v} + 0 = 0 + \mathbf{v} = \mathbf{v}$
> 6) Every vector has an additive [[Inverse|inverse]]: $\forall \mathbf{v} \in V \exists \mathbf{w} \in V, \mathbf{v} + \mathbf{w} = \mathbf{w} + \mathbf{v} = 0$
> 7) Multiplication by $1$: $\forall \mathbf{v} \in V, 1 \cdot \mathbf{v} = \mathbf{v}$
> 8) Vector scalar multiplication is associative: $\forall a, b \in \mathbb{F} \forall \mathbf{v} \in V, a \cdot (b \cdot \mathbf{v}) = (a \cdot b) \cdot \mathbf{v}$
> 9) [[Distributive Property|Distributive Law 1]]: $\forall a \in \mathbb{F} \forall \mathbf{v}, \mathbf{w} \in V, a \cdot (\mathbf{v} + \mathbf{w}) = a \cdot \mathbf{v} + a \cdot \mathbf{w}$
> 10) Distributive Law $2$: $\forall a, b \in \mathbb{F} \forall \mathbf{v} \in V, (a + b) \cdot \mathbf{v} = a \cdot \mathbf{v} + b \cdot \mathbf{v}$

# Types

## Examples

- $\mathbb{F}^n$
- [[Complex Vector Space]]
- [[Real Vector Space|Real Vector Space]]

## Other

- [[Vector Subspace|Vector Subspace]]
- [[Function Space|Function Space]]

# Properties

- Additive identity is unique
- Additive inverses of vectors are unique ($-\mathbf{v}$)
- $\forall \mathbf{v} \in V, - (- \mathbf{v}) = \mathbf{v}$
- $\forall \mathbf{v} \in V, 0 \cdot \mathbf{v} = \mathbf{0}$
- $\forall a \in \mathbb{F}, a \cdot \mathbf{0} = \mathbf{0}$
- $\forall \mathbf{v} \in V, -1 \cdot \mathbf{v} = -v$
- $\forall a \in \mathbb{F} \forall \mathbf{v} \in V, a \cdot \mathbf{v} = 0 \implies a = 0 \lor \mathbf{v} = \mathbf{0}$

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=71)