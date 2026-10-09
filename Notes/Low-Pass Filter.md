---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Low-Pass Filter[^1]
> A linear filter whose [[Transfer Function (Signal Processing)|transfer function]] lets low [[Spatial Frequency|spatial frequencies]] (near the origin) pass and attenuates high frequencies.

# Properties
- Applied to an image, outputs a blurry picture encoding the coarse elements of the image.
- Used to blur images, e.g. to remove noise or in preparation for subsampling (to avoid [[Aliasing]]).
- Typical examples are the [[Box Filter]] (averaging), the [[Gaussian Filter]], and the [[Binomial Filter]] ([[Blur Filter|blur filters]]); they are normalized to [[DC Gain]] $1$.[^2]
- Counterparts: [[Band-Pass Filter]], [[High-Pass Filter]].

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
