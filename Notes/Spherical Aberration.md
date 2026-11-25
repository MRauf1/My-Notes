---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Spherical Aberration[^1]
> A lens defect in which rays (waves) arriving at the periphery of the lens, i.e. at high angles, are bent more strongly than they should be. The focal length effectively shortens for high-angle rays, which come from high spatial frequencies of the object. It is quantified by the coefficient $C_s$ (a length; about $2$ mm on typical cryo-EM objective lenses) and enters the [[Wave Aberration Function|wave aberration function]] as $+\tfrac{\pi}{2}C_s\lambda^3 f^4$.

The name comes from glass lenses with spherical rather than ideal curvature. Magnetic lenses have nothing spherical about them, but their peripheral over-focusing is modelled the same way.

# Properties
- Under underfocus, it effectively *reduces* the defocus for high-angle electrons ([[Defocus (Cryo-EM)]]).
- It matters only at high spatial frequency, around $3$–$4$ Å resolution.
- It is a different aberration from [[Chromatic Aberration|chromatic aberration]], which depends on wavelength (energy) rather than angle.

# Questions
> [!question]- Show that $C_s$ acts like a frequency-dependent reduction of defocus, and estimate where it starts to matter.
> $\chi(f) = -\pi\lambda\delta f^2 + \tfrac{\pi}{2}C_s\lambda^3 f^4 = -\pi\lambda f^2\big(\delta - \tfrac12 C_s\lambda^2 f^2\big)$. So the effective defocus is $\delta_{\text{eff}}(f) = \delta - \tfrac12 C_s\lambda^2 f^2$, which decreases with $f$. The term matters when $\tfrac{\pi}{2}C_s\lambda^3 f^4 \sim 1$, i.e. $f \sim (2/(\pi C_s\lambda^3))^{1/4}$. For $C_s = 2$ mm $= 2\times10^7$ Å and $\lambda = 0.0197$ Å (300 keV), $C_s\lambda^3 \approx 153$ Å, so $f \approx 0.25$ Å$^{-1}$, i.e. about $4$ Å resolution.

[^1]: [Sigworth, p. 7](zotero://open-pdf/library/items/PZX9RV5T?page=7&annotation=WBETE5PS)
