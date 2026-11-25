---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Macromolecule[^1]
> A very large molecule built by polymerizing many smaller units (monomers): a protein (chains of amino acids), a nucleic acid (chains of nucleotides), or a complex of several such molecules held together (e.g. a ribosome, proteasome, or nuclear pore).

In cryo-EM, "the macromolecule" means **one whole copy** of the protein or complex under study, typically hundreds of kDa to several MDa. It does not mean one of its amino acids; a single amino-acid residue is about $110$ Da. One copy imaged in the specimen is called a *particle*.

# Properties
- A [[Cryo-EM Specimen]] contains many copies of the macromolecule. Combining them is what makes structure determination possible ([[Subtomogram Averaging]], [[Single-Particle Analysis]]).
- Copies may differ in composition or shape ([[Conformational Heterogeneity]]).
- **Size** is quoted as molecular mass in daltons (1 Da ≈ the mass of a hydrogen atom). An amino-acid residue is about $110$–$120$ Da. A large molecular machine of several subunits can total about $1$ MDa and measure about $200$ Å across.
- **Sequence determines fold.** A protein's amino-acid sequence (coded by DNA) determines its 3D fold. Hydrogen bonding gives α-helices and β-sheets, the interior is hydrophobic, and the surface is polar.
- **Structure prediction.** In 2020 the review stated that predicting a structure from sequence (the protein folding problem) had succeeded only for small proteins. That is outdated: AlphaFold (Jumper et al., Nature 2021) predicts many structures with near-experimental accuracy[^2]. Experiment is still needed for complexes, conformational states and ligands, and predicted models are now routinely docked into cryo-EM maps ([[Atomic Model]]).
- Molecular machines pass through several conformations in their cycles, so understanding one requires multiple structures ([[Conformational Heterogeneity]]).

[^1]: [Macromolecule (Wikipedia)](https://en.wikipedia.org/wiki/Macromolecule)
[^2]: [Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold, Nature 596:583–589](https://www.nature.com/articles/s41586-021-03819-2)
