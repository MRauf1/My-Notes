---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Lambertian Shading)[^1]
> A [[Shading]] model, based on an observation of Lambert, stating that the illumination a surface receives from a light source is proportional to the cosine of the angle $\theta$ between the surface [[Normal Vector|normal]] $\mathbf{n}$ and the light direction $\mathbf{l}$:
> $$
> \begin{align}
> L = k_d I \max(0, \mathbf{n} \cdot \mathbf{l})
> \end{align}
> $$
> where $L$ is the pixel color, $k_d$ is the diffuse coefficient (surface color), and $I$ is the light source intensity.

![[Lambertian Shading.png]]

# Properties
- Since $\mathbf{n}$ and $\mathbf{l}$ are [[Unit Vector|unit vectors]], their [[Dot Product]] $\mathbf{n} \cdot \mathbf{l}$ directly gives $\cos\theta$.
- A surface facing directly toward the light receives maximum illumination; a surface tangent to or facing away from the light direction receives none.
- View-independent: the shaded color does not depend on the view direction $\mathbf{v}$, unlike [[Blinn-Phong Shading]], which adds a view-dependent specular highlight on top of this diffuse component.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=97&annotation=HUBEY4V2)
