---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Image-Order Rendering)[^1]
> An approach to [[Rendering]] in which each pixel is considered in turn, and for each pixel all the objects that influence it are found and the pixel value is computed. The "for each pixel" loop is on the outside, nested around a "for each object" loop.

# Properties
- Contrasts with [[Object-Order Rendering]], which considers objects rather than pixels on the outer loop; the two can compute exactly the same images but suit different effects and have different performance characteristics.
- Broadly speaking, image-order rendering is simpler to get working and more flexible in the effects it can produce (e.g., shadows and reflections), but usually takes much more execution time to produce a comparable image.
- [[Ray Tracing]] is the canonical image-order rendering algorithm.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
