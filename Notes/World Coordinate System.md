---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (World Coordinate System)[^1]
> The coordinate system whose origin is the pinhole of a [[Pinhole Camera]]. The 3D position of a point $\mathbf{P}$ in the world is written $\mathbf{P} = (X, Y, Z)$, where the $Z$ axis is perpendicular to the camera's sensing (projection) plane.

# Properties
- Serves as the reference frame from which points are mapped into [[Camera Coordinate System|camera coordinates]] via the [[Perspective Projection Equations]].
- Placing the origin at the pinhole itself, rather than at a point in front of the camera, distinguishes this convention from simpler world coordinate setups sometimes used elsewhere in [[Computer Vision]].

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
