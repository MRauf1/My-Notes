---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Rasterization)[^1]
> The process of finding all the pixels in an image that are occupied by a geometric [[Primitive (Computer Graphics)|primitive]]; the central stage of the [[Graphics Pipeline]]. For each incoming primitive, the rasterizer enumerates the pixels it covers and interpolates per-vertex attribute values across it (see [[Gouraud Interpolation]]), producing one [[Fragment]] per covered pixel.

# Properties
- Lines are rasterized based on implicit or parametric line equations (e.g., the midpoint algorithm for implicit lines), enumerating the pixels the line passes through.
- For triangles, the standard convention is to draw a pixel if and only if its center's [[Barycentric Coordinates]] are all in the open interval $(0,1)$; this pixel-center rule makes triangles that share vertices and edges rasterize without holes and without the final image depending on the order in which adjacent triangles are drawn.
- Object-order rendering is also called rendering by rasterization, or (for rasterization-based systems) scanline rendering.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=174&annotation=U5MIX8AX)
