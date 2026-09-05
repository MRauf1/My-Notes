---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Ray Intersection)[^1]
> The second stage of [[Ray Tracing]]: given a viewing ray, finding the first intersection with a surface at a ray parameter $t$ in some interval $[t_0, t_1]$; the basic case takes $t_0 = 0$ and $t_1 = +\infty$, restricting to intersections not behind the ray's origin.

# Properties
- Solved analytically for implicit surfaces (see [[Ray-Sphere Intersection]]) and for parametric surfaces such as triangles and polygons (see [[Ray-Triangle Intersection]] and [[Ray-Polygon Intersection]]).
- For a scene containing many objects, a group of objects can itself be treated as a single intersectable object: the ray is tested against every object in the group, and the intersection with the smallest $t$ is returned, since this is the intersection nearest the camera.
- Restricting the search to $t \in [t_0, t_1]$ (rather than just $t > 0$) makes the same intersection routine reusable for [[Shadow Ray|shadow rays]] and [[Specular Reflection|reflection rays]], which require excluding a small interval near the ray's origin.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
