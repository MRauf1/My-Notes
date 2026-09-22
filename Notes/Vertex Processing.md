---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Vertex Processing)[^1]
> The first stage of the [[Graphics Pipeline]]: preparing a primitive's vertices for [[Rasterization]] by applying the modeling, viewing, and projection transformations to map each vertex's position from object space into screen space (pixel coordinates), while transforming other per-vertex attributes (colors, surface normals, texture coordinates) as needed.

# Properties
- Must complete, along with [[Clipping (Computer Graphics)|clipping]], before rasterization, since a primitive's vertices must be in screen coordinates with all attributes known before the rasterizer can run.
- Position transformation is carried out by the [[Viewing Transformation]] pipeline, implemented using [[Homogeneous Coordinates]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=186&annotation=JQ46EEGK)
