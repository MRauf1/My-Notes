---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Viewing Transformation)[^1]
> The transformation that maps 3D locations, given as $(x,y,z)$ coordinates in world space, to 2D coordinates in the image, expressed in units of pixels. It depends on the camera's position and orientation, the type of projection, the field of view, and the resolution of the output image.

![[Viewing Transformation Pipeline.png]]

# Properties
- Plays a central role in [[Object-Order Rendering]], which must rapidly find the image-space location of each object in the scene; [[Ray Tracing]] instead works in the opposite direction, generating a ray per pixel via [[Ray Generation]].
- Decomposed into a pipeline of simpler transformations, each moving geometry between named coordinate spaces:
	- **Object space**, the coordinates in which a model is originally defined, mapped by a *modeling transformation* into
	- **World space** (canonical coordinates), the common scene coordinate system, mapped by the [[Camera Transformation]] into
	- **Camera space** (eye space), mapped by a projection transformation ([[Orthographic Projection Matrix]] or [[Perspective Projection Matrix]]) into
	- The **canonical view volume** (clip space / normalized device coordinates), mapped by the [[Viewport Transformation]] into
	- **Screen space** (pixel coordinates).
- Breaking the overall transformation into this sequence isolates what each stage depends on: the camera transformation depends only on camera pose, the projection transformation only on the projection type, and the viewport transformation only on the output image's size and position.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=155&annotation=PV89U52L)
