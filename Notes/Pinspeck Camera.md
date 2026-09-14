---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Pinspeck Camera)[^1]
> A [[Computational Camera]] formed by a small occluder that blocks part of the light reaching the sensor, rather than a pinhole that lets light through at only one point. It is complementary to a wide-aperture [[Pinhole Camera]]: its [[Imaging Matrix]] is, up to scale, the identity matrix minus the imaging matrix of the corresponding pinhole camera.

# Properties
- Records a signal with a large constant offset, the total light that would arrive with no occluder, minus a small, shadow-induced fluctuation caused by the occluder, rather than an image that directly resembles the scene.
- Has been used in practice to recover scene information from the faint shadow an occluder casts.

[^1]: [MIT Vision Book - The Camera as a Linear System](https://visionbook.mit.edu/camera_as_linsys.html)
