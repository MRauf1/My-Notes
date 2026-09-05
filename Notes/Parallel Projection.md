---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Parallel Projection)[^1]
> The simplest type of projection, in which 3D points are mapped to 2D by moving them along a fixed projection direction until they hit the image plane. The resulting view is determined by the choice of projection direction and image plane.

![[Parallel and Perspective Projection.png]]

# Properties
- Called **orthographic** if the image plane is perpendicular to the projection (view) direction, and **oblique** otherwise.
- Contrasts with [[Perspective Projection]], which projects along lines through a single viewpoint rather than along parallel lines.
- All viewing rays generated for a parallel/orthographic view share the same direction, unlike in [[Perspective Projection]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
