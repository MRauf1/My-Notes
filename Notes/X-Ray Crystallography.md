---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] X-Ray Crystallography[^1]
> Structure determination from a crystal of the [[Macromolecule|macromolecule]]: a highly ordered lattice of identical copies. Rotated in an X-ray beam (wavelength $\approx 1$ Å), the crystal produces diffraction spots. Their intensities are the squared magnitudes $|F_{hkl}|^2$ of the [[Fourier Series|Fourier-series]] coefficients of the electron density of one unit cell. Once the missing phases are determined by other means, the structure follows by inverting a discrete Fourier transform.

# Properties
- **The phase problem.** The intensities determine only $|F_{hkl}|$. Inverting $|F_{hkl}|^2$ gives the autocorrelation of the density (the Patterson function), not the density itself.
- **The bottleneck is purifying and crystallizing the sample**, which is extremely hard for membrane proteins. [[Single-Particle Analysis]] needs no crystal.
- **Averaging.** The crystal averages its copies physically, through coherent diffraction from the lattice. A minimal crystal holds about $10^8$ molecules, versus about $10^4$ particles needed in principle by cryo-EM ([[Radiation Damage]]).
- Cooling to cryogenic temperature reduces radiation damage, which also limits the X-ray dose.
- It images the electron density $\rho_e$, while cryo-EM images the potential ([[Cryo-EM Density Map]]). Like NMR, and unlike cryo-EM, it measures an ensemble average rather than individual particles ([[NMR Structure Determination]]).
- **Further weaknesses relative to cryo-EM.** Crystal contacts can alter the protein's structure away from its physiological conformation, and the beam aggregates all molecules at once, which hides structural variability. Cryo-EM records each particle separately.[^2]

[^1]: [Singer and Sigworth, 2020, p. 3](zotero://open-pdf/library/items/FKVQSKD6?page=3&annotation=LTJPKATV)
[^2]: [Bendory et al., 2020, p. 3](zotero://open-pdf/library/items/N4ZIHINK?page=3&annotation=KRCFXRRI)
