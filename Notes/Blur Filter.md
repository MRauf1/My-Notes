---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Blur Filter[^1]
> A [[Low-Pass Filter|low-pass filter]] that removes the high [[Spatial Frequency|spatial-frequency]] content of an image, leaving only the low-frequency components; the output has lost detail and looks blurry. Linear blurring computes local (weighted) averages over small neighborhoods of input pixels, i.e. a [[Convolution]] $\ell_{\text{out}} = h \circ \ell_{\text{in}}$ with a kernel $h$ whose [[DC Gain]] is usually normalized to $1$.

# Types
- Linear (convolutional):
	- [[Box Filter]]
	- [[Gaussian Filter]]
	- [[Binomial Filter]] (integer approximation of the Gaussian)
- Nonlinear (remove noise while preserving details such as contours):
	- Anisotropic diffusion
	- Bilateral filtering

# Properties
- Applications: noise reduction, revealing image structure at different scales, and upsampling/downsampling images (avoiding [[Aliasing]]).
- A desirable blur filter attenuates high spatial frequencies monotonically (stronger attenuation for higher frequencies) and cancels the highest frequency (the alternating wave $[\dots, 1, -1, 1, -1, \dots]$) completely; the [[Box Filter]] fails both, the discretized [[Gaussian Filter]] fails the second, and the [[Binomial Filter]] satisfies both.
- Common 2D blur kernels are [[Separable Filter|separable]], so they can be applied as cascades of 1D convolutions.

[^1]: [MIT Vision Book - Blurring](https://visionbook.mit.edu/blurring_2.html)
