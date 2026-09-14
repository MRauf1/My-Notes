---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Trichromatic Theory of Color Vision)[^1]
> The empirical finding that the appearance of any color can be matched by an appropriate linear combination of three fixed reference lights, called **primary colors**, due to the presence of three classes of [[Cones|cone]] photoreceptors in the eye.

# Properties
- The eye's response to an incident light spectrum $\mathbf{t}$ can be written as a matrix product $[L, M, S]^T = \mathbf{C}_{eye}\mathbf{t}$, where the rows of $\mathbf{C}_{eye}$ are the spectral sensitivity curves of the L, M, and S cones.
- Because the eye's photosensors respond linearly to incoming light, the rules of linear algebra apply to color matching and manipulation, e.g. via [[Grassmann's Laws]].
- Underlies why any [[Color Reproduction System]] need only reproduce three numbers per color, rather than an entire [[Power Spectrum]], to achieve a perceptual color match.
- Reduces the high-dimensional space of possible light [[Power Spectrum|power spectra]] to a 3D subspace of perceived colors, giving rise to [[Metamerism]].

[^1]: [MIT Vision Book - Color](https://visionbook.mit.edu/color.html)
