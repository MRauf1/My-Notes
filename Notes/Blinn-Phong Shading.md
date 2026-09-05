---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Blinn-Phong Shading)[^1]
> A [[Shading]] model, proposed by Phong and updated by Blinn, that adds a specular highlight to [[Lambertian Shading]], brightest when the view direction $\mathbf{v}$ and light direction $\mathbf{l}$ are symmetric about the surface [[Normal Vector|normal]] $\mathbf{n}$ (i.e., near a mirror configuration), and decreasing smoothly away from it:
> $$
> \begin{align}
> \mathbf{h} = \frac{\mathbf{v} + \mathbf{l}}{\lVert \mathbf{v} + \mathbf{l} \rVert}, \qquad L = k_d I \max(0, \mathbf{n} \cdot \mathbf{l}) + k_s I \max(0, \mathbf{n} \cdot \mathbf{h})^p
> \end{align}
> $$
> where $\mathbf{h}$ is the half vector bisecting $\mathbf{v}$ and $\mathbf{l}$, $k_s$ is the specular coefficient (specular color), and $p$ is the Phong exponent.

![[Blinn-Phong Shading.png]]

# Properties
- Closeness of the half vector $\mathbf{h}$ to the normal $\mathbf{n}$ approximates closeness to a mirror configuration; the [[Dot Product]] $\mathbf{n} \cdot \mathbf{h}$ reaches its maximum of $1$ when they coincide.
- The Phong exponent $p$ controls apparent shininess: larger values (e.g., thousands) sharpen the highlight into a nearly mirror-like appearance, while small values (e.g., tens) give a matte "eggshell" look. When in doubt, the specular color is set to gray (equal red, green, blue).
- Combined with [[Ambient Shading]], the full local illumination model is $L = k_a I_a + k_d I \max(0, \mathbf{n} \cdot \mathbf{l}) + k_s I \max(0, \mathbf{n} \cdot \mathbf{h})^p$.
- By the superposition property of light, the contributions of multiple light sources are simply summed, extending the model to $N$ lights by summing the diffuse and specular terms over all lights.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=98&annotation=MXYW8TWV)
