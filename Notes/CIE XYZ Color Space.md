---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (CIE XYZ Color Space)[^1]
> A standard [[Color Reproduction System|color space]] defined by the Commission Internationale de l'Éclairage (CIE) using three color-matching functions, $\bar{x}(\lambda)$, $\bar{y}(\lambda)$, $\bar{z}(\lambda)$, chosen to be all-positive at every wavelength, unlike the eye's own cone sensitivity curves.

![[CIE Color Matching Functions.png]]

# Properties
- Projecting a light spectrum onto these three functions gives its [[Tristimulus Values|tristimulus values]], $X$, $Y$, and $Z$.
- Normalizing the tristimulus values to remove overall intensity gives the **CIE chromaticity coordinates**, $x = X/(X+Y+Z)$ and $y = Y/(X+Y+Z)$.
- No set of physically realizable (non-negative) primary lights forms a valid [[Color Reproduction System|color-matching system]] with the CIE color-matching functions, even though the matrix $\mathbf{C}_{CIE}$ is itself a valid matrix for measuring color.

[^1]: [MIT Vision Book - Color](https://visionbook.mit.edu/color.html)
