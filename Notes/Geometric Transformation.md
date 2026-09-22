---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Geometric Transformation)[^1]
> Operations such as rotation, translation, scaling, shearing, reflection, and projection that reposition or reshape geometry, all of which can be accomplished by multiplying point or vector coordinates by a transformation matrix.

# Types
- [[Scale Transformation]]
- [[Shear Transformation]]
- [[Rotation Matrix]]
- [[Reflection]]
- [[Affine Transformation]] (linear transformation composed with translation)
- [[Rigid-Body Transformation]]
- [[Perspective Projection]] / [[Parallel Projection]]

# Properties
- Sequences of transformations compose into a single matrix via [[Composition of Transformations|matrix multiplication]].
- Pure linear transformations (scale, shear, rotation, reflection) fix the origin; representing translation as well requires [[Homogeneous Coordinates]].
- A transformation matrix can be interpreted either as moving points within a fixed [[Coordinate Frame]], or as re-expressing fixed points in a different coordinate frame.
- Surface [[Normal Vector|normal]] vectors do not transform the same way as points or tangent vectors under a transformation matrix; see [[Normal Vector Transformation]].
- The image of a circle (or sphere) under any linear matrix transformation is an ellipse (or ellipsoid).

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=124&annotation=RXAI4IPK)
