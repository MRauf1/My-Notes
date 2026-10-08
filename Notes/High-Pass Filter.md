---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] High-Pass Filter[^1]
> A linear filter whose [[Transfer Function (Signal Processing)|transfer function]] lets high [[Spatial Frequency|spatial frequencies]] pass and attenuates low frequencies (near the origin).

# Properties
- Applied to an image, shows the fine details of the image (e.g. edges and texture).
- Useful for edge enhancement.
- Can be built as the identity minus a [[Low-Pass Filter|low-pass filter]], $\delta - h_{\text{LP}}$; then its DC gain is $1 - H_{\text{LP}}[0,0]$, which is $0$ for a normalized low-pass kernel, so the output has zero mean ([[DC Value]]).[^2]
- Counterparts: [[Low-Pass Filter]], [[Band-Pass Filter]].

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
