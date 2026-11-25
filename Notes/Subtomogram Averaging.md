---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Subtomogram Averaging[^1]
> Estimation of one shared 3D structure $f$ from $N$ [[Subtomogram|subtomograms]] under the model
> $$
> \begin{align}
> v_i = g_i \cdot \big(M_i f\big) + \varepsilon_i, \qquad g_i = (R_i, t_i) \in SE(3),
> \end{align}
> $$
> where $g_i$ is the unknown [[Particle Pose]] and $M_i$ is the projector (in Fourier space) onto the frequencies that copy $i$ actually measured, i.e. outside its rotated [[Missing Wedge]] $R_i^{\top} W$. It alternates between estimating the poses (alignment against the current reference) and averaging the aligned copies, at each frequency only over the copies that measured it.

# Properties
- **Noise reduction.** Averaging $N$ aligned copies shrinks the noise like $1/\sqrt{N}$.
- **Fills the missing wedge.** The copies point in different directions, so their wedges $R_i^{\top} W$ do too. Almost every frequency is then measured by many copies, which also removes the anisotropy.
- **Assumes homogeneity.** There is one shared $f$. If the copies differ, the average blurs toward a mean structure ([[Conformational Heterogeneity]]).

# Questions
> [!question]- Under what condition on the poses does averaging recover every frequency, and when does it fail?
> A frequency $k$ is recovered if $k \notin R_i^{\top} W$ for enough copies $i$, i.e. if the orientations $\{R_i\}$ are diverse enough that the rotated wedges do not all contain $k$. It fails under **[[Preferred Orientation|preferred orientation]]**: if all copies share nearly the same $R_i$ (e.g. membrane proteins in a membrane parallel to the slab), the rotated wedges coincide and the wedge stays missing however large $N$ is.

> [!question]- Why must the alignment score be wedge-aware?
> Two subtomograms whose copies have similar $R_i$ share similar wedge artifacts: the same elongation and streaks. A plain cross-correlation over all frequencies rewards matching those artifacts, so copies get aligned, or classified, by their wedge (i.e. by orientation) rather than by the molecule. Restricting the correlation to frequencies measured by both, $M_i M_j$, removes this bias.

[^1]: [Cryogenic electron tomography (Wikipedia)](https://en.wikipedia.org/wiki/Cryogenic_electron_tomography)
