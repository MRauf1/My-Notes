---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Reflectance Spectrum)[^1]
> For diffuse surface reflection, a function $s(\lambda)$ of wavelength describing how a surface scales the [[Power Spectrum|power spectrum]] of incident light at each wavelength. The power spectrum of the reflected light, $r(\lambda)$, is the wavelength-by-wavelength product of the incident power spectrum $\ell_{in}(\lambda)$ and the reflectance spectrum, scaled by a proportionality constant $k$ that depends on the reflection geometry:
> $$
> \begin{align}
> r(\lambda) = k\, \ell_{in}(\lambda)\, s(\lambda)
> \end{align}
> $$

# Properties
- Extends the [[Lambertian Reflectance Model]] to describe wavelength-dependent, rather than scalar, surface reflectance.
- Characterizes most matte (diffuse) reflections; the general reflection of light from a surface, including specular components, is instead described by the [[Bidirectional Reflectance Distribution Function (BRDF)|BRDF]].
- The same wavelength-by-wavelength scaling also models the effect of an attenuating filter on transmitted light, in which case $s(\lambda)$ is called the filter's **transmittance spectrum**.

[^1]: [MIT Vision Book - Color](https://visionbook.mit.edu/color.html)
