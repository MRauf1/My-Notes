---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Aliasing)[^1]
> The jagged appearance of lines and primitive edges that results from making an all-or-nothing (point-sampled) decision of whether each pixel is inside a primitive, rather than accounting for partial pixel coverage.

# Properties
- Affects both [[Rasterization]] and [[Ray Tracing]] identically when both point-sample at pixel centers: the set of fragments produced by standard ("aliased") rasterization is exactly the set of pixels a ray tracer would mark as hit by sending one ray through each pixel's center.
- Addressed by antialiasing techniques such as [[Box Filter Antialiasing]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=192&annotation=LGFI9NHW)
