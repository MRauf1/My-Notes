---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition (Low Dynamic Range (LDR) Image)[^1]
> A low dynamic range (LDR) image stores pixel values over a fixed, bounded range using integers—for example, an 8-bit image has possible values $0, \tfrac{1}{255}, \tfrac{2}{255}, \dots, \tfrac{254}{255}, 1$.

# Properties
- Contrasted with [[High Dynamic Range Image|high dynamic range (HDR) images]], which use floating-point numbers to represent a wide range of values.
- The denominator $255$ (rather than $256$) is used so that $0$ and $1$ can be represented exactly.
- Real displays take quantized integer input, commonly in the range $0$–$255$ (8 bits), even when intensities are manipulated as floating-point values in $[0,1]$.
- A type of [[Dynamic Range (Image)|image dynamic range]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=68&annotation=6QKT4SFD)
