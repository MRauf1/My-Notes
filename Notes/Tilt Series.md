---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Tilt Series[^1]
> A sequence of images of the same field of a [[Cryo-EM Specimen|specimen]], each recorded after rotating the specimen by a known angle $\theta$ about a fixed **tilt axis** perpendicular to the beam. In specimen coordinates, with the beam along $z$ at $\theta = 0$ and the tilt axis along $y$, the tilt is
> $$
> \begin{align}
> R_\theta = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}, \qquad |\theta| \le \alpha \approx 60^\circ\text{–}70^\circ,
> \end{align}
> $$
> usually in steps of $1^\circ$–$3^\circ$, with the total electron dose split across the images. Each image is a projection ([[Projection Approximation]]) along the beam direction $R_\theta^{\top} e_z$ as seen from the specimen.

**Rotation about $y$ moves points in the $x$–$z$ plane.** The tilt axis lies in the slab's $x$–$y$ plane and is perpendicular to the beam. The slab normal makes angle $\theta$ with the beam, so the beam meets the slab at a varying angle.

![[Cryo-ET Tilt Series Frame.png]]
![[Cryo-ET Tilt Geometry.png]]

# Properties
- **Single axis.** The holder rotates about its own long axis, so arbitrary tilt axes are not possible. **Dual-axis** tomography rotates the grid $90^\circ$ in its plane and records a second series.
- **Path length.** A beam line crosses a slab of thickness $d$ over a length $L(\theta) = d/\cos\theta$ (the coordinate $p \cdot n$ changes at rate $\cos\theta$ along the beam). This doubles at $60^\circ$ and is unbounded as $\theta \to 90^\circ$. Combined with the exponential attenuation and multiple scattering in the [[Projection Approximation]] (and grid bars shadowing the field at high tilt), this caps $\alpha$ and produces the [[Missing Wedge]].
- **Parallax encodes depth.** A particle at specimen position $(x, y, z)$ lands on the detector at $(x\cos\theta + z\sin\theta,\; y)$. The $z\sin\theta$ term shifts particles at different depths by different amounts. This relative shift, not refraction, is why the same particle appears at different detector positions.
- **Tilt-series alignment.** Unwanted rigid shifts (tilt axis not exactly at the specimen height, stage drift, beam-induced motion) are removed before reconstruction, using gold fiducials or patch tracking.
- **Dose-symmetric order** ($0, +\Delta, -\Delta, +2\Delta, \dots$) is the usual collection order, so that the least-damaged images are the low-tilt ones.
- Reconstructing from a tilt series gives a [[Tomogram]].

[^1]: [Cryogenic electron tomography (Wikipedia)](https://en.wikipedia.org/wiki/Cryogenic_electron_tomography)
