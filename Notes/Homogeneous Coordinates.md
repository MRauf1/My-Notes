---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Homogeneous Coordinates)[^1]
> A representation of a $d$-dimensional point or vector using $d+1$ coordinates — e.g. $(x,y,1)$ in 2D or $(x,y,z,1)$ in 3D — so that an [[Affine Transformation]] (a linear map followed by a translation) can be applied with a single $(d+1)\times(d+1)$ matrix multiplication instead of a separate matrix multiplication and vector addition.

# Properties
- The added (homogeneous) coordinate is $1$ for a position and $0$ for a direction vector or offset; a $0$ in that slot makes the translation part of the matrix multiply against zero and be ignored, and it is copied unchanged into the result, so direction vectors are correctly left unaffected by translation while positions are correctly translated.
- Composing several affine transformations (rotations, scales, shears, translations) reduces to multiplying their homogeneous matrices together; the bottom row of such a matrix is always $(0, \dots, 0, 1)$.
- Geometrically, encoding a translation this way is equivalent to a 3D [[Shear Transformation|shear]] based on the added coordinate, restricted to the plane where that coordinate equals $1$.
- In perspective viewing, the homogeneous coordinate is allowed to take values other than $0$ or $1$, which is the basis for perspective projection matrices.
- More generally, the homogeneous vector $[x\ y\ z\ w]^T$ is defined to represent the ordinary point $(x/w,\, y/w,\, z/w)$, with $w$ acting as a shared denominator; this coincides with the earlier convention when $w=1$, but allowing the bottom row of the transformation matrix to be nonzero lets $w$ vary, yielding a [[Projective Transformation]] rather than only an affine one.[^2]

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=143&annotation=27KKFH29)
[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=162&annotation=V5YNPCP2)
