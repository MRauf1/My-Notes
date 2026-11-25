---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Preferred Orientation[^1]
> The distribution of [[Particle Pose|particle orientations]] $R_i$ in a specimen is far from uniform on $SO(3)$, e.g. because particles adsorb to the air–water interface in only a few ways, or membrane proteins sit in a membrane parallel to the slab. The measured central slices then cluster in Fourier space ([[Fourier Slice Theorem]]).

# Properties
- **In [[Single-Particle Analysis]]**, the slices miss some directions, giving anisotropic resolution (a gap analogous to the [[Missing Wedge]]).
- **In [[Subtomogram Averaging]]**, the copies' rotated wedges $R_i^{\top} W$ coincide and fail to fill each other in.
- **In [[Conformational Heterogeneity]]**, it can bias estimated state populations when the difference between states lies in poorly sampled slices.
- **Causes and remedies.** Proteins adsorb to the [[Air–Water Interface]] or the support film with one face. Surfactants or pH changes can help. Tilted-specimen collection widens the views but worsens [[Beam-Induced Motion]], whose largest component is normal to the specimen.
- **Computational correction (2024).** spIsoNet corrects anisotropy and particle misalignment by self-supervised learning, without extra sample preparation[^2].

[^1]: [Naydenova & Russo (2017), Measuring the effects of particle orientation to improve the efficiency of electron cryomicroscopy](https://www.nature.com/articles/s41467-017-00782-3)
[^2]: [Overcoming the preferred-orientation problem in cryo-EM with self-supervised deep learning (Nature Methods 2024)](https://www.nature.com/articles/s41592-024-02505-1)
