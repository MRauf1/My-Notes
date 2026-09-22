---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Orthographic View Volume)[^1]
> The axis-aligned box $[l,r] \times [b,t] \times [f,n]$ seen by an orthographic camera looking down the $-z$ direction with its head pointing along $+y$, bounded by the left plane $x=l$, right plane $x=r$, bottom plane $y=b$, top plane $y=t$, near plane $z=n$, and far plane $z=f$.

# Properties
- Because the viewer looks down $-z$ and the entire volume has negative $z$ values, the convention $n > f$ holds: the near plane $z=n$ is closer to the viewer than the far plane $z=f$, even though $f$ is the numerically smaller (more negative) value.
- Mapped into the [[Canonical View Volume]] by the [[Orthographic Projection Matrix]], an instance of the [[Windowing Transformation]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=157&annotation=XHP3AVAI)
