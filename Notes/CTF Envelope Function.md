---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] CTF Envelope Function[^1]
> The factor $E(|k|)$ of the [[Contrast Transfer Function]] that damps high frequencies, usually modelled as Gaussian:
> $$
> \begin{align}
> E(|k|) = e^{-B|k|^2/4},
> \end{align}
> $$
> where $B$ (in Å$^2$) is the **B-factor**. Good datasets have $B \approx 60$–$100$ Å$^2$.

# Properties
- **Size of the damping.** The amplitude at resolution $d$ is attenuated by $e^{-B/(4d^2)}$.
  - $B = 60$, $d = 4$ Å: amplitude $\approx e^{-0.94} \approx 1/e$, power $\approx e^{-1.9} \approx 0.15$.
  - $B = 100$, $d = 5$ Å: amplitude $1/e$.
  - $B = 100$, $d = 2.5$ Å: amplitude $e^{-4}$. The source states $1/e^2$ here, but $|k|^2$ quadruples when $d$ halves, so the exponent quadruples.
- **It is the ultimate limit on resolution**, and it sets the particle count through the [[Rosenthal–Henderson Relation]] (the same $B$).
- **Contributions**:
  - *Spatial incoherence*: an angular spread $\alpha$ of incident electrons shifts the defocused image by $\alpha z$. With $\alpha = 10^{-3}$ rad (tungsten source) and $z = 1$ μm, a 1 nm periodicity is washed out. Field-emission guns reach $10^{-5}$–$10^{-6}$ rad.
  - *Charging*: ejected electrons leave the specimen positively charged, which deflects incident electrons like a larger source.
  - *[[Beam-Induced Motion]]* and Brownian motion of particles from beam-induced rearrangement of water. Water diffuses by about $1$ Å$^2$ per $1\ e^-/\text{Å}^2$ of dose.
  - *[[Radiation Damage]]*.
- On modern microscopes, coherence, stage stability and charging contribute little. Uncorrected beam-induced motion is the largest term, and after $2\ e^-/\text{Å}^2$ radiation damage accounts for more than half of $B$.
- **The decay is faster at higher defocus**, because a source angular spread $\alpha$ shifts the defocused pattern by $\alpha\delta$ ([[Defocus (Cryo-EM)]]). Sigworth quotes $B \approx 50$–$100$ Å$^2$ for good images; at $B = 100$ Å$^2$, $5$ Å frequencies are attenuated to $1/e$.[^sigworth]

[^1]: [Singer and Sigworth, 2020, p. 7](zotero://open-pdf/library/items/FKVQSKD6?page=7&annotation=KBCGATDS)
[^sigworth]: [Sigworth, p. 10](zotero://open-pdf/library/items/PZX9RV5T?page=10&annotation=SVZB882Y)
