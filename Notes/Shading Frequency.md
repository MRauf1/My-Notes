---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Shading Frequency)[^1]
> The rate, relative to pixel size, at which a shading computation is evaluated; it determines whether [[Per-Vertex Shading]] (a low shading frequency, interpolated across each primitive) or [[Per-Fragment Shading]] (a high shading frequency, up to one evaluation per pixel) is adequate to reproduce a given effect.

# Properties
- Large-scale shading features (e.g., diffuse shading on a smoothly curved surface) can be evaluated at a low shading frequency and interpolated without visible error.
- Small-scale features (sharp highlights, fine [[Texture Mapping|texture]] detail) require a high shading frequency — at least one sample per pixel — to appear crisp rather than blurred or missed entirely.
- A high shading frequency can still be achieved within the vertex stage, as long as the primitive's vertices are placed close together in image space; otherwise it requires fragment-stage evaluation.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=192&annotation=P2N6PLRG)
