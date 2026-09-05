---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Shading)[^1]
> The third stage of [[Ray Tracing]]: computing the pixel color at an intersection point by modeling how the surface reflects incoming light toward the camera, using the intersection point, surface [[Normal Vector|normal]], and light and surface properties.

# Properties
- Defined in terms of illumination from a point [[Light|light]] source, using three [[Unit Vector|unit]] vectors at the shading point: the light direction $\mathbf{l}$ (toward the light), the view direction $\mathbf{v}$ (toward the camera), and the surface normal $\mathbf{n}$.
- Shading equations are evaluated separately per color channel (e.g., red, green, blue).
- Component shading models include [[Lambertian Shading]] (diffuse), [[Blinn-Phong Shading]] (specular highlights), and [[Ambient Shading]], which are typically summed together into a single local illumination model.
- Extended with [[Shadow Ray|shadow rays]] to account for occlusion of the light source, and with [[Specular Reflection]] to account for mirror-like reflected light.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=97&annotation=HUBEY4V2)
