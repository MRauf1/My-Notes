---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Lambertian Reflectance Model)[^1]
> A simplified [[Bidirectional Reflectance Distribution Function (BRDF)|BRDF]], $F_L$, describing purely diffuse reflection. The outgoing light power $\ell_{out}$ is a function only of the surface orientation relative to the incoming ray direction, a scalar surface reflectance, and the incoming light power, but not of the outgoing direction $\mathbf{q}$:
> $$
> \begin{align}
> \ell_{out} = F_L(\ell_{in}(\lambda), \mathbf{n}, \mathbf{p}) = a\, \ell_{in}(\lambda)\, (\mathbf{n} \cdot \mathbf{p})
> \end{align}
> $$
> where $a$ is the surface **reflectance**, or **albedo**, $\mathbf{n}$ is the surface normal vector, and $\mathbf{p}$ points toward the source of the incident light.

# Properties
- Because $\ell_{out}$ does not depend on the outgoing direction $\mathbf{q}$, a Lambertian surface reflects light equally in every outgoing direction, for a fixed incoming light direction $\mathbf{p}$.
- Integrating this expression over all incoming directions $\mathbf{p}$ gives the total intensity reflecting off a Lambertian surface, $\ell_{out} = \int_{\mathbf{p}} a\,\ell_{in}(\mathbf{p}) \cos(\mathbf{n} \cdot \mathbf{p})\, d\mathbf{p}$; this integrated brightness carries very little information about the incoming light $\ell_{in}(\mathbf{p})$ from any particular direction, which is why a [[Pinhole Camera|camera]] is needed to form an image and recover directional information.
- Analogous to [[Lambertian Shading]] in computer graphics, $L = k_d I \max(0, \mathbf{n} \cdot \mathbf{l})$, which additionally clamps negative orientations to zero and denotes the light direction and diffuse coefficient by $\mathbf{l}$ and $k_d$ in place of $\mathbf{p}$ and $a$.
- The integral of this cosine-weighted reflection over a visible surface underlies the [[Corner Camera]], which relates a hidden scene's radiance to intensity variations observed on a nearby visible surface.
- Extended to a wavelength-dependent [[Reflectance Spectrum]], $r(\lambda) = k\,\ell_{in}(\lambda)\,s(\lambda)$, when modeling how diffuse reflection alters the [[Power Spectrum]], and hence color appearance, of the incident light.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
