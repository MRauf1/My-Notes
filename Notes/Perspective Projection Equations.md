---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Perspective Projection Equations)[^1]
> For a [[Pinhole Camera]] whose sensing plane lies at distance $f$ from the pinhole, similar triangles relate the [[World Coordinate System|world coordinates]] $(X, Y, Z)$ of a scene point to its [[Camera Coordinate System|camera-plane coordinates]] $(x, y)$:
> $$
> \begin{align}
> x &= f\frac{X}{Z} \\
> y &= f\frac{Y}{Z}
> \end{align}
> $$

# Properties
- Under this projection, distant objects appear smaller, through the inverse scaling by $Z$.
- Apply not just to pinhole cameras, but to most lens-based cameras and to human vision as well.
- An instance of [[Perspective Projection]], specialized to the pinhole camera model with explicit world and camera coordinates; the general graphics notion of perspective projection instead specifies the projection by a viewpoint and image plane without reference to a physical pinhole.
- Contrasts with [[Orthographic Projection]], which does not scale objects by their distance from the camera.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
