---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Atomic Model[^1]
> A list of the atoms of a [[Macromolecule|macromolecule]]. Each atom $a$ has coordinates $r_a \in \mathbb{R}^3$, an element, its residue and chain, an occupancy, and a B-factor $B_a$ (the spread of its displacement). It is stored as a PDB/mmCIF file. It relates to a [[Cryo-EM Density Map]] by the forward model
> $$
> \begin{align}
> V(x) \approx \sum_a \big(\varphi_{Z_a} * G_{B_a}\big)(x - r_a),
> \end{align}
> $$
> where $\varphi_Z$ is the scattering potential of an atom of atomic number $Z$, and $G_B$ is a Gaussian (the density of the atom's displacement) whose width is set by $B$.

# Properties
- **Building.** The sequence is known. Model building traces the backbone, places side chains, and refines all coordinates against the map **subject to stereochemical restraints**: bond lengths and angles, allowed backbone torsions (the Ramachandran plot), no clashes. Today it often starts from a predicted structure docked into the map.
- **Validation**: map–model [[Fourier Shell Correlation]], geometry statistics, and whether side chains sit in density.
- **Interpretation, not measurement.** It is far lower-dimensional than the map: about $3N$ coordinates with strong priors, versus $10^6$–$10^7$ voxels. At $3$–$4$ Å [[Resolution (Cryo-EM)|resolution]], individual atoms are not resolved, so the restraints and priors determine much of it; the worse the resolution, the more the prior decides. Pseudo-atomic models (coarse Gaussians or beads) are an intermediate representation.
- **Naming clash.** The per-atom B-factor is a local displacement spread. The global B-factor of the [[Rosenthal–Henderson Relation]] is the overall decay of signal with frequency.

[^1]: [Protein Data Bank (file format) (Wikipedia)](https://en.wikipedia.org/wiki/Protein_Data_Bank_(file_format))
