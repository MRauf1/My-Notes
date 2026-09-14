---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Computational Camera)[^1]
> An imaging system whose recorded sensor intensities need not resemble an interpretable image, unlike a conventional [[Pinhole Camera|pinhole]] or [[Lens|lens-based]] camera. Because the optical elements of such systems are often linear in their response to light, they can be described using linear algebra as a [[Camera as Linear System|linear system]], which provides a way to computationally recover an interpretable image from the recorded data.

# Properties
- Includes medical and astronomical imaging systems, whose raw sensor data generally requires computational processing before it resembles a picture of the scene.
- Examples include the [[Pinspeck Camera]] and the [[Corner Camera]], which recover images from measurements that do not themselves look like images.
- Contrasts with a [[Pinhole Camera]] or conventional [[Lens|lens-based]] camera, for which the [[Imaging Matrix]] is approximately the identity, so the sensor measurements already form a recognizable image.

[^1]: [MIT Vision Book - The Camera as a Linear System](https://visionbook.mit.edu/camera_as_linsys.html)
