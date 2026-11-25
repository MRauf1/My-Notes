---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Masking[^1]
> A support prior: values of the map $\varphi$ outside a specified real-space region, the molecule's support, are set to zero during refinement ([[MAP Refinement (Cryo-EM)]]).

# Properties
- It shrinks the parameter space and removes solvent noise, so it can raise resolution.
- **Risk: an inverse crime.** The mask should come from prior knowledge, e.g. a known elongated shape. A mask taken from a first refinement and fed into a second one uses the data twice. This is an "inverse crime" and gives overoptimistic results, e.g. inflated [[Fourier Shell Correlation]].
- Masks also focus [[3D Classification]] on a region.

[^1]: [Singer and Sigworth, 2020, p. 19](zotero://open-pdf/library/items/FKVQSKD6?page=19&annotation=33HLAYG9)
