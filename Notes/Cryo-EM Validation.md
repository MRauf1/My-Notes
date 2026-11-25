---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Validation[^1]
> Checking that a reconstruction faithfully represents the data rather than the initialization or the analyst's assumptions (model bias, [[Einstein from Noise]]). Because the reconstruction problem is non-convex, the output can depend on the initialization, and there is no agreed computational standard. Practice combines several heuristics:
> - **Multiple initializations**: random restarts converging to similar structures.
> - **Biological plausibility**: correct primary and secondary structure.
> - **Tilt-pair validation**: two images of the same particles at a known relative tilt; the assigned orientations must differ by that tilt. It is useful only at intermediate resolution.
> - **Cross-technique comparison** with [[X-Ray Crystallography]] or [[NMR Structure Determination]] structures.
> - **Public data deposition**, so others can reprocess.
> - **Half-map [[Fourier Shell Correlation]]** for resolution.

# Properties
- **Half-maps are not immune.** Refining both halves with the same procedure, reference or mask can induce correlated errors even though the data are independent, which inflates the FSC ([[Cryo-EM Masking]]). Tests that measure the amount of overfitting in a map have been proposed.
- **Open challenge**: confidence intervals for maps that are robust to systematic errors ([[Open Problems in Cryo-EM]]).

[^1]: [Bendory et al., 2020, p. 23](zotero://open-pdf/library/items/N4ZIHINK?page=23&annotation=G373XRJW)
