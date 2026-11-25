---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Specimen and Field[^1]
> A **cryo-EM specimen** is a thin slab of vitreous (non-crystalline) ice, produced by [[Vitrification]], from tens of nm (purified samples) to $100$–$300$ nm (cells) thick, holding many copies of a [[Macromolecule|macromolecule]] together with everything else in that volume. It is made by freezing a purified sample, or a cell (often thinned into a lamella by focused-ion-beam milling), fast enough that the water does not crystallize. A **field** is one region of the specimen that the microscope images at once.

The specimen is not one isolated molecule. The whole slab is imaged, and in [[Cryo-Electron Tomography]] it is the whole slab that gets tilted.

# Properties
- Copies freeze in essentially random orientations and positions, so each has its own unknown [[Particle Pose]].
- **Two kinds of specimen.** For [[Single-Particle Analysis]], the ice is made as thin as possible (barely thicker than the particle), the sample is purified, and thousands of fields are each imaged once. For [[Cryo-Electron Tomography]], the specimen is often a cell or a lamella, $100$–$300$ nm thick, and a few fields are each imaged at many tilts.
- The slab geometry (thin in $z$, wide in $x, y$) is what limits the [[Tilt Series|tilt range]]: the beam's path through the ice grows like $d/\cos\theta$.

[^1]: [Cryogenic electron tomography (Wikipedia)](https://en.wikipedia.org/wiki/Cryogenic_electron_tomography)
