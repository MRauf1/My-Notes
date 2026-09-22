---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Multisample Antialiasing)[^1]
> An optimization of [[Supersampling]] that samples visibility (coverage and depth) at a higher rate than shading, since the sharp edges that cause [[Aliasing]] usually come from primitive edges rather than fast shading variation within a primitive.

# Properties
- Systems using [[Per-Vertex Shading]] (e.g., RenderMan) achieve this cheaply by rasterizing at high resolution, since interpolating already-computed shading colors to many fragments is inexpensive.
- Hardware pipelines using [[Per-Fragment Shading]] instead store, per fragment, a single shading color together with a coverage mask and a set of depth values for several sub-pixel sample points.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=193&annotation=CFHTE872)
