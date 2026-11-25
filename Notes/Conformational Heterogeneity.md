---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Conformational Heterogeneity[^1]
> The copies of a [[Macromolecule|macromolecule]] in a specimen are not identical: copy $i$ has its own structure $f_i \sim \mathcal{P}$, drawn from a distribution over structures, and is observed at its own [[Particle Pose]] $g_i$. It is *compositional* if subunits or binding partners are present or absent, and *conformational* if the shape changes, either among discrete states or continuously.

**Where homogeneity is and isn't assumed.** Reconstructing a [[Tomogram]] treats the field as one object and assumes nothing about the copies; it only needs the frozen specimen not to change during the tilt series. [[Subtomogram Averaging]] and [[Single-Particle Analysis]] with one shared $f$ do assume homogeneity.

# Types
- [[3D Classification]]: discrete states, fitted as a mixture model.
- [[Cryo-EM Covariance Estimation]]: linear continuous variability, via principal modes.
- [[Neural Heterogeneous Reconstruction]]: nonlinear continuous variability via a learned latent space.
- Deformation models: each copy is a warped template (flow fields, normal modes, elastic networks, multi-body refinement of rigid domains).
- Manifold and spectral embedding of particles (diffusion maps, graph Laplacians on images).
- Pose-free distribution matching: a generator whose simulated projections match the image distribution (CryoGAN-type).
- Moment methods: image moments encode the mean and covariance of the ensemble ([[Kam's Method]]).
- Atomic models with structure-prediction priors, guided by the particle images.
- Population estimation: weights of states and per-particle posteriors, with uncertainty.

# Properties
- The split into homogeneous and heterogeneous methods is the same in [[Single-Particle Analysis]] and [[Cryo-Electron Tomography]]: heterogeneity is a property of the molecule population, not of the imaging geometry. Only the forward model changes (one projection at $R_i$ versus a tilt fan at $R_\theta R_i$). A second axis cuts across all types: poses fixed beforehand (from a homogeneous consensus refinement), estimated jointly, or avoided (pose-free).
- Under a homogeneous model, the reconstruction roughly estimates the mean $\mathbb{E}[f]$. Flexible regions are blurred, so resolution varies across the map (local resolution), and the poses are estimated against a reference that resembles no actual copy.
- **The missing wedge can masquerade as heterogeneity**: copies with similar orientations share wedge artifacts, so a naive classifier groups them by orientation rather than by conformation.
- **Pose and conformation are confounded.** A rigid rotation of one domain can be explained by $g_i$ or by $f_i$; identifiability needs a rigid part to anchor the pose.
- **Resolution–heterogeneity tradeoff.** More states or latent dimensions describe the variability better, but leave fewer effective copies per state.
- Turning state populations into free energies, $\Delta G = -k_B T \ln(p_1/p_2)$, assumes freezing preserved the equilibrium distribution, which is debated.
- **Status of continuous methods** (open problems in [[Open Problems in Cryo-EM]]):
    - Normal-mode analysis relies on a harmonic approximation that is questionable for large, complex deformations.
    - Diffusion-map methods per viewing direction assume known rotations and cannot yet be stitched reliably into one 3D landscape.
    - Multi-body refinement fails at domain interfaces and misses non-rigid motion.
    - Methods that infer heterogeneity jointly with the rotations (high-dimensional "3D movie" functions, deep networks such as [[Neural Heterogeneous Reconstruction]]) are the active frontier.
- Single-particle cryo-EM images individual particles, unlike [[X-Ray Crystallography]] and [[NMR Structure Determination]], which measure ensembles. That is why it can resolve mixtures at all.
- **Ill-posed without structure.** $N$ 2D images cannot determine $N$ 3D structures, so the distribution must be constrained: discrete (a few volumes) or continuous (a low-dimensional subspace, a manifold, or rigid domains moving relative to each other). The discrete model is easy to fit by EM but scales poorly in $K$ and ignores the correlations between states.[^2]

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
[^2]: [Bendory et al., 2020, p. 23](zotero://open-pdf/library/items/N4ZIHINK?page=23&annotation=R6WSEE68)
