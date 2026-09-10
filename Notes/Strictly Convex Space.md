---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Strictly Convex Norm)[^1]
> A norm on a real vector space $V$ is strictly convex if, for every $v, w \in V$ with $\lVert v \rVert = \lVert w \rVert = 1$,
> $$
> \left\lVert \tfrac{1}{2}(v + w) \right\rVert < 1
> $$

Equivalently, a normed space $(X, \lVert \cdot \rVert)$ is strictly convex if its closed unit ball is a [[Convex Set|strictly convex set]]: given any two distinct points $x, y$ on the unit sphere $\partial B$, the line segment joining $x$ and $y$ meets $\partial B$ only at $x$ and $y$ (the boundary contains no line segments).

![[Strictly Convex Unit Balls.png]]

> [!abstract] Theorem 2 (Standard Norm on $\mathbb{R}^n$ is Strictly Convex)[^1]
> The standard [[Vector Norm|norm]] on $\mathbb{R}^n$ is strictly convex. This follows from the [[Parallelogram Identity]].

> [!abstract] Theorem 3 ($1$-Norm is not Strictly Convex)[^1]
> The [[1-Norm]] on $\mathbb{R}^n$ is not strictly convex if $n \geq 2$.

Strict convexity sits strictly between a general [[Normed Space]] and an [[Inner Product Space]] in terms of structure: every inner product space is strictly convex, but not every strictly convex normed space arises from an inner product. Strict convexity guarantees the uniqueness of a best approximation to an element of $X$ out of a convex subspace $Y$, provided such an approximation exists (compare the [[Best Approximation Theorem]] for inner product spaces).

If a strictly convex normed space $X$ is complete and satisfies the (slightly stronger) property of being a [[Uniformly Convex Space]], then $X$ is also reflexive, by the Milman–Pettis theorem.

# Properties
- [[Normed Space]]
- [[Inner Product Space]]
- [[Parallelogram Identity]]
- [[Uniformly Convex Space]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=296)
