---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Amplitude Contrast[^1]
> Contrast that is present even at zero [[Defocus (Cryo-EM)|defocus]]. It arises from the loss of electrons scattered to high angles by dense parts of the specimen (they miss the objective aperture), and from inelastic scattering. It enters the [[Contrast Transfer Function]] as a small phase offset, the **mixing angle** $\alpha$ (about $0.05$ rad for biological specimens):
> $$
> \begin{align}
> \mathrm{CTF}(f) = \sin\big(\chi(f) - \alpha\big),
> \end{align}
> $$
> where $\chi$ is the [[Wave Aberration Function|wave aberration function]].

# Properties
- It makes $\mathrm{CTF}(0) = -\sin\alpha$ slightly negative, so the very lowest frequencies are not completely lost.
- Under underfocus it has the same sign as low-frequency phase contrast, and the two add.
- For weak biological specimens it is small. Most of the signal is [[Phase Contrast Imaging|phase contrast]].

[^1]: [Sigworth, p. 7](zotero://open-pdf/library/items/PZX9RV5T?page=7&annotation=67EXVBIM)
