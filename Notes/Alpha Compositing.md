---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition (Alpha Compositing)[^1]
> To composite a foreground color $c_f$ over a background color $c_b$, where $\alpha$ is the fraction of the pixel covered by the foreground (the pixel coverage), the composited color is
> $$
> \begin{align}
> c = \alpha c_f + (1 - \alpha) c_b.
> \end{align}
> $$

# Properties
- For an opaque foreground, $\alpha$ is the fraction of the pixel's area covered by the foreground object, with the remaining $(1-\alpha)$ covered by the background.
- For a transparent foreground (e.g., paint on glass or tracing paper), the foreground blocks a fraction $(1-\alpha)$ of the light coming through from the background and contributes a fraction $\alpha$ of its own color.
- Since the foreground and background weights sum to $1$, the composited color is unchanged when the two layers share the same color.
- The coverage value $\alpha$ for every pixel of an image is stored as an [[Alpha Channel]] or alpha mask.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=68&annotation=6QKT4SFD)
