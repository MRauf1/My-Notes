---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Texture Mapping)[^1]
> Replacing a value used in a [[Shading]] computation (e.g., the diffuse color) with a value read from a texture — an image used to add surface detail — at a texture coordinate, rather than using the primitive's own attribute value directly. The lookup operation is called a texture lookup.

# Properties
- The texture coordinate is itself commonly stored as a per-vertex attribute, interpolated across the primitive like any other via [[Gouraud Interpolation]], so every point on a primitive knows where it lives in the texture.
- Added to make shaded surfaces look less homogeneous and artificial than they would using only per-vertex or per-primitive attribute values.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=191&annotation=SWU6GN7Q)
