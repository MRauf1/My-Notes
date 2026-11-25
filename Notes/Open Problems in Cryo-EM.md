---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Open Problems in Cryo-EM[^1]
> Limitations of current [[Cryo-EM Processing Pipeline|cryo-EM methods]] that have research potential. Each one is stated as in the 2020 review and re-checked against the literature as of November 2026.

# Properties
**Heterogeneity**
- **Continuous heterogeneity ("3D movies") — still open.** In 2020 this was the main computational challenge: discrete classification works for small $K$, while continua and highly similar states were an "elusive unfulfilled promise". Benchmarks such as CryoBench (NeurIPS 2024) were built precisely because the methods disagree and are hard to evaluate[^2]. See [[Conformational Heterogeneity]].
- **Manual, irreproducible classification — still open.** Hierarchical [[3D Classification]] relies on manual tweaking, and quality degrades and cost grows linearly in $K$.
- **High-resolution covariance — partly open.** The full covariance has $O(L^6)$ entries and needs complete view coverage, so it is estimated only at low resolution ([[Cryo-EM Covariance Estimation]]).
- **Manifold methods: stitching across viewing directions — still open.** Diffusion-map embeddings per viewing direction (ManifoldEM) are hard to stitch into one 3D landscape. Ground-truth studies report physically impossible, stunted or hybrid motions[^3].
- **Physical deformation priors — open.** Normal-mode analysis rests on a harmonic approximation that is questionable for large deformations. Pseudo-atomic deformation models conserve mass by design, so they cannot capture compositional change[^4].
- **Rigid-body and multi-body models** fail at domain interfaces and cannot capture non-rigid motion.

**Inference and uncertainty**
- **Posterior and uncertainty quantification — still largely open.** Maps are MAP point estimates ([[MAP Refinement (Cryo-EM)]]), and MCMC is not standard practice. Recent steps: simulation-based inference of per-image conformations against a template ensemble (cryoSBI, PNAS 2025)[^5], log-likelihood Hessian sensitivity analysis (2024)[^6], and diffusion priors for Bayesian 3D reconstruction from incomplete measurements[^7]. Calibrated uncertainty for full maps remains unsolved.
- **Computational cost — partly addressed.** ML-EM scales as $O(nL^4\log L)$. Grid-free representations (Gaussian mixtures, splatting, neural fields) and amortized pose inference are active directions ([[Cryo-EM Volume Representations]]).
- **Validation, confidence intervals and model bias — ongoing.** There is no agreed computational standard; half-map FSC can be fooled by correlated refinement errors ([[Cryo-EM Validation]]). Masks reused from the same data are an inverse crime ([[Cryo-EM Masking]]), and template bias persists ([[Einstein from Noise]], 2025 work on confirmation bias in picking[^8]).

**Data and imaging**
- **Particle picking — still open.** Small proteins, complete view coverage, and the lack of labelled datasets remain the main problems (2025 review)[^9]. Reconstruction directly from micrographs, or from all movie frames, avoids picking: EM directly from micrographs (2023)[^10], picking in all frames (2025). See [[Particle Picking]].
- **Small particles — partly addressed.** The 2020 limit was about $40$ kDa. It is now about $38$ kDa without a scaffold (2026), and $14$ kDa with nanobody scaffolds (2025). Scaffold-free sub-40 kDa targets are still at the edge.
- **Preferred orientation — partly addressed.** The computational correction spIsoNet (Nature Methods 2024) recovers under-sampled views by self-supervised learning[^11]. Sample-side causes remain ([[Preferred Orientation]], [[Air–Water Interface]]).
- **Beam-induced motion in the first frames — still open.** The early "burst phase" is too fast to correct and destroys the least-damaged signal. It is considered a primary resolution limit[^12] ([[Beam-Induced Motion]]).
- **In situ single-particle imaging — emerging.** 2D template matching locates and classifies complexes in images of cells (Grigorieff lab, 2023–2024)[^13]. Crowding and background noise still limit it to large, abundant targets.
- **Automated, objective outlier rejection — open (not re-checked).** Particles that are rejected may be genuine alternative states.

**Theory** (the 2020 open questions from Bendory et al.[^14] and their status in 2026)
- **Sample complexity of the full cryo-EM problem — still open.** Known: for the idealized model (perfect picking, no CTF), $\sigma^6$ samples for uniform rotations and $\sigma^4$ for non-uniform ones ([[Orbit Recovery Sample Complexity]]). Recent progress: a provable second-moment algorithm for non-uniform rotations (2026)[^15]; a provable method of moments for cryo-EM (2026)[^16]; orbit recovery under the full rigid-motion group, i.e. with shifts (2025)[^17]; group-invariant moments under tomographic projections (2026)[^18]. Still missing: rates with CTF, imperfect picking, heterogeneity and finite target resolution, i.e. "how many particles for resolution $d$ at a given SNR".
- **Information–computation gaps — open, increasingly studied.** Enough information (sample complexity) does not imply an efficient algorithm. For example, the second moment may suffice information-theoretically for non-uniform rotations while being hard computationally. Gaps have been conjectured for super-resolution MRA and observed empirically in MRA and MTD variants. Recent work on projected MRA and weak-signal latent-variable models (2026) pushes this further[^19]. A gap for the cryo-EM setting itself is not established.
- **Guarantees for the algorithms actually used — largely open.** The behaviour of ML-EM, SGD and the method of moments on the cryo-EM likelihood is not well understood. A first step is the analysis of maximum likelihood in the high-noise orbit model (Annals of Statistics, 2024). Convergence and landscape results for the full non-convex problem are lacking ([[Iterative Refinement (Cryo-EM)]]).
- **Multi-target detection and picking-free reconstruction — partly addressed.** Reconstruction directly from simulated micrographs has been demonstrated, and MTD sample complexity studied (2025)[^20]. A full analysis, and success on experimental data, remain open ([[Multi-Target Detection]]). This is the theoretical route around the particle-size limit.
- **Priors from biological knowledge — partly addressed.** Convenience priors (Gaussian Fourier, Poisson voxels) were the 2020 norm. Learned generative priors over maps now exist (CryoFM, ICLR 2025)[^21], but their bias and their effect on validation are not characterized ([[MAP Refinement (Cryo-EM)]]).
- **Deep learning at low SNR — open in theory.** In 2020, deep learning had limited impact on 3D reconstruction and heterogeneity, because of noise and model bias from supervised training. It is now widespread (picking, heterogeneity, priors). But no network can beat the information-theoretic rate $1/\mathrm{SNR}^q$, and when learned methods are provably near-optimal at low SNR is unknown. A related empirical finding: cryo-EM image sets lie near low-dimensional manifolds (PRX Life, 2025)[^22].
- **Bias of the forward-model approximations — open (not checked).** The projection and weak-phase approximations introduce a bias that does not average out with $N$. Bounds on that bias in the reconstructed map, as a function of particle size, resolution and $N$, appear not to be standard ([[Cryo-EM Forward Model]]).

[^1]: [Singer and Sigworth, 2020, p. 25](zotero://open-pdf/library/items/FKVQSKD6?page=25&annotation=33V8EBR8)
[^2]: [Jeon et al. (2024), CryoBench: Diverse and challenging datasets for the heterogeneity problem in cryo-EM, NeurIPS D&B](https://arxiv.org/abs/2408.05526)
[^3]: [Recovery of Conformational Continuum From Single-Particle Cryo-EM Images: Optimization of ManifoldEM Informed by Ground Truth (IEEE TCI 2022)](https://doi.org/10.1109/tci.2022.3174801)
[^4]: [Schwab et al. (2024), DynaMight, Nature Methods](https://www.nature.com/articles/s41592-024-02377-5)
[^5]: [Dingeldein et al. (2025), Amortized template matching of molecular conformations from cryoelectron microscopy images using simulation-based inference, PNAS 122(23)](https://www.pnas.org/doi/10.1073/pnas.2420158122)
[^6]: [Sensitivity Analysis of Cryo-Electron Microscopy Reconstructions via the Log-Likelihood Hessian (arXiv:2411.13263)](https://arxiv.org/abs/2411.13263)
[^7]: [Diffusion Priors for Bayesian 3D Reconstruction from Incomplete Measurements (arXiv:2412.14897)](https://arxiv.org/abs/2412.14897)
[^8]: [Structure from Noise: Confirmation Bias in Particle Picking in Structural Biology (arXiv:2507.03951)](https://arxiv.org/abs/2507.03951)
[^9]: [Artificial intelligence in cryo-EM protein particle picking: recent advances and remaining challenges (Brief. Bioinform. 2025)](https://academic.oup.com/bib/article/26/1/bbaf011/7958312)
[^10]: [Expectation-maximization for structure determination directly from cryo-EM micrographs (arXiv:2303.02157)](https://arxiv.org/abs/2303.02157)
[^11]: [Overcoming the preferred-orientation problem in cryo-EM with self-supervised deep learning (Nature Methods 2024)](https://www.nature.com/articles/s41592-024-02505-1)
[^12]: [Devitrification reduces beam-induced movement in cryo-EM (IUCrJ 2021)](https://journals.iucr.org/m/issues/2021/02/00/pw5016/index.html)
[^13]: [Lucas, Himes & Grigorieff (2023), Baited reconstruction with 2D template matching for high-resolution structure determination in vitro and in vivo without template bias, eLife](https://www.biorxiv.org/content/10.1101/2023.07.03.547552v2.full.pdf)
[^14]: [Bendory et al., 2020, p. 24](zotero://open-pdf/library/items/N4ZIHINK?page=24&annotation=CSRANFJZ)
[^15]: [Bendory, Edidin, Katz, Kreymer & Sharon (2026), Provable orbit recovery over SO(3) from the non-uniform second moment (arXiv:2602.20590)](https://arxiv.org/abs/2602.20590)
[^16]: [Provable method of moments for cryo-EM (arXiv:2610.17892)](https://arxiv.org/abs/2610.17892)
[^17]: [Orbit recovery under the rigid motions group (arXiv:2512.07405)](https://arxiv.org/abs/2512.07405)
[^18]: [Group-invariant moments under tomographic projections (arXiv:2604.08330)](https://arxiv.org/abs/2604.08330)
[^19]: [Projected multi-reference alignment (arXiv:2605.25533)](https://arxiv.org/abs/2605.25533); [Sample complexity of weak-signal latent-variable models (arXiv:2610.24770)](https://arxiv.org/abs/2610.24770)
[^20]: [A note on the sample complexity of multi-target detection (arXiv:2501.11980)](https://arxiv.org/abs/2501.11980)
[^21]: [Zhou, Li, Yuan & Gu (2025), CryoFM: A Flow-based Foundation Model for Cryo-EM Densities, ICLR](https://arxiv.org/abs/2410.08631)
[^22]: [Evans, Murad, Dingeldein, Cossio, Covino & Meila (2025), Cryo-EM images are intrinsically low dimensional, PRX Life 3:033025](https://doi.org/10.1103/txrb-fw3z)
