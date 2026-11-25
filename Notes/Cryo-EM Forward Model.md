---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Forward Model[^1]
> The map from the unknowns (structures, poses, microscope and specimen parameters) to the recorded data in single-particle cryo-EM. In its most general physical form:
> 1. **Specimen.** A vitreous-ice slab containing particles $j = 1, \dots, M$, each with structure $f_j \sim \mathcal{P}$ and full pose $g_j = (R_j, \mathbf{t}_j) \in SE(3)$ ([[Special Euclidean Group]]):
> $$
> \begin{align}
> V(\mathbf{r}) = V_{\text{ice}}(\mathbf{r}) + \sum_{j=1}^{M}(g_j\cdot f_j)(\mathbf{r}) + V_{\text{other}}(\mathbf{r}) + i\,V_{\text{abs}}(\mathbf{r}),
> \end{align}
> $$
>    where $iV_{\text{abs}}$ is an absorptive part for electrons lost to inelastic or high-angle scattering, and $V$ changes during exposure (motion, damage).
> 2. **Propagation.** The electron wave $\psi = e^{ikz}u$ obeys the paraxial (high-energy) [[Schrödinger Equation]]:
> $$
> \begin{align}
> \partial_z u = \frac{i}{2k}\nabla_\perp^2 u + i\sigma V u, \qquad u(z_{\text{top}}) = 1,
> \end{align}
> $$
>    which gives the exit wave $u_{\text{exit}}(x, y)$.
> 3. **Optics.** Each spatial frequency is phase-shifted by the lens and cut off by the aperture, $\psi_{\text{img}} = \mathcal{F}^{-1}\big[A(\mathbf{k})e^{-i\chi(\mathbf{k})}\mathcal{F}u_{\text{exit}}\big]$ ([[Wave Aberration Function]]). The intensity is averaged over the partially coherent source: $I = \mathbb{E}_{\text{source}}|\psi_{\text{img}}|^2$.
> 4. **Detection.** Movie frames $\tau = 1, \dots, T$ give Poisson counts per pixel, $N_{p,\tau} \sim \mathrm{Poisson}\big(D_\tau\,(\mathrm{MTF} * I_\tau)(p)\big)$ ([[Cryo-EM Noise Model]]).
>
> The inverse problem is to recover $\mathcal{P}$ (or a single map $\varphi$) with everything else treated as nuisance.

**Animation of the standard model.** Each term is applied in turn:
1. the molecule and the specimen;
2. the rotation $R_i$, and the projection as the exit-wave phase, which the detector cannot see in focus;
3. the Fourier view of each image as a central slice, SPR vs. cryo-ET;
4. the shift $S_{\mathbf{t}_i}$;
5. why defocus is needed, then the CTF $a_i h_i *$;
6. the noise $\varepsilon_i$;
7. the resulting dataset.

![[Cryo-EM Forward Model.mp4]]

**Where the forward model sits in the process.** Every stage after imaging is part of inverting this model:

| Stage | What happens | Notes |
|---|---|---|
| Sample | purify; apply a thin film to a grid; plunge-freeze | [[Vitrification]], [[Air–Water Interface]] |
| Imaging | parallel beam, defocused objective lens, low dose, movies | [[Phase Contrast Imaging]], [[Radiation Damage]] |
| Micrograph processing | align frames, estimate the CTF, find particles | [[Motion Correction]], [[CTF Estimation]], [[Particle Picking]] |
| Particle processing | 2D classes, initial model, refinement, heterogeneity | [[2D Classification]], [[Ab Initio Reconstruction]], [[Iterative Refinement (Cryo-EM)]], [[Conformational Heterogeneity]] |
| Interpretation | resolution, atomic model, validation | [[Fourier Shell Correlation]], [[Atomic Model]], [[Cryo-EM Validation]] |

**The standard model.** After approximations A1–A9 (below), particle image $i$ is
$$
\begin{align}
\underbrace{I_i}_{\text{particle image}} = \underbrace{a_i}_{\text{scale}}\; \underbrace{h_i}_{\text{PSF}} * \underbrace{S_{\mathbf{t}_i}}_{\text{2D shift}}\, \underbrace{P}_{\text{projection}}\big(\underbrace{R_i}_{\text{rotation}}\circ \underbrace{f_i}_{\text{structure}}\big) + \underbrace{\varepsilon_i}_{\text{noise}}, \qquad \hat h_i(\mathbf{k}) = \underbrace{\sin\big(\chi_i(\mathbf{k}) - \alpha\big)}_{\text{CTF oscillation}}\;\underbrace{e^{-B|\mathbf{k}|^2/4}}_{\text{envelope}},
\end{align}
$$
with
$$
\begin{align}
\chi_i(\mathbf{k}) = -\pi\lambda\,\delta_i(\mathbf{k})\,|\mathbf{k}|^2 + \tfrac{\pi}{2}C_s\lambda^3|\mathbf{k}|^4.
\end{align}
$$

| Term | Meaning |
|---|---|
| $I_i \in \mathbb{R}^{L\times L}$ | the $i$-th boxed particle image, normalized (mean subtracted) and sampled on the pixel grid |
| $a_i$ | per-image contrast scale; absorbs the interaction constant $\sigma$ (the weak-phase factor $2\sigma$), dose and normalization |
| $h_i$, $\hat h_i$ | point spread function of image $i$ and its Fourier transform, the [[Contrast Transfer Function]] |
| $\chi_i$ | [[Wave Aberration Function]]: lens phase at spatial frequency $\mathbf{k}$ |
| $\delta_i(\mathbf{k})$ | [[Defocus (Cryo-EM)\|defocus]] (underfocus positive), including astigmatism through its dependence on the direction of $\mathbf{k}$ |
| $\lambda$ | electron [[Wavelength\|wavelength]] (≈ 0.02 Å at 300 keV) |
| $C_s$ | [[Spherical Aberration\|spherical aberration]] coefficient (≈ 2 mm) |
| $\alpha$ | [[Amplitude Contrast\|amplitude-contrast]] angle (≈ 0.05–0.1) |
| $B$ | B-factor of the [[CTF Envelope Function\|envelope]]: partial coherence, residual motion, damage |
| $\mathbf{k}$ | 2D [[Spatial Frequency\|spatial frequency]] (Å$^{-1}$) |
| $*$ | 2D convolution |
| $S_{\mathbf{t}_i}$ | in-plane shift by $\mathbf{t}_i \in \mathbb{R}^2$ (particle off-centre in the box) |
| $P$ | projection along the beam, $Pf(x,y) = \int f(x,y,z)\,dz$ ([[Projection Approximation]]) |
| $R_i \in SO(3)$ | orientation of particle $i$; $(R\circ f)(\mathbf{r}) = f(R^{-1}\mathbf{r})$ ([[Particle Pose]]) |
| $f_i$ | 3D electrostatic potential of particle $i$ relative to ice ([[Cryo-EM Density Map]]); $f_i = \varphi$ if homogeneous |
| $\varepsilon_i$ | noise: Gaussian, zero mean, stationary, with radially symmetric spectrum $\mathrm{PSD}_b(|\mathbf{k}|)$; includes structural noise from ice and neighbours |

This is the [[Cryo-EM Image Formation Model]] with every component made explicit.

# Types
Variants of the standard model, by assumption:
- **Homogeneous**: $f_i = \varphi$. A [[Multi-Reference Alignment]] problem over $SO(3)\times\mathbb{R}^2$ ([[Cryo-EM Maximum Likelihood Reconstruction]]).
- **Known poses**: linear in $f$, so a CT-type least-squares problem ([[Tomographic Reconstruction]]).
- **Discrete heterogeneity**: $f_i = \varphi_{c_i}$ ([[3D Classification]]).
- **Linear continuous**: $f_i = \mu + \sum_m z_{im}u_m$ ([[Cryo-EM Covariance Estimation]]).
- **Deformation**: $f_i = \varphi\circ D_{z_i}^{-1}$ (mass-conserving).
- **Nonlinear latent**: $f_i = \mathrm{Dec}_\theta(z_i)$ ([[Neural Heterogeneous Reconstruction]]).
- **Pose distribution**: uniform vs. non-uniform $R_i$, which changes the sample complexity from $\sigma^6$ to $\sigma^4$ ([[Orbit Recovery Sample Complexity]]).
- **Micrograph level** (without A8): $\text{micrograph} = \sum_j h * S_{\mathbf{t}_j}P(R_j\circ f_j) + \varepsilon$ ([[Multi-Target Detection]]).
- **Tilt series**: views $R_\theta R_i$ with $R_\theta$ known ([[Cryo-Electron Tomography]], [[Subtomogram Averaging]]).

# Properties
- **The approximation hierarchy (A1–A9):**

| # | Approximation | Valid when | What is lost |
|---|---|---|---|
| A1 | Static specimen | motion corrected; dose weighting | residual motion and damage become blur ([[Motion Correction]], [[Beam-Induced Motion]]) |
| A2 | Projection: drop $\frac{i}{2k}\nabla_\perp^2u$ inside the specimen, so $u_{\text{exit}} = e^{i\sigma PV}$ | thickness $t \ll 2d^2/\lambda$ at resolution $d$ (≈ 400 Å at 2 Å, ≈ 230 Å at 1.5 Å; my estimate) | Ewald-sphere curvature: data really lie on curved surfaces, not central planes ([[Fourier Slice Theorem]]) |
| A3 | Weak phase: $e^{i\sigma PV} \approx 1 + i\sigma PV$ | projected phase small | multiple scattering and the $\lvert\text{scattered}\rvert^2$ term ([[Weak Phase Approximation]]). Per atom the phase is milliradians, but across a large particle relative to ice it can reach about $0.5$ rad (my estimate) |
| A4 | Linear intensity | as A3 | the image becomes linear in $V$: $I \approx 1 + 2\,h * \sigma PV$ |
| A5 | Coherence as a Gaussian envelope | linear regime, small spreads | exact partial-coherence integrals |
| A6 | Isoplanatic CTF | thin ice, small tilt | defocus gradients (partly restored per particle) |
| A7 | Gaussian, stationary, signal-independent noise | many counts per pixel; low contrast | Poisson statistics; structured background |
| A8 | Isolated, centred particles | picking works | overlaps, CTF-delocalized signal outside the box ([[Multi-Target Detection]] → [[Multi-Reference Alignment]]) |
| A9 | Discretization | band-limit below Nyquist | interpolation error ([[Cryo-EM Volume Representations]]) |

- **Why approximate** instead of using the full model:
  1. *Error budget*: per-image SNR is about $0.01$–$0.1$, and the dropped terms (second order in the phase) are far below the noise.
  2. *Tractability*: the full model needs a 3D wave propagation for every image × pose × iteration, while the linear model makes each projection one Fourier slice ([[Iterative Refinement (Cryo-EM)]]).
  3. *Identifiability*: the extra nuisance parameters of the full model cannot be estimated at this SNR, and adding them worsens the estimate of $\varphi$ ([[Neyman–Scott Problem]]).
  4. *Structure*: linearity in $f$ is what gives the Fourier slice theorem, common lines, the MRA/orbit-recovery theory and the method of moments.
  5. *Controlled*: A2–A4 are a first-order expansion with explicit remainders. Each can be restored when needed (Ewald-sphere correction, multislice, Poisson likelihood).
- **Caveat: modelling error is bias.** It does not shrink with the number of particles $N$, while noise falls like $1/\sqrt N$. So at large $N$ and $1$–$2$ Å resolution, A2–A4 become the limiting error. Keep an approximation while its bias is below the statistical error at the target resolution. Rigorous bounds on this bias inside reconstruction appear not to be standard ([[Open Problems in Cryo-EM]]).

# Questions
> [!question]- Why does dropping the Fresnel term inside the specimen turn images into projections, and when is that justified?
> Without $\frac{i}{2k}\nabla_\perp^2u$, the equation $\partial_z u = i\sigma Vu$ is solved pointwise in $(x,y)$: $u_{\text{exit}} = \exp\big(i\sigma\int V\,dz\big) = e^{i\sigma PV}$, so each image depends on $V$ only through its projection. The dropped term spreads the wave sideways over the thickness $t$. For detail of size $d$, the diffracted wave's phase lag over $t$ is about $\pi t\lambda/d^2$ (the same geometry as the CTF's defocus term). Neglecting it requires $t \ll d^2/\lambda$ up to a constant: thin specimens and moderate resolution. Equivalently, the Ewald sphere is flat enough over the frequencies of interest.

> [!question]- Connection: How is the projection approximation an operator-splitting (commutation) question?
> Dictionary: the propagation $\partial_z u = (A + B)u$ has $A = \frac{i}{2k}\nabla_\perp^2$ (Fresnel, a generator of free propagation) and $B = i\sigma V$ (multiplication by the potential). The exit wave is the ordered exponential of $A + B$ over the thickness. Multislice approximates it by alternating $e^{\Delta z B}$ and $e^{\Delta z A}$ (Lie–Trotter / Strang splitting), with error controlled by the commutator $[A, B]$ ([[Matrix Exponential]], [[Duhamel's Principle]]). The projection approximation keeps only $e^{tB}$. That is exact if $A$ is negligible over $t$, or if $[A, B] = 0$; since $[\nabla_\perp^2, V] \neq 0$ wherever $V$ varies transversely, the error grows with $t$ and with resolution.
> **Where it breaks:** $A$ is an unbounded operator and $B$ a multiplication operator in infinite dimensions, so finite-dimensional splitting bounds hold only for band-limited $V$, i.e. up to a target resolution.

[^1]: [Singer and Sigworth, 2020, p. 6](zotero://open-pdf/library/items/FKVQSKD6?page=6&annotation=TTBCW788); [Sigworth, p. 4](zotero://open-pdf/library/items/PZX9RV5T?page=4&annotation=JLHI7RV6)
