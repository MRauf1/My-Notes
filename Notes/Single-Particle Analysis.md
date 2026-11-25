---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Single-Particle Analysis (SPA, Single-Particle Reconstruction)[^1]
> The approach to [[Cryo-Electron Microscopy|cryo-EM]] in which a purified specimen containing many copies of a [[Macromolecule|macromolecule]], frozen in random orientations, is imaged **without tilting**: each field gets one image carrying the full electron dose. Each copy (particle) contributes one 2D projection ([[Projection Approximation]]) at an unknown [[Particle Pose]],
> $$
> \begin{align}
> I_i = S_{t_i}\, P_{e_z}\big(R_i^{-1} \cdot f\big) + \varepsilon_i, \qquad R_i \in SO(3),\ t_i \in \mathbb{R}^2,
> \end{align}
> $$
> where $S_{t_i}$ is an in-plane shift. The 3D structure $f$ is reconstructed by estimating the poses and filling Fourier space with the corresponding central slices $R_i^{\top} e_z^{\perp}$ ([[Fourier Slice Theorem]]).

**Many fields, each imaged once.** A session moves across thousands of fields of one or a few grids and takes one $0^\circ$ image per field, collecting about $10^5$–$10^6$ particle images. The diversity of viewing directions comes from the particles themselves: each froze in its own orientation $R_i$. In [[Cryo-Electron Tomography]], by contrast, the slab is rotated so that the same copies are seen from many known directions.

# Types
Subproblems of SPA:
- [[Ab Initio Reconstruction]]: a first 3D structure without a starting model.
- [[2D Classification]]: grouping and averaging particle images by view.
- Refinement: maximum likelihood / MAP over $f$ with poses marginalized, using the [[Expectation-Maximization Algorithm]].
- [[Conformational Heterogeneity]]: when the copies differ.

# Properties
- **Only 5 pose parameters per particle are observable**: 3 angles and 2 in-plane shifts. A shift along the beam is integrated away by the projection.
- **No missing wedge**: random $R_i$ scatter the central slices in all directions. The failure mode is [[Preferred Orientation]].
- **Handedness is not identifiable** from the images alone ([[Handedness Ambiguity]]).
- **Comparison with [[Cryo-Electron Tomography]].** In both, copies sit at random, unknown poses $R_i$.
  - *Cryo-ET* sees each copy at many known relative orientations $R_\theta R_i$. Each copy can therefore be reconstructed without $R_i$, and the pose is only needed to align copies for averaging (3D–3D registration).
  - *SPA* sees each copy once, at $R_i$ alone. Its pose is needed before its image can be used at all (2D–3D registration).
  - SPA has no specimen-frame reconstruction and works directly in the molecule frame ([[Cryo-EM Reference Frames]]).
- **Why SPA usually reaches higher resolution than [[Subtomogram Averaging]].** The [[Missing Wedge]] is not the main reason, since averaging over diverse poses fills it. The reasons are:
  1. **Dose per image.** One image carries the whole dose, which is recorded as a movie, motion-corrected and dose-weighted. A tilt series splits the dose over about 40 images, each too noisy for precise alignment, and the later ones are already radiation-damaged.
  2. **Thin ice.** SPA ice is barely thicker than the particle, so the beam path is short and there is no cellular crowding. Cryo-ET specimens are $100$–$300$ nm thick, grow like $d/\cos\theta$ with tilt, and have a defocus gradient across each tilted image.
  3. **Particle count.** The number of particles needed grows exponentially in $1/d^2$ ([[Rosenthal–Henderson Relation]]). SPA collects $10^5$–$10^6$ particles; cryo-ET typically $10^3$–$10^4$, each with a larger B-factor.
  4. **Geometric precision.** Cryo-ET needs every tilt image's geometry to be correct to about an ångström.
  5. **Heterogeneity in situ.** Copies in cells vary more, which splits the data further.
- The steps are organized in the [[Cryo-EM Processing Pipeline]]. The full forward model, with CTF and shifts, is the [[Cryo-EM Image Formation Model]]. With known poses, reconstruction is linear ([[Tomographic Reconstruction]]); the unknown poses make it nonlinear.
- Electrons cause far less [[Radiation Damage]] per useful scattering event than X-rays. Typically $10^5$–$10^6$ particle images give near-atomic resolution, and in principle about $10^4$ suffice.
- **The simplest version of the problem** is to recover a structure from noise-free projections at unknown viewing directions. In practice they are also very noisy, shifted and CTF-filtered.[^2]

![[Cryo-EM Simulated Projections.png]]

# Questions
> [!question]- Why does SPA have no missing wedge, and when does it get an analogous gap?
> Each particle image gives the central plane $R_i^{\top} e_z^{\perp}$. With the $R_i$ spread over $SO(3)$, the plane normals $R_i^{\top} e_z$ cover the sphere, so every frequency lies on some measured plane. There is no shared hinge, as there is in a single-axis tilt series. A gap appears when the normals cluster ([[Preferred Orientation]]): frequencies whose direction lies near the missing normals' great circles are poorly sampled, and resolution becomes anisotropic.

> [!question]- Connection: What does a crystal do in X-ray crystallography that SPA does computationally, and where does the analogy break?
> A crystal **averages** a huge number of identical copies physically: on a lattice with a common orientation, their scattered waves add coherently into Bragg peaks, so one copy's signal is amplified without any alignment. SPA averages $10^5$–$10^6$ isolated copies computationally, after estimating each copy's pose. The dictionary:
> - the lattice (known, identical poses) corresponds to the estimated poses $g_i$;
> - coherent summation corresponds to averaging aligned images;
> - rotating the crystal during data collection corresponds to the random $R_i$ supplied by freezing.
>
> **Where it breaks:** a crystal needs identical copies fixed in a lattice, so heterogeneity is averaged away or prevents crystallization (hard for membrane proteins). In SPA, heterogeneity is visible and can be modelled.

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
[^2]: [Bendory et al., 2020, p. 35](zotero://open-pdf/library/items/N4ZIHINK?page=35&annotation=JWNAD8ED)
