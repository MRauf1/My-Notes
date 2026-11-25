---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Resolution (Cryo-EM)[^1]
> A [[Cryo-EM Density Map|map]] has resolution $d$ (in [[Ångström|Å]]) if its [[Fourier Transform|Fourier]] components are reliable up to spatial frequency $k = 1/d$, i.e. it contains trustworthy detail down to spacings of about $d$. Smaller $d$ is better. In practice, $d$ is read off the [[Fourier Shell Correlation]].

# Properties
- **What is visible** (approximate):

| Resolution | Visible |
|---|---|
| $> 10$ Å | overall shape, domains, subunit arrangement |
| $6$–$9$ Å | α-helices as rods, β-sheets as slabs |
| $\approx 4.5$ Å | individual β-strands separated |
| $3$–$4$ Å ("near-atomic") | backbone traceable, bulky side chains, sequence assignable |
| $2$–$3$ Å | most side chains, ligands, ordered water |
| $\lesssim 1.5$ Å ("atomic") | individual atoms as separate peaks |

- **Nyquist limit**: with pixel size $p$, the resolution cannot be better than $d = 2p$.
- **Local resolution** varies across a map, with flexible regions worse ([[Conformational Heterogeneity]]). **Directional resolution** varies with direction, under the [[Missing Wedge]] or [[Preferred Orientation]].
- What limits it is noise, radiation damage, alignment errors and lens aberrations, not the electron wavelength ($\approx 0.02$ Å). Its cost in particle count is given by the [[Rosenthal–Henderson Relation]].
- **Records.** Single-particle cryo-EM had reached about $1.5$ Å by early 2020, and $1.2$ Å later that year (apoferritin), where individual atoms are resolved (see [[Motion Correction]]). About $3$–$4$ Å suffices for an informative [[Atomic Model]], with chemical constraints filling in.
- The ultimate limit is the decay of signal with frequency ([[CTF Envelope Function]]).

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
