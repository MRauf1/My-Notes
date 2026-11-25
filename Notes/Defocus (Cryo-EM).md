---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Defocus (Cryo-EM)[^1]
> The distance $\delta$ between the specimen and the plane on which the objective lens is focused, used to create [[Phase Contrast Imaging|phase contrast]]. In the usual convention, $\delta = -z > 0$ means **underfocus**: the lens is weakened (less current) and focuses *above* the specimen. As far as the lens can tell, the electron waves could have started there. In this convention the phase-contrast term of the [[Contrast Transfer Function]] is $\sin(-\pi\lambda\delta f^2)$, with spatial frequency $f = 1/d$.

# Properties
- **Why underfocus.** At low spatial frequencies it gives negative phase contrast, the same sign as [[Amplitude Contrast|amplitude contrast]], so the two add. It also partly compensates [[Spherical Aberration|spherical aberration]].
- **Trade-off.** Larger $\delta$ boosts low-frequency contrast, so particles are easier to see and pick, but the CTF oscillates faster at high frequencies. Spatial incoherence also damps high frequencies more at large defocus, because a source angular spread $\alpha$ shifts the pattern by $\alpha\delta$ ([[CTF Envelope Function]]). Typical values are about $1$ μm, roughly $400{,}000$ wavelengths.
- Different micrographs are taken at different defoci so that CTF zeros fall at different frequencies ([[CTF Correction]]). The defocus is estimated from the data ([[CTF Estimation]]).

# Questions
> [!question]- Show that underfocus makes low-frequency phase contrast and amplitude contrast add rather than cancel.
> With amplitude contrast as a phase offset $\alpha$, $\mathrm{CTF}(f) = \sin(-\pi\lambda\delta f^2 - \alpha)$. At $f = 0$ it equals $-\sin\alpha < 0$, the amplitude-contrast term. For $\delta > 0$ (underfocus), $-\pi\lambda\delta f^2 - \alpha$ becomes more negative as $f$ grows, so $|\mathrm{CTF}|$ grows with the same negative sign: they reinforce. For $\delta < 0$ (overfocus), the phase term is positive and first cancels the amplitude term, giving a zero at low frequency.

[^1]: [Sigworth, p. 6](zotero://open-pdf/library/items/PZX9RV5T?page=6&annotation=HDZD5SCA)
