---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-Electron Tomography (Cryo-ET)[^1]
> The approach to [[Cryo-Electron Microscopy|cryo-EM]] in which a [[Tilt Series]] of one field of a frozen specimen is inverted into a 3D [[Tomogram]]. Copies of a [[Macromolecule|macromolecule]] are then cut out of the tomogram as [[Subtomogram|subtomograms]] and combined by [[Subtomogram Averaging]] into a 3D structure.

# Properties
- **Poses are random and unknown**, as in [[Single-Particle Analysis]]. Because each copy is seen at many known relative orientations $R_\theta R_i$, it can be reconstructed without knowing $R_i$. The pose is needed only to align copies for averaging (3D–3D registration). The tomogram lives in the specimen frame, the average in the molecule frame ([[Cryo-EM Reference Frames]]).
- It sees molecules **in situ**, in their native cellular context, including one-off objects that cannot be averaged. For those, the [[Missing Wedge]] remains.
- The tomogram is noisy and has a [[Missing Wedge]]; averaging over many copies at diverse poses addresses both.
- **Lower resolution than [[Single-Particle Analysis]]**, mainly because of dose splitting, thick and crowded specimens, fewer particles, tilt-geometry errors and in-situ heterogeneity, rather than the wedge.
- **Modern refinement** fits each particle's 2D tilt images directly, at poses $R_\theta R_i$ with $R_\theta$ known, instead of aligning wedge-corrupted subtomograms. It also models per-tilt deformation and optics. This has reached residue-level resolution in cells, e.g. a ribosome–antibiotic complex at 3.5 Å inside intact bacteria[^2].

[^1]: [Cryogenic electron tomography (Wikipedia)](https://en.wikipedia.org/wiki/Cryogenic_electron_tomography)
[^2]: [Tegunov, Xue, Dienemann, Cramer & Mahamid (2021), Multi-particle cryo-EM refinement with M visualizes ribosome-antibiotic complex at 3.5 Å in cells](https://www.nature.com/articles/s41592-020-01054-7)
