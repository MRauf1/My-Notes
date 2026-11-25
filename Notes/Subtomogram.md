---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Subtomogram[^1]
> A small 3D box $v_i$ cut out of a [[Tomogram]] around one copy (particle) of a [[Macromolecule|macromolecule]]. Particles are located by *particle picking*, e.g. template matching against a reference.

# Properties
- It inherits the tomogram's noise and [[Missing Wedge]] $W$. In the frame of copy $i$, whose orientation is $R_i$ ([[Particle Pose]]), the wedge is $R_i^{\top} W$.
- One copy alone is too noisy and too wedge-corrupted to interpret; many are combined by [[Subtomogram Averaging]].

[^1]: [Cryogenic electron tomography (Wikipedia)](https://en.wikipedia.org/wiki/Cryogenic_electron_tomography)
