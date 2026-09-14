---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Bidirectional Reflectance Distribution Function (BRDF))[^1]
> Given an incident [[Light Ray|light ray]] of power $\ell_{in}(\lambda)$ arriving from direction $\mathbf{p}$ at a surface point with normal $\mathbf{n}$, the bidirectional reflectance distribution function $F$ gives the power $\ell_{out}$ of the light reflected in the outgoing direction $\mathbf{q}$, as a function of the surface normal, the incoming and outgoing ray directions, and the wavelength $\lambda$:
> $$
> \begin{align}
> \ell_{out} = F(\ell_{in}, \mathbf{n}, \lambda, \mathbf{p}, \mathbf{q})
> \end{align}
> $$

![[BRDF Geometry.png]]

# Properties
- General BRDFs can be quite complicated, describing both diffuse and specular components of reflection; even surfaces with purely diffuse reflection can exhibit complicated reflectance distributions.
- Linear in the incoming light power $\ell_{in}$, by [[Linearity of Reflection]].
- The [[Lambertian Reflectance Model]] is a simplified BRDF, denoted $F_L$, that depends only on the surface orientation relative to the incoming and outgoing directions, not on the outgoing direction $\mathbf{q}$ itself.
- The [[Phong Reflection Model]] adds a view-dependent specular term on top of the diffuse reflection given by this BRDF framework.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
