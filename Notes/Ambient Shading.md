---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Ambient Shading)[^1]
> A [[Shading]] term added to avoid rendering unlit surfaces as completely black, contributing a constant amount to the pixel color that depends only on the object hit and not on the surface geometry, as if the surface were illuminated equally by light from everywhere: $L = k_a I_a$, where $k_a$ is the surface's ambient coefficient (ambient color) and $I_a$ is the ambient light intensity.

# Properties
- A crude but useful heuristic approximation to indirect illumination from other surfaces, which a simple [[Shading]] model otherwise ignores entirely.
- Usually expressed as the product of a surface color and an ambient light color, allowing ambient contribution to be tuned per surface or globally; when in doubt, the ambient color is set equal to the diffuse color.
- Combines with [[Lambertian Shading]] and [[Blinn-Phong Shading]] to form the full local illumination model.
- Applied unconditionally, regardless of whether the point is in shadow, unlike the diffuse and specular terms, which a [[Shadow Ray]] can suppress.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=98&annotation=MXYW8TWV)
