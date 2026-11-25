---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Wave Aberration Function[^1]
> The phase $\chi(f)$ that the objective lens adds to the wave scattered at [[Spatial Frequency|spatial frequency]] $f$, relative to the unscattered wave:
> $$
> \begin{align}
> \chi(f) = -\pi\lambda\delta f^2 + \frac{\pi}{2}C_s\lambda^3 f^4,
> \end{align}
> $$
> with [[Defocus (Cryo-EM)|defocus]] $\delta$ (underfocus positive) and [[Spherical Aberration|spherical aberration]] coefficient $C_s$. The [[Contrast Transfer Function]] is then
> $$
> \begin{align}
> \mathrm{CTF}(f) = \sin\big(\chi(f) - \alpha\big)\, e^{-Bf^2/4},
> \end{align}
> $$
> with [[Amplitude Contrast|amplitude-contrast]] angle $\alpha$ and envelope B-factor $B$ ([[CTF Envelope Function]]).

# Properties
- The first term is the effect of a perfect lens that is out of focus; the second is spherical aberration. Higher-order aberration terms matter only beyond about $1$ Å resolution.
- The zeros of the CTF occur where $\chi(f) - \alpha \in \pi\mathbb{Z}$.

[^1]: [Sigworth, p. 8](zotero://open-pdf/library/items/PZX9RV5T?page=8&annotation=SGNHULZX)
