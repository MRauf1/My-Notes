---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Color Reproduction System)[^1]
> A system that measures an input light and produces an output light matching its color appearance to a human observer, such as a camera together with a screen display. It is defined by a $3 \times N$ matrix $\mathbf{C}$ of sensor spectral sensitivity curves (one row per sensor, over $N$ wavelength samples), a set of primary light spectra forming the columns of a matrix $\mathbf{P}$, and a $3 \times 3$ matrix $\mathbf{M}$ translating a color measurement $\mathbf{C}\mathbf{t}$ into amplitude controls $\mathbf{M}\mathbf{C}\mathbf{t}$ for the primary lights.

# Properties
- Perfectly reproduces colors, as judged by a human observer, exactly when the sensing matrix is some linear combination of the eye's cone sensitivities, $\mathbf{C} = \mathbf{R}\,\mathbf{C}_{eye}$ for a full-rank $3 \times 3$ matrix $\mathbf{R}$, and the mixing matrix is $\mathbf{M} = (\mathbf{C}\mathbf{P})^{-1}$.
- Because primary lights can only be combined in non-negative amounts, only colors within the system's [[Color Gamut]] can actually be produced, even when the sensing and mixing matrices satisfy the perfect-reproduction condition.
- Relies on the [[Trichromatic Theory of Color Vision]]: reproducing only the three tristimulus values of a color, rather than its full [[Power Spectrum]], suffices for a perceptual match.

[^1]: [MIT Vision Book - Color](https://visionbook.mit.edu/color.html)
