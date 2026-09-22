---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Coordinate Frame)[^1]
> A coordinate system consisting of an origin point $\mathbf{p}$ and a basis $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ (assumed [[Orthonormal Basis|orthonormal]] by convention unless stated otherwise). A point with frame coordinates $(u, v, w)$ represents the point $\mathbf{p} + u\mathbf{u} + v\mathbf{v} + w\mathbf{w}$ in the ambient (canonical) frame.

# Properties
- The **frame-to-canonical matrix** converts coordinates expressed in a frame into coordinates expressed in the canonical frame; its inverse, the **canonical-to-frame matrix**, converts in the opposite direction.
- Re-expressing a point in a different frame is a change of coordinates, so the same transformation matrix can be read two ways: as moving points within one fixed frame, or as re-expressing fixed points in a different frame — a duality analogous to the [[Change of Basis Matrix|change of basis matrix]] for vector spaces, but extended to include an origin, which requires [[Homogeneous Coordinates]] to represent as a single matrix.
- The [[Camera Frame]] used in [[Ray Generation]] is a specific coordinate frame with the viewpoint as origin.
- The [[Camera Transformation]] in the [[Viewing Transformation]] pipeline is the canonical-to-frame matrix of a camera's coordinate frame.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=149&annotation=GU9IY2P2)
