---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Processing Pipeline[^1]
> The computational pipeline of [[Single-Particle Analysis]] has two stages:
> 1. **Micrograph level**, mostly classical image and signal processing: [[Motion Correction]], [[CTF Estimation]], [[Particle Picking]].
> 2. **Particle level**, mostly statistical estimation and optimization: [[2D Classification]], [[Ab Initio Reconstruction]], 3D reconstruction ([[Iterative Refinement (Cryo-EM)]], [[MAP Refinement (Cryo-EM)]]), and heterogeneity analysis ([[Conformational Heterogeneity]]).
>
> It ends with fitting an [[Atomic Model]] into the map and validating its [[Resolution (Cryo-EM)|resolution]].

# Properties
- **Manual intervention** happens at two points:
  - tuning picking thresholds to limit false positives;
  - choosing 2D/3D classes to keep for the "best" reconstruction, which often rejects most particles.

  Rejected particles may be contaminants, incomplete or denatured complexes, or genuine alternative conformations. That makes the selection subjective and hard to reproduce.
- **On-the-fly processing** runs concurrently with data collection at facilities. It gives early quality checks (CTF-fit resolution, detail in 2D classes, even 3D maps), speeds up specimen optimization, and makes better use of microscope time.
- Full flowchart: movie frame alignment → CTF estimation → particle picking (and pruning) → 2D classification → ab initio model → optional 3D classification → 3D refinement → optional per-particle refinement → post-processing. Steps are often iterated, e.g. re-picking with class averages as templates.[^2]

![[Cryo-EM SPR Pipeline Flowchart.png]]

[^1]: [Singer and Sigworth, 2020, p. 9](zotero://open-pdf/library/items/FKVQSKD6?page=9&annotation=UUPTCYFE)
[^2]: [Bendory et al., 2020, p. 34](zotero://open-pdf/library/items/N4ZIHINK?page=34&annotation=HG3MH6RA)
