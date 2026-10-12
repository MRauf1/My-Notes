---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Image Gradient[^1]
> The [[Gradient Vector|gradient]] of an image $\ell(x, y)$, a 2D vector at each pixel:
> $$
> \begin{align}
> \nabla \ell(x, y) = \left(\frac{\partial \ell(x, y)}{\partial x}, \frac{\partial \ell(x, y)}{\partial y}\right)
> \end{align}
> $$
> With [[Gaussian Derivative|Gaussian derivatives]], $\nabla \ell \circ g = \nabla g \circ \ell = (g_x(x, y), g_y(x, y)) \circ \ell$; with discrete kernels $d_n[n, m], d_m[n, m]$ ([[Discrete Image Derivative]]), $\nabla \ell = (d_n[n, m], d_m[n, m]) \circ \ell[n, m]$.

# Properties
- **Directional derivative**: along $\mathbf{t} = (\cos\theta, \sin\theta)$ the [[Directional Derivative|directional derivative]] is a linear combination of the two axis derivatives,
$$
\begin{align}
\frac{\partial \ell(x, y)}{\partial \mathbf{t}} = \nabla \ell \cdot \mathbf{t} = \cos(\theta) \frac{\partial \ell}{\partial x} + \sin(\theta) \frac{\partial \ell}{\partial y}
\end{align}
$$
- **Steerability**: in the Gaussian case,
$$
\begin{align}
\frac{\partial \ell}{\partial \mathbf{t}} \circ g = (\nabla g \cdot \mathbf{t}) \circ \ell = g_\theta(x, y) \circ \ell(x, y) = \cos(\theta) \, g_x \circ \ell + \sin(\theta) \, g_y \circ \ell
\end{align}
$$
  with $g_\theta = \cos(\theta) g_x + \sin(\theta) g_y$, so the derivative along any angle requires no new convolutions, only a linear combination of the outputs of $g_x$ and $g_y$ (a steerable filter[^2]).
- In the discrete case $d_\theta[n, m] = \cos(\theta) d_n[n, m] + \sin(\theta) d_m[n, m]$ only approximates the derivative along $\theta$; the quality of the approximation depends on the kernels (e.g. [[Roberts Cross Operator]], [[Sobel Operator]]).
- Summing the $x$ and $y$ first derivatives gives a first derivative along $45^\circ$ (not rotationally invariant), unlike summing second derivatives ([[Laplacian Filter]]).
- The basis of edge-based descriptors such as SIFT and HOG, and of the [[Retinex Algorithm]].

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
[^2]: Term from Freeman & Adelson (1991), added from general knowledge.
