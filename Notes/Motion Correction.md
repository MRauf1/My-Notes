---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Motion Correction[^1]
> Direct electron detectors (DED) record each exposure as a movie. Motion correction is the translational alignment and averaging of the movie frames, to undo [[Beam-Induced Motion]]:
> - **Global**: estimate the relative shift of every pair of frames, then solve a least-squares problem for per-frame shifts.
> - **Local**: cross-correlate small patches, and fit a velocity field assumed smooth in position and time (local low-degree polynomials). Then align and average.
> - **Dose weighting**: weight each frame's frequencies by how much signal survives [[Radiation Damage]] at that accumulated dose.

# Properties
- Motion-corrected images have a smaller B-factor, Thon rings to higher frequency ([[CTF Estimation]]) and better contrast.
- **The "Resolution Revolution".** DEDs with motion correction first gave 3–4 Å structures, then about 1.5 Å by 2020. Single-particle cryo-EM has since reached 1.2 Å on apoferritin, at which individual atoms are resolved[^2].
- Per-particle motion correction tracks the motion of individual particles.
- **MotionCor2** models the motion as a smooth, block-based deformation: patch shifts from cross-correlation, fitted by a polynomial that is quadratic in space and cubic in time. Motion correction is a registration problem whose main difficulty is the noise.[^3]

[^1]: [Singer and Sigworth, 2020, p. 9](zotero://open-pdf/library/items/FKVQSKD6?page=9&annotation=KHYMN85E)
[^2]: [Nakane et al. (2020), Single-particle cryo-EM at atomic resolution, Nature 587:152–156](https://www.nature.com/articles/s41586-020-2829-0)
[^3]: [Bendory et al., 2020, p. 16](zotero://open-pdf/library/items/N4ZIHINK?page=16&annotation=LLP52DGB)
