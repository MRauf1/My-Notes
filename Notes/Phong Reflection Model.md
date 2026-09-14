---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Phong Reflection Model)[^1]
> A model of surface reflection with a specular component. The light reflected from a surface is assumed to have three components: (1) an ambient component, a constant term added to all reflections; (2) a diffuse component, given by the [[Lambertian Reflectance Model]]; and (3) a specular component. For outgoing ray direction $\mathbf{q}$, the specular contribution is
> $$
> \begin{align}
> \ell_{\text{Phong spec}} = k_s (\mathbf{r} \cdot \mathbf{q})^\alpha \ell_{in}
> \end{align}
> $$
> where $k_s$ is a constant, $\alpha$ is a parameter governing the spread of the specular reflection, and $\mathbf{r}$ is the direction of maximum specular reflection,
> $$
> \begin{align}
> \mathbf{r} = 2(\mathbf{p} \cdot \mathbf{n})\mathbf{n} - \mathbf{p}.
> \end{align}
> $$

# Properties
- The direction $\mathbf{r}$ mirrors the incoming direction $\mathbf{p}$ about the surface normal $\mathbf{n}$, obeying the [[Law of Reflection]].
- The exponent $\alpha$ controls the spread of the specular highlight, playing the same role as the exponent $p$ in [[Blinn-Phong Shading]], which instead raises $\mathbf{n} \cdot \mathbf{h}$ (with $\mathbf{h}$ the half vector between the view and light directions) to this power, approximating the specular term without computing $\mathbf{r}$ directly.
- By [[Linearity of Reflection]], the total reflection due to multiple light sources is the sum of the ambient, diffuse, and specular contributions computed from each source.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
