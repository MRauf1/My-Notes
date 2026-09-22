---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Per-Fragment Shading)[^1]
> Evaluating a [[Shading]] equation independently for each [[Fragment]], using per-fragment interpolated vectors (e.g., the eye-space surface normal and eye-space position), rather than interpolating already-shaded vertex colors as in [[Per-Vertex Shading]].

# Properties
- Avoids the interpolation artifacts of per-vertex shading, since the shading equation is evaluated at (up to) every pixel rather than only at vertices; see [[Shading Frequency]].
- Requires [[Vertex Processing]] to pass the geometric attributes needed for shading (e.g., eye-space normal and position) through the rasterizer as interpolated attributes via [[Gouraud Interpolation]], coordinating with the fragment-processing stage that consumes them.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=191&annotation=4F2ZRHR6)
