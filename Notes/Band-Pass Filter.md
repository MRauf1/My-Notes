---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Band-Pass Filter[^1]
> A linear filter whose [[Transfer Function (Signal Processing)|transfer function]] lets a band of middle [[Spatial Frequency|spatial frequencies]] pass and attenuates both low and high frequencies.

# Properties
- Applied to an image, highlights middle size elements.
- Can be built as the difference of two [[Low-Pass Filter|low-pass filters]] with different cutoffs (e.g. a difference of Gaussians).[^2]
- Counterparts: [[Low-Pass Filter]], [[High-Pass Filter]].

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
