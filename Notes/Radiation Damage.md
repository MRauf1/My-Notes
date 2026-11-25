---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Radiation Damage (Cryo-EM)[^1]
> Of the electrons crossing a [[Cryo-EM Specimen|specimen]]:
> - most pass without interaction and contribute only shot noise;
> - **elastically** scattered electrons keep their energy and form the phase-contrast signal ([[Projection Approximation]]);
> - **inelastically** scattered electrons lose energy, ionizing and breaking the molecules.
>
> That damage limits the total electron dose and exposure time. Inelastically scattered electrons carry no contrast: they are removed by an energy filter, or they add noise.

# Properties
- Inelastic scattering grows with ice thickness, so thin ice helps. Thin ice also makes it likelier that the beam crosses at most one molecule at each point.
- **Electrons versus X-rays.** Electrons cause orders of magnitude less damage per useful scattering event. In theory, about $10^4$ particles suffice for a structure, versus about $10^8$ molecules in a minimal crystal for [[X-Ray Crystallography]] at similar resolution.
- High-resolution signal decays with accumulated dose, so movies are dose-weighted ([[Motion Correction]]). Damage is part of the [[CTF Envelope Function|B-factor]].

[^1]: [Singer and Sigworth, 2020, p. 5](zotero://open-pdf/library/items/FKVQSKD6?page=5&annotation=L7DF32I2)
