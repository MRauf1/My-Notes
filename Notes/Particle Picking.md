---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Particle Picking[^1]
> Segmenting and boxing out particle images from micrographs, discarding regions with noise or contaminants. The classic method is **template matching**: cross-correlate a few templates with every micrograph window and keep windows with high correlation. Templates can be:
> - Gaussian blobs or their differences;
> - projections of a low-resolution (e.g. negative-stain, $\sim 40$ Å) map;
> - $10$–$100$ class averages from $10^3$–$10^4$ manually picked particles.

# Properties
- **Size limit.** Detection reliability falls with particle mass, since contrast and SNR fall. In 2020, the limit without other help was about $40$ kDa. The record now stands at about $38$ kDa without a scaffold[^2], and $14$ kDa with a nanobody scaffold (lysozyme, 2025)[^3].
- **Model bias.** Templates bias which windows are selected, and so the reconstruction ([[Einstein from Noise]]).
- **Outliers.** Picked stacks contain false positives: several particles in one box, partial particles, pure noise.
- **Deep-learning pickers** are faster but also prone to model bias, and they need training. As of 2025 reviews, picking is still an open problem for small proteins, for complete view coverage, and for lack of large labelled datasets[^4].
- **Picking-free reconstruction**, directly from micrographs or from all movie frames, is an active direction ([[Open Problems in Cryo-EM]]).
- **Template-free picking.** Select reference windows automatically by local mean and variance (particles have lower mean and higher variance), correlate, then train a classifier (SVM) on the most and least particle-like regions.[^5]
- **Outlier pruning**: a consensus of several pickers via a neural network, or a Gaussian-mixture model of the picker's outputs. RELION's workflow: manually pick a few hundred particles, 2D-classify them, and use the class averages as templates.

[^1]: [Singer and Sigworth, 2020, p. 11](zotero://open-pdf/library/items/FKVQSKD6?page=11&annotation=8SHIQTKN)
[^2]: [High-resolution cryo-EM structures of small protein–ligand complexes near the theoretical size limit (Nat. Commun. 2026)](https://www.nature.com/articles/s41467-026-71934-7)
[^3]: [Nanobody scaffolds enable cryo-EM imaging of smallest protein structure yet (Diamond Light Source, 2025)](https://www.diamond.ac.uk/Home/News/LatestNews/2025/New-nanobody-scaffold-unlocks-cryo-EM-imaging-of-the-smallest-proteins.html)
[^4]: [Artificial intelligence in cryo-EM protein particle picking: recent advances and remaining challenges (Brief. Bioinform. 2025)](https://academic.oup.com/bib/article/26/1/bbaf011/7958312)
[^5]: [Bendory et al., 2020, p. 18](zotero://open-pdf/library/items/N4ZIHINK?page=18&annotation=5CBEJML4)
