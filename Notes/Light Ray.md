---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Light Ray)[^1]
> An abstraction describing light radiation heading in a particular direction from a particular location in space. A light ray is specified by its position, direction, and intensity as a function of wavelength and polarization.

# Properties
- Visible [[Light]] is physically electromagnetic radiation, which exhibits wave effects such as [[Diffraction]]; the light ray abstraction ignores these diffraction effects, treating light as traveling along straight lines.
- A collection of light rays filling a region of space, indexed additionally by time, is described by the [[Plenoptic Function]].
- The power of a light ray reflected off a surface, given an incoming ray, is governed by the [[Bidirectional Reflectance Distribution Function (BRDF)|BRDF]] of that surface.
- Ignoring diffraction is part of the broader [[Geometric Optics]] approximation, under which light rays bend only at material interfaces according to laws such as [[Snell's Law]].

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
