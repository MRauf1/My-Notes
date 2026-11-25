---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Tomogram[^1]
> The 3D reconstruction (a voxel map $\hat f$ of the electrostatic potential) of an entire field of a [[Cryo-EM Specimen|specimen]], computed by inverting a [[Tilt Series]]. Each tilt fills one central plane of Fourier space ([[Fourier Slice Theorem]]). The inversion uses, for example, weighted back-projection or iterative methods (SIRT).

# Properties
- It contains **every** copy of the [[Macromolecule|macromolecule]] in the field, together with membranes and other material. Each copy is reconstructed individually, so no assumption is made that copies are identical.
- **Noisy**: the low total dose is split across all tilts.
- **Anisotropic**: unmeasured frequencies form the [[Missing Wedge]], so features are elongated along the beam axis and surfaces parallel to the slab vanish.
- Small boxes around individual copies are cut out as [[Subtomogram|subtomograms]].

[^1]: [Cryogenic electron tomography (Wikipedia)](https://en.wikipedia.org/wiki/Cryogenic_electron_tomography)
