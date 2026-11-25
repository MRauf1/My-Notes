---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Wave Vector[^1]
> For a wave in $\mathbb{R}^n$ with phase $\theta(\mathbf{x}, t) = \mathbf{k}\cdot\mathbf{x} - \omega t + \varphi_0$, the wave vector $\mathbf{k} = \nabla_{\mathbf{x}}\theta$ points in the direction of propagation. Its magnitude is the [[Wavenumber|wavenumber]], $|\mathbf{k}| = 2\pi/\lambda$.

# Properties
- It is perpendicular to the [[Wavefront|wavefronts]] (in an isotropic medium).
- Its components are the wavenumbers along each axis. A wave tilted by $\theta$ from the $z$-axis has transverse component $k_\perp = |\mathbf{k}|\sin\theta$, so its crests repeat every $2\pi/k_\perp = \lambda/\sin\theta$ along a transverse line, which is the diffraction condition $d\sin\theta = \lambda$ ([[Diffraction]]).
- In Fourier analysis, $\mathbf{k}$ is the frequency variable: $\hat f(\mathbf{k})$ is the weight of the plane wave $e^{i\mathbf{k}\cdot\mathbf{x}}$ ([[Fourier Transform]], [[Spatial Frequency]]).

[^1]: [Wave vector (Wikipedia)](https://en.wikipedia.org/wiki/Wave_vector)
