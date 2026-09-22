---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Graphics Pipeline)[^1]
> The sequence of operations, starting with geometric objects and ending by updating pixels in an image, used to implement [[Object-Order Rendering]]. Objects are always described by sets of vertices, and the pipeline is commonly organized into four stages: vertex processing, rasterization, fragment processing, and blending.

# Properties
- Also called rendering by rasterization; rasterization-based systems are also called scanline renderers.
- Stages: [[Vertex Processing]] transforms incoming vertices and their attributes; [[Rasterization]] breaks each primitive into [[Fragment|fragments]]; fragment processing computes a color and depth per fragment (possibly via [[Per-Fragment Shading]]); [[Fragment Blending]] combines the fragments at each pixel into a final color, producing the framebuffer image.
- The most common geometric operation is mapping vertex positions from object space to screen space via matrix transformations (see [[Viewing Transformation]]); the most common per-pixel operation is [[Hidden Surface Removal]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=174&annotation=U5MIX8AX)
