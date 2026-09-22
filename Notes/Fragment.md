---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Fragment)[^1]
> The output unit produced by [[Rasterization]] for a [[Primitive (Computer Graphics)|primitive]]: one fragment per pixel covered by the primitive, each carrying its own set of interpolated attribute values (e.g., color, depth) at that pixel.

# Properties
- Processed in the fragment-processing stage of the [[Graphics Pipeline]] to compute a color and depth, ranging from simply passing through the rasterizer's interpolated values to full [[Per-Fragment Shading]].
- Combined with other fragments at the same pixel during [[Fragment Blending]], most commonly by the [[Z-Buffer Algorithm]].
- Its depth is obtained the same way as any other attribute, by interpolating the $z$-coordinate across the primitive via [[Gouraud Interpolation]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=175&annotation=T57QG7Q4)
