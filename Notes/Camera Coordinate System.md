---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Camera Coordinate System)[^1]
> The 2D coordinates $(x, y)$ of a point on the **virtual camera plane** of a [[Pinhole Camera]]: a plane placed at distance $f$ in front of the pinhole, mirroring the true projection plane, which lies behind the pinhole at the same distance $f$. Placing the virtual camera plane in front of the pinhole produces a projected image without the inversion that the true projection plane introduces. The $x, y$ axes are parallel to the [[World Coordinate System|world]] axes $X, Y$ and, unlike on the true projection plane, have the same sign as the world coordinates.

# Properties
- Related to [[World Coordinate System|world coordinates]] $(X, Y, Z)$ by the [[Perspective Projection Equations]], $x = fX/Z$ and $y = fY/Z$.
- Related to [[Image Coordinate System|image coordinates]] $(n, m)$, which are measured in pixels, by an affine transform.
- Plays a role analogous to the [[Camera Frame]] and [[Focal Length]] used to define viewing rays in computer graphics, though the pinhole camera model places its origin at the pinhole rather than at an eye point positioned behind the image plane.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
