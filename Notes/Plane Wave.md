---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Plane Wave[^1]
> A [[Wave]] in $\mathbb{R}^n$ whose [[Wavefront|wavefronts]] are parallel planes (hyperplanes) perpendicular to a fixed direction. The sinusoidal plane wave with [[Wave Vector|wave vector]] $\mathbf{k}$ and angular frequency $\omega$ is
> $$
> \begin{align}
> u(\mathbf{x}, t) = A\cos(\mathbf{k}\cdot\mathbf{x} - \omega t + \varphi_0), \qquad \text{or } \psi(\mathbf{x}, t) = A e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}.
> \end{align}
> $$
> At any instant, $u$ is constant on each plane $\mathbf{k}\cdot\mathbf{x} = \text{const}$, and these planes move along $\mathbf{k}$ at the [[Phase Velocity|phase velocity]] $\omega/|\mathbf{k}|$.

![[Plane Wave.png]]

In the figure, the red planes are crests and the blue planes are troughs ([[Crest and Trough]]). The arrows show the field value along one line, which is the same everywhere on each plane, and the planes advance at the phase velocity.

# Properties
- It is an idealization: it extends infinitely and has a single direction and frequency. A distant point source is locally a plane wave, e.g. the parallel illumination beam in electron microscopy ([[Projection Approximation]]).
- **Plane waves are the Fourier basis.** Any (nice) function is a superposition of plane waves, $f(\mathbf{x}) = \int \hat f(\mathbf{k})\, e^{i\mathbf{k}\cdot\mathbf{x}}\, d\mathbf{k}/(2\pi)^n$ ([[Fourier Transform]]). So a specimen that modulates a plane wave sends out one diffracted plane wave per spatial frequency ([[Diffraction]]).
- Superposing two plane waves of equal frequency but different directions gives straight interference fringes, with period $2\pi/|\mathbf{k}_1 - \mathbf{k}_2|$ ([[Interference (Waves)]]).

# Questions
> [!question]- When is a plane wave $e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}$ a solution of the wave equation $u_{tt} = c^2\Delta u$?
> Each derivative acts by multiplication: $\partial_t \mapsto -i\omega$ and $\nabla \mapsto i\mathbf{k}$. So $u_{tt} = -\omega^2 u$ and $\Delta u = -|\mathbf{k}|^2 u$. The equation holds if and only if $\omega^2 = c^2|\mathbf{k}|^2$, i.e. $\omega = \pm c|\mathbf{k}|$ (the dispersion relation). The phase velocity is then $c$ in every direction ([[Wave Equation]]).

> [!question]- Show that two plane waves of the same frequency with wave vectors $\mathbf{k}_1 \neq \mathbf{k}_2$ produce fringes with period $2\pi/|\mathbf{k}_1 - \mathbf{k}_2|$.
> With $\psi = e^{i(\mathbf{k}_1\cdot\mathbf{x} - \omega t)} + e^{i(\mathbf{k}_2\cdot\mathbf{x} - \omega t)}$, the intensity is
> $$
> \begin{align}
> |\psi|^2 = 2 + 2\cos\big((\mathbf{k}_1 - \mathbf{k}_2)\cdot\mathbf{x}\big),
> \end{align}
> $$
> which is time-independent and constant on planes perpendicular to $\mathbf{k}_1 - \mathbf{k}_2$. Its period along $\mathbf{k}_1 - \mathbf{k}_2$ is $2\pi/|\mathbf{k}_1 - \mathbf{k}_2|$. For a transmitted beam $\mathbf{k}_1 = (0, k)$ and a beam diffracted at angle $\theta$, $|(\mathbf{k}_1 - \mathbf{k}_2)_\perp| = k\sin\theta = 2\pi/d$, so the fringes reproduce the specimen period $d$.

[^1]: [Plane wave (Wikipedia)](https://en.wikipedia.org/wiki/Plane_wave)
