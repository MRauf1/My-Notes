---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Common Lines[^1]
> In [[Single-Particle Analysis]], the Fourier transforms of two particle images $I_i, I_j$ are the slices of $\hat f$ on the central planes $\Pi_i = R_i^{\top} e_z^{\perp}$ and $\Pi_j = R_j^{\top} e_z^{\perp}$ ([[Fourier Slice Theorem]]). If $\Pi_i \neq \Pi_j$, they intersect in a line through the origin, the **common line**, along which both images must agree:
> $$
> \begin{align}
> \hat I_i\big(r\, c_{ij}\big) = \hat I_j\big(r\, c_{ji}\big), \qquad r \in \mathbb{R},
> \end{align}
> $$
> where $c_{ij}$ and $c_{ji}$ are the line's directions in each image's own 2D coordinates. The pair $(c_{ij}, c_{ji})$ is determined by the relative rotation $R_i R_j^{\top}$.

# Properties
- **Ab initio orientation.** Common lines among triples of images determine their relative orientations, up to a global rotation and the [[Handedness Ambiguity]]. This is a classical route to [[Ab Initio Reconstruction]] (angular reconstitution, synchronization over $SO(3)$).
- **Noise.** At raw-particle SNR, common lines cannot be detected reliably. In practice they are applied to class averages ([[2D Classification]]).
- In [[Cryo-Electron Tomography]], the analogous object for a tilt series is the shared $k_y$ hinge, which every slice of the fan contains ([[Cryo-EM Reference Frames]]).
- **Angular reconstitution.** A pair of images fixes two of the three Euler angles of their relative rotation, and a third image fixes the rest. Assigning further images one at a time is noise-sensitive and accumulates error. [[Rotation Synchronization]] uses all pairs at once instead.[^2]
- **Symmetry.** A symmetric molecule has several common lines per pair of images.

# Questions
> [!question]- Why do common lines fail for 2D objects (1D projections)?
> By the Fourier slice theorem, a 1D projection of a 2D object gives $\hat f$ on a central **line** of the 2D Fourier plane. Two distinct central lines intersect only at the origin, where every projection has the same value, $\hat f(0) = \int f$. So the intersection carries no information about the relative angle. In 3D, central planes intersect in a whole line, along which the images must agree, and that is informative.

> [!question]- Why do two images determine only one angle of their relative orientation, while three determine it fully (up to handedness)?
> Two distinct central planes share exactly one line, so a pair fixes the directions $c_{ij}$ and $c_{ji}$ in each image. The remaining freedom is the dihedral angle between the planes about that line: rotating $\Pi_j$ about the common line keeps it a common line. With three images, the three common lines must be consistent. The dihedral angles of the three planes are then fixed by the angles between the common lines measured within each image (spherical triangle geometry), which pins the relative rotations, up to a reflection that produces the same angles.

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
[^2]: [Bendory et al., 2020, p. 13](zotero://open-pdf/library/items/N4ZIHINK?page=13&annotation=9WLSFAJ4)
