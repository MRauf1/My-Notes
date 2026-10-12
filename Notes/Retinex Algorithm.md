---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Retinex Algorithm[^1]
> An algorithm (Land and McCann) that separates an image $\ell(x, y) = r(x, y) \times l(x, y)$ into a reflectance image $r(x, y) \in (0, 1)$ and an illumination image $l(x, y)$, assuming the illumination varies smoothly while the reflectance consists of uniform patches separated by sharp boundaries:
> 1. Take the log to turn the product into a sum, $\log \ell = \log r + \log l$, so that $\frac{\partial \log \ell}{\partial x} = \frac{\partial \log r}{\partial x} + \frac{\partial \log l}{\partial x}$ (same for $y$).
> 2. Threshold the [[Image Gradient|gradients]]: large derivatives are assigned to reflectance, small ones to illumination,
> $$
> \begin{align}
> \frac{\partial \log r(x, y)}{\partial x} = \begin{cases} \frac{\partial \log \ell(x, y)}{\partial x} & \text{if } \left|\frac{\partial \log \ell(x, y)}{\partial x}\right| > T \\ 0 & \text{otherwise} \end{cases}
> \end{align}
> $$
> 3. Integrate the gradients to get $\log r$ ([[Signal Reconstruction from Derivatives]]) and exponentiate.
> 4. Recover the illumination as $l(x, y) = \ell(x, y) / r(x, y)$.

The motivating question is how the visual system tells gray from white. The light reaching the eye confounds the illumination with the surface reflectance, yet [[Perception|perception]] tracks reflectance: two patches with identical intensity $\ell$ can look different because the visual system (at least partially) discounts the illumination. Retinex is a simple model of this estimation of reflectance and illumination.

# Properties
- Rationale: two adjacent pixels inside a uniform-reflectance patch differ little (even nonuniform illumination changes slowly), whereas pixels across a reflectance boundary differ strongly.
- Illumination derivatives are much smaller than reflectance derivatives but extend over much larger regions, so once integrated, brightness changes from nonuniform illumination may exceed those from reflectance.
- Works remarkably well on simple displays and many real images, but its assumptions are restrictive and it fails in situations where the human visual system succeeds.
- The brightness difference it recovers is stronger than what humans perceive, since perception also depends on context, grouping (e.g. surfaces appearing to float in different planes), and incomplete separation of the two components.
- An early instance of [[Intrinsic Image Decomposition]].

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
