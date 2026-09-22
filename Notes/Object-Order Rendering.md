---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Object-Order Rendering)[^1]
> An approach to [[Rendering]] in which each object is considered in turn, and for each object all the pixels that it influences are found and updated. The "for each object" loop is on the outside, nested around a "for each pixel" loop.

# Properties
- Contrasts with [[Image-Order Rendering]], which considers pixels rather than objects on the outer loop; the two can compute exactly the same images but suit different effects and have different performance characteristics.
- Effects like accurate shadows and reflections, which are easy in [[Ray Tracing]], are comparatively awkward to produce in the object-order framework.
- Relies on a [[Viewing Transformation]] to rapidly find the image-space location of each object in the scene.
- Implemented in practice by the [[Graphics Pipeline]], which finds the pixels occupied by each object via [[Rasterization]]; its single pass over all scene geometry is sped up in complex scenes using [[Culling]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
