---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Affine Transformation)
> Let $V$ be a [[Vector Space|vector space]] over a field $\mathbb{F}$. A function $f: V \rightarrow V$ is an affine transformation if there exists a [[Linear Map|linear map]] $T: V \rightarrow V$ and a vector $b \in V$ such that
> $$
> \begin{align}
> f(x) = Tx + b
> \end{align}
> $$

An affine transformation is a linear map composed with a translation. Unlike a linear map, it need not fix the origin ($f(0) = b$), but it still preserves collinearity (points on a line map to points on a line) and ratios of distances along a line.

# Types

- [[Isometry|Isometry]]
- [[Rigid-Body Transformation]]

# Properties

- [[Affine Symmetry|Affine Symmetry]]
- In computer graphics, an affine transformation of $\mathbb{R}^n$ is implemented as a single matrix multiplication using [[Homogeneous Coordinates]], which fold the linear map $T$ and the translation $b$ into one $(n+1)\times(n+1)$ matrix.[^2]

[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=143&annotation=27KKFH29)
