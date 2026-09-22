---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Projective Transformation)[^1]
> A transformation of [[Homogeneous Coordinates]] by a general matrix whose result is normalized by dividing by its last ("$w$") component: given $\tilde{\mathbf{x}} = M\mathbf{x}$ in homogeneous form, the transformed ordinary point is $\tilde{\mathbf{x}}/\tilde{w}$. Also called a homography.

# Properties
- Generalizes linear maps ($x' = ax+by+cz$) and [[Affine Transformation|affine transformations]] ($x' = ax+by+cz+d$) to "linear rational functions" that share a common denominator across all output coordinates.
- Maps lines to lines (and, in 2D, squares to quadrilaterals), but does not preserve parallel lines.
- The matrix $M$ is defined only up to a nonzero scalar multiple: scaling $M$ by $c$ scales both the numerator and the shared denominator by $c$, leaving the normalized result unchanged.
- Equivalently viewed as an ordinary linear map on homogeneous vectors under the equivalence $\mathbf{x} \sim \alpha\mathbf{x}$ for all $\alpha \neq 0$ (i.e., all points on the same line through the origin represent the same point in space); a homogeneous vector can be transformed repeatedly — even passing through $w=0$ at an intermediate step — and needs to be normalized (divided by $w$) only once ordinary coordinates are required, which amounts to intersecting its line through the origin with the plane $w=1$.
- The [[Perspective Projection Matrix]] is a projective transformation; an affine transformation is the special case whose bottom row is $(0,\dots,0,1)$, so that $\tilde{w}$ is always $1$ and no normalization is needed.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=163&annotation=4JI7MLD4)
