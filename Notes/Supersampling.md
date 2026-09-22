---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Supersampling)[^1]
> The most direct implementation of [[Box Filter Antialiasing]]: rendering an image at a much higher resolution than needed, then downsampling (averaging groups of high-resolution samples) to the target resolution.

# Properties
- Quite expensive, since it multiplies the cost of [[Rasterization]] — and, under [[Per-Fragment Shading]], the cost of shading as well — by the supersampling factor.
- [[Multisample Antialiasing]] is an optimization that avoids the full cost of supersampling by decoupling the visibility sampling rate from the shading rate.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=193&annotation=J7ABNAD2)
