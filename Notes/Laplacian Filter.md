---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Laplacian Filter[^1]
> The image filter computing the [[Laplacian Operator|Laplacian]], the sum of the second order [[Partial Derivative|partial derivatives]] (the divergence of the [[Image Gradient|gradient]]):
> $$
> \begin{align}
> \nabla^2 \ell = \frac{\partial^2 \ell}{\partial x^2} + \frac{\partial^2 \ell}{\partial y^2}
> \end{align}
> $$
> Being more noise sensitive than first derivatives, it is usually combined with a [[Gaussian Filter|Gaussian]] $g$, $\nabla^2 \ell \circ g = \nabla^2 g \circ \ell$, where the **Laplacian of Gaussian** is
> $$
> \begin{align}
> \nabla^2 g = \frac{x^2 + y^2 - 2\sigma^2}{\sigma^4} g(x, y)
> \end{align}
> $$
> In 1D it is approximated by $[1, -2, 1] = [1, -1] \circ [1, -1]$; in 2D by the **five-point formula**
> $$
> \begin{align}
> \nabla_5^2 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \qquad \nabla_5^2 \ell[n, m] = -4\ell[n, m] + \ell[n+1, m] + \ell[n-1, m] + \ell[n, m+1] + \ell[n, m-1]
> \end{align}
> $$

# Properties
- Popularized by Marr and Hildreth (1980) for locating boundaries between objects.
- The five-point kernel is sum-separable: convolve with $[1, -2, 1]$ and with its transpose and sum the outputs (the central pixel and its four nearest neighbors).
- The Laplacian of Gaussian follows from the [[Gaussian Derivative]] $g_{x^2} = \frac{x^2 - \sigma^2}{\sigma^4} g$ summed over both axes.
- Advantages over the [[Image Gradient|gradient]]:
	- **Rotationally invariant**: a linear operator responding equally to edges in any orientation (only approximately in the discrete case). Summing the two second derivatives gives a rotationally invariant kernel, whereas summing the two first derivatives gives a $45^\circ$ derivative.
	- **Measures curvature**: a linear trend has non-zero derivative despite having no boundaries, but zero Laplacian.
	- Edges can be located at its **zero-crossings**, though this is not a very reliable edge detector.
	- Zero-crossings of an image form closed contours.
- Applications beyond images: it models vibrations in physics ([[Wave Equation]]; whether one can "hear the shape of a drum" from its Laplacian eigenvalues, Kac 1966), graph theory, and spectral methods for image segmentation ([[Graph Laplacian Matrix]]).
- Since $\nabla^2 \ell$ has [[DC Gain]] $0$, it is a [[High-Pass Filter]]; subtracting it from the image sharpens it ([[Sharpening Filter]]).[^2]

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
[^2]: Added from general knowledge.
