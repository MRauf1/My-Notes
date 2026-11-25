---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Projection Approximation[^1]
> For a thin, weakly scattering [[Cryo-EM Specimen|specimen]] with electrostatic potential $V : \mathbb{R}^3 \to \mathbb{R}$ (what a [[Cryo-EM Density Map]] reconstructs), illuminated by a parallel beam along a unit direction $d$, the exit wave only acquires a phase proportional to the line integral of $V$ along the beam:
> $$
> \begin{align}
> \psi_{\text{out}}(x) = \psi_{\text{in}}\, \exp\!\big(i\sigma\, (P_d V)(x)\big), \qquad (P_d V)(x) = \int_{\mathbb{R}} V(x + s\,d)\, ds, \quad x \in d^{\perp}.
> \end{align}
> $$
> Here $\sigma$ is the interaction constant. Defocus converts this phase into recorded intensity (phase contrast), so to first order each image is a linear, filtered function of the projection $P_d V$.

The projection is **parallel (orthographic)**: there is no perspective, because the beam is parallel and the depth of field is much larger than the specimen.

# Properties
- **Refraction is present but negligible.** Ice has a positive mean inner potential $V_0$ of a few volts. This gives it a refractive index for electrons
$$
\begin{align}
n - 1 \approx \frac{V_0}{U}\cdot\frac{E_0 + eU}{2E_0 + eU} \sim 10^{-5} \quad (U = 300 \text{ kV},\ E_0 = 511 \text{ keV}).
\end{align}
$$
A parallel-faced slab only offsets the beam sideways, by $\approx L\,(n-1)\tan\theta$, which is about $0.06$ Å for a path $L = 400$ nm at $\theta = 60^\circ$. This offset is the same for every particle, so it carries no depth information. The phase *variations* due to the molecules (tiny local refractions) are the signal itself.
- **Validity requires a short path.** The fraction of electrons that pass without inelastic scattering decays like $e^{-L/\lambda_{\text{in}}}$, where $\lambda_{\text{in}}$ is a few hundred nm in ice. Inelastically scattered electrons blur the image. In thick specimens multiple scattering also becomes common, and the image stops being a projection. This is what limits the [[Tilt Series|tilt range]].
- Together with the [[Fourier Slice Theorem]], it says that each image measures one central plane of $\hat V$.
- **Size of the signal.** Passing within about $1$ Å of a nucleus (a potential of tens of volts) advances the electron's phase by about a milliradian. Mean inner potentials are about $5$ V for vitreous ice, $6.5$ V for lipid bilayers and $7.5$ V for protein. Cryo-EM images the protein–ice contrast.
- Defocus converts the phase into intensity through the [[Contrast Transfer Function]]. The full per-particle model is the [[Cryo-EM Image Formation Model]].
- The phase picked up is an accumulated [[Phase Shift|phase shift]]: the local wavelength shortens inside the potential, and the excess $\int (k - k_0)\,dz$ remains after the wave exits.
- **Interaction constant values**: $\sigma \approx 0.86$, $0.73$ and $0.65$ mrad/(V·Å) for $120$, $200$ and $300$ keV electrons.[^sigworth]
- **Size of the phase shift per atom.** The source describes a few tens of volts over about $1$ Å as giving "on the order of a milliradian". With $\sigma = 0.65$ mrad/(V·Å), $20$ V × $1$ Å gives about $13$ mrad, so the order of magnitude is milliradians to about $10$ mrad. Either way it is small, which is the [[Weak Phase Approximation]].
- It is approximation A2 of the [[Cryo-EM Forward Model]]: dropping the Fresnel term $\frac{i}{2k}\nabla_\perp^2u$ of the paraxial [[Schrödinger Equation]] inside the specimen.

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
[^sigworth]: [Sigworth, p. 2](zotero://open-pdf/library/items/PZX9RV5T?page=2&annotation=ID5WZXFW)
