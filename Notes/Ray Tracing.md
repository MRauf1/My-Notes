---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Ray Tracing)[^1]
> A form of [[Image-Order Rendering]] that computes one pixel at a time by finding the object seen at that pixel's position: any object visible to a pixel must intersect the pixel's viewing ray, a line emanating from the viewpoint in the direction the pixel looks, and the object of interest is the one that intersects the ray nearest the camera.

# Properties
- A basic ray tracer has three parts:
	- [[Ray Generation]], which computes the origin and direction of each pixel's viewing ray from the camera geometry.
	- [[Ray Intersection]], which finds the closest object intersecting the viewing ray.
	- [[Shading]], which computes the pixel color from the results of ray intersection.
- Extends naturally to [[Shadow Ray|shadow rays]] and [[Specular Reflection|reflection rays]] by tracing additional rays from the intersection point.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
