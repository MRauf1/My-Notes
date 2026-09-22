---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Camera Transformation)[^1]
> The first stage of the [[Viewing Transformation]] pipeline: a [[Rigid-Body Transformation]] that converts points from world space into camera space by placing the camera at the origin in a convenient orientation. It depends only on the camera's pose — an eye position $\mathbf{e}$, a gaze direction $\mathbf{g}$, and a view-up vector $\mathbf{t}$.

# Properties
- Constructs a right-handed $\mathbf{u}, \mathbf{v}, \mathbf{w}$ [[Camera Frame|camera basis]] with $\mathbf{w}$ opposite the gaze direction and $\mathbf{v}$ coplanar with $\mathbf{g}$ and $\mathbf{t}$.
- Equal to the canonical-to-frame matrix (see [[Coordinate Frame]]) of this camera coordinate frame: $M_{cam} = R\,T$, where $R$ is the rotation with rows $\mathbf{u}, \mathbf{v}, \mathbf{w}$ and $T$ translates by $-\mathbf{e}$.
- Equivalently understood as first translating the eye $\mathbf{e}$ to the origin, then rotating the basis $\mathbf{u}, \mathbf{v}, \mathbf{w}$ onto the canonical axes $x, y, z$.
- Also called the eye transformation; sometimes "viewing transformation" is used by other sources to refer to just this stage rather than the full pipeline.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=155&annotation=PV89U52L)
