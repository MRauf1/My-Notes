---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition (Alpha Channel)[^1]
> An alpha channel is a fourth channel added to an RGB image storing the coverage value $\alpha$ for each pixel, making the image an RGBA image; with 8-bit channels, each pixel then takes up 32 bits.

# Properties
- If instead stored as a separate grayscale image, the same per-pixel $\alpha$ values are called an alpha mask or transparency mask.
- Used to compute [[Alpha Compositing]] of a foreground layer over a background layer.
- Extends [[24-bit Color]] (24 bits) to 32 bits per pixel—a conveniently sized chunk in many computer architectures.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=68&annotation=6QKT4SFD)
