---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Hidden Surface Removal)[^1]
> The problem, addressed during [[Fragment Blending]], of ensuring that surfaces closer to the viewer appear in front of surfaces farther away.

# Properties
- The painter's algorithm — drawing surfaces back-to-front so that nearer surfaces overdraw farther ones — is a straightforward solution but is rarely used in practice.
- The [[Z-Buffer Algorithm]] is the standard, efficient solution used in practice.
- [[Occlusion Culling]] addresses a related goal (avoiding work on invisible geometry) but discards fully-hidden geometry before it is processed at all, rather than resolving visibility per pixel after rasterization.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=188&annotation=TT9CS47R)
