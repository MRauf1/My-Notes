---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Density Map[^1]
> The output of a cryo-EM reconstruction: a voxel grid of the molecule's **electrostatic (Coulomb) potential** $V(x)$, relative to the mean potential of the surrounding ice. It is not a probability density. The name comes from X-ray crystallography, whose maps show electron density. The potential is fixed by the net charge density through [[Poisson Equation|Poisson's equation]] (see [[Electric Potential]]):
> $$
> \begin{align}
> -\nabla^2 V = \frac{e\,(\rho_{\text{nuc}} - \rho_e)}{\varepsilon_0} \quad\Longleftrightarrow\quad \hat V(k) = \frac{e\,\big(\hat\rho_{\text{nuc}}(k) - \hat\rho_e(k)\big)}{\varepsilon_0\, |2\pi k|^2},
> \end{align}
> $$
> where $\rho_{\text{nuc}}$ is the nuclear charge density (in units of $e$) and $\rho_e$ the electron density.

**"Density" does not mean probability density.** The map is a physical scalar field in volts (up to an unknown scale), not a distribution over space. It is called a density because it plays the role of the electron-density maps of X-ray crystallography: large where there is matter, and displayed as an isosurface at a chosen threshold. It need not be nonnegative and need not integrate to $1$.

# Properties
- **Electrons vs. X-rays.** X-rays scatter off electrons and image $\rho_e$. Electrons scatter off the potential, i.e. off nuclei and electrons together. Per atom, this relation is the Mott–Bethe formula: the electron scattering factor is $\propto (Z - f_X(k))/k^2$.
- **The potential is a smoothed version of the net charge.** The $1/|k|^2$ factor is a low-pass filter, so each atom gives a smooth positive peak, and $V$ resembles a blurred atom density.
- **Net charge is visible.** Negatively charged groups can appear weaker than in electron-density maps.
- **Scale is arbitrary and values can be negative.** Maps are normalized and contoured in units of their standard deviation. Contrast exists only relative to the ice, so the solvent averages to zero.
- **Probability enters only through averaging.** Each atom's contribution is convolved with the distribution of its displacement over copies and thermal motion (the B-factor of the [[Atomic Model]]).
- **Treating the map as a measure is a modelling choice.** Some methods clip a map to be nonnegative and normalize it into a probability measure, so that optimal transport or Gaussian-mixture fitting applies. That is not what the map physically is.
- Its reliable detail is quantified by its [[Resolution (Cryo-EM)|resolution]]. Images of it are projections ([[Projection Approximation]]).
- The map can be parameterized in several ways ([[Cryo-EM Volume Representations]]).

# Questions
> [!question]- Why does a cryo-EM map look like an electron-density map, even though it images the potential?
> By Poisson's equation, $\hat V(k) \propto (\hat\rho_{\text{nuc}} - \hat\rho_e)/|k|^2$: the potential is the net charge density passed through the low-pass Coulomb kernel $1/(4\pi\varepsilon_0|x|)$. Each nucleus is only partially screened by its own electrons, so every atom contributes a smooth positive peak at its position, as in an electron-density map. The two differ where net charge matters: ionized groups change $V$ but barely change $\rho_e$.

> [!question]- Where, if anywhere, does a genuine probability density appear in a cryo-EM map?
> In the blurring of each atom: the reconstruction averages over copies and thermal motion, so each atom's potential is convolved with the probability density of its displacement, $V(x) \approx \sum_a (\varphi_{Z_a} * G_{B_a})(x - r_a)$, where $G_{B_a}$ is that density (Gaussian, width set by the B-factor). The map as a whole is not a probability density.

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
