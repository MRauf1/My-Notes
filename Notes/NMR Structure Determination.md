---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] NMR Structure Determination[^1]
> Protein structure determination by nuclear magnetic resonance:
> 1. In a strong magnetic field, nuclear magnetic dipoles are flipped to a higher-energy state by a radio-frequency field (hundreds of MHz).
> 2. As they decay, they excite nearby dipoles with a probability that depends on distance. Measuring this coupling estimates pairwise distances between atoms.
> 3. The 3D structure is computed from the local distance estimates.

# Properties
- It is limited to small proteins (fewer than about $200$ residues, about $50$ kDa), where the signals of individual residues can be told apart. Unlike crystallography, it works in physiological conditions (water solution at room temperature).
- Recovering a global structure from pairwise distances is a distance-geometry problem.
- Like [[X-Ray Crystallography]], it measures an ensemble of molecules rather than individual particles.

[^1]: [Singer and Sigworth, 2020, p. 4](zotero://open-pdf/library/items/FKVQSKD6?page=4&annotation=D69Y26R5)
