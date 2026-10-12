---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Brightness Constancy Assumption[^1]
> The intensity of a scene point is preserved as it moves through an image sequence $\ell(x, y, t)$. For a displacement $(u, v)$ between consecutive frames,
> $$
> \begin{align}
> \ell(x + u, y + v, t + 1) = \ell(x, y, t)
> \end{align}
> $$
> In particular, a static image $\ell_0(x, y)$ translating globally with constant velocity $(v_x, v_y)$ produces the sequence
> $$
> \begin{align}
> \ell(x, y, t) = \ell_0(x - v_x t, y - v_y t)
> \end{align}
> $$

# Properties
- The initial hypothesis of most motion estimation algorithms.
- **Brightness constancy constraint**: for small motions, a first-order Taylor expansion (or differentiating $\ell_0(x - v_x t, y - v_y t)$ in $t$) gives a linear constraint on the velocity[^2]
$$
\begin{align}
\frac{\partial \ell}{\partial x} v_x + \frac{\partial \ell}{\partial y} v_y + \frac{\partial \ell}{\partial t} = 0
\end{align}
$$
  i.e. $(\ell_x, \ell_y, \ell_t) \cdot (v_x, v_y, 1) = 0$, relating the [[Image Gradient|spatial gradient]] to the temporal derivative. It is a single equation in two unknowns, so locally only the velocity component along the gradient is recoverable (the aperture problem).[^2]
- In the frequency domain, a sequence satisfying global brightness constancy is supported on a plane: see [[Fourier Transform of Moving Image]].
- Violated by illumination changes, shading changes under motion, specularities, occlusions, and transparency.[^2]
- Underlies velocity-tuned [[Spatio-Temporal Gaussian Filter|spatio-temporal derivative filters]].

[^1]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
[^2]: Added from general knowledge.
