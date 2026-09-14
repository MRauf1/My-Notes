---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Linearity of Reflection)[^1]
> Surface reflection behaves linearly in the incoming light: the light reflected off a surface illuminated by the sum of two light sources equals the sum of the light that would be reflected by each source individually,
> $$
> \begin{align}
> \ell_{out}(\ell_{in,1} + \ell_{in,2}) = \ell_{out}(\ell_{in,1}) + \ell_{out}(\ell_{in,2}).
> \end{align}
> $$

# Properties
- Equivalently, the [[Bidirectional Reflectance Distribution Function (BRDF)]] $F$ is linear in its incoming-light argument $\ell_{in}$.
- Lets the total light reflected due to multiple light sources be computed by summing each source's individual contribution, rather than needing to reason about the sources jointly.
- Underlies the additive combination of ambient, diffuse, and specular contributions from multiple lights in the [[Phong Reflection Model]] and its [[Blinn-Phong Shading|Blinn-Phong]] approximation.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
