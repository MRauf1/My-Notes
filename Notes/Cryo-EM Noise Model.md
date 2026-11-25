---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Noise Model[^1]
> At the level of individual movie frames, the dominant noise is **shot noise**, which is [[Poisson Distribution|Poisson]]. After frames are averaged into micrographs, the noise is modelled as **Gaussian**, with a non-white but **radially symmetric** power spectrum. Its spectral shape comes from inelastic scattering, ice-thickness variation and the PSF. The spectrum is estimated during reconstruction, or from micrograph regions without particles.

# Properties
- **SNR** is usually well below $0$ dB and can be as low as $-20$ dB, i.e. noise power $100\times$ the signal power. Two causes: low dose, to limit [[Radiation Damage]], and low contrast, since there is no heavy-metal stain.
- All current algorithms rely, explicitly or implicitly, on the Gaussian assumption ([[Cryo-EM Maximum Likelihood Reconstruction]]).
- At this SNR, alignment, detection and clustering all become hard ([[Multi-Reference Alignment]], [[Particle Picking]]).

[^1]: [Bendory et al., 2020, p. 5](zotero://open-pdf/library/items/N4ZIHINK?page=5&annotation=CER5BGEN)
