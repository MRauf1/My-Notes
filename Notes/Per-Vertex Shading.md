---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Per-Vertex Shading)[^1]
> Also called Gouraud shading: evaluating a [[Shading]] equation once per vertex — using that vertex's position and normal together with the light and camera positions — and then interpolating the resulting vertex colors across each primitive via [[Gouraud Interpolation]], rather than evaluating shading at every pixel.

# Properties
- Cannot reproduce shading detail finer than the primitives used to draw the surface, since shading is computed only at vertices and never in between; see [[Shading Frequency]].
- Shading computations should be performed in a coordinate system that remains orthonormal when viewed in world space (e.g., world space or eye space), since shading equations depend on angles between vectors, and angles are not preserved by operations such as nonuniform scale (often used in the modeling transformation) or [[Perspective Projection|perspective projection]].
- Shading in eye space has the added convenience that the camera position never needs to be tracked separately: the camera sits at the origin in eye space in a perspective projection, and the view direction is always $+z$ in an orthographic projection.
- Contrasts with [[Per-Fragment Shading]], which evaluates the shading equation once per fragment instead of once per vertex.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=190&annotation=T95PZVI4)
