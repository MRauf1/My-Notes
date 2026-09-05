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

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
