---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Orthographic Projection)[^1]
> An alternative to [[Perspective Projection Equations|perspective projection]] from the 3D coordinates of a scene to the 2D coordinates of the sensor plane, in which rays are orthogonal to the projection plane, so the size of a projected object is independent of its distance to the camera:
> $$
> \begin{align}
> x &= kX \\
> y &= kY
> \end{align}
> $$
> where $(X, Y)$ are the [[World Coordinate System|world coordinates]] of the point, $(x, y)$ its projected coordinates, and $k$ a constant scaling factor accounting for change of units, which is a fixed global image scaling.

# Properties
- Also called **parallel projection**.
- Contrasts with the [[Perspective Projection Equations|perspective projection equations]], under which objects shrink with distance through inverse scaling by depth $Z$; here, no such depth-dependent scaling occurs.
- Corresponds to the graphics notion of [[Parallel Projection]] in the special case where the image plane is perpendicular to the projection direction, which that note calls orthographic.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
