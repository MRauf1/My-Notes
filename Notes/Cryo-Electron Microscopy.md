---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-Electron Microscopy (Cryo-EM)[^1]
> Transmission electron microscopy of a [[Cryo-EM Specimen|specimen]] frozen in vitreous ice ([[Vitrification]]), used to determine the 3D structure of [[Macromolecule|macromolecules]]. Each recorded image is, to first order, a projection of the specimen's electrostatic potential ([[Projection Approximation]]), and the 3D structure is recovered computationally from many such projections.

# Types
- [[Cryo-Electron Tomography]]: one field is imaged at many known tilts; copies are then extracted and averaged.
- [[Single-Particle Analysis]]: one untilted image per field; each copy contributes a single projection at an unknown pose.

# Properties
- The electron dose must stay low, because the beam destroys the specimen. So every image has very low SNR, and structure is only recovered by combining many images or many copies of the molecule.
- Structure determination combines the [[Fourier Slice Theorem]] (what each image measures) with estimation of each copy's [[Particle Pose]].
- "Cryo" refers to [[Vitrification]], not crystallization. Unlike X-ray crystallography, no crystal is needed: copies are averaged computationally after pose estimation, rather than physically by a lattice.
- The two approaches differ in which frame the reconstruction lives in ([[Cryo-EM Reference Frames]]).
- Copies of a molecule need not be identical; handling that is the problem of [[Conformational Heterogeneity]].
- **Recognition.** *Nature Methods* named cryo-EM Method of the Year 2015, and the 2017 Nobel Prize in Chemistry went to three of its pioneers.[^2]
- **Three defining difficulties**:
    - very low SNR ([[Cryo-EM Noise Model]]);
    - missing data: unknown poses and locations ([[Multi-Reference Alignment]]);
    - massive datasets: several TB of movies, and $8\times10^6$ voxels for a $200^3$ map. Higher resolution compounds the problem, needing more parameters, more data and more computation.

[^1]: [Cryogenic electron microscopy (Wikipedia)](https://en.wikipedia.org/wiki/Cryogenic_electron_microscopy)
[^2]: [Bendory et al., 2020, p. 1](zotero://open-pdf/library/items/N4ZIHINK?page=1&annotation=23L6KV42)
