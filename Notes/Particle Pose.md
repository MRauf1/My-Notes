---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Particle Pose[^1]
> The pose of copy $i$ of a [[Macromolecule|macromolecule]] is the element $g_i = (R_i, t_i) \in SE(3)$ of the [[Special Euclidean Group]] that carries a reference map $f_{\text{ref}}$ onto that copy, in tomogram coordinates ($x, y$ in the plane of the untilted slab, $z$ along the $0^\circ$ beam):
> $$
> \begin{align}
> v_i \approx g_i \cdot f_{\text{ref}}, \qquad (g_i \cdot f)(x) = f\big(R_i^{\top}(x - t_i)\big).
> \end{align}
> $$
> $R_i = I$ means the copy has the same orientation as the reference.

**The pose rotation $R_i$ is not the tilt $R_\theta$.** The tilt rotates the whole slab, is known from the stage, is shared by every molecule in an image, and spans one axis over about $\pm 60^\circ$. The pose rotation belongs to one copy, is unknown and must be estimated, and can be anything in $SO(3)$, since molecules freeze in random orientations.

# Properties
- **Gauge freedom.** Replacing $f_{\text{ref}}$ by $Q \cdot f_{\text{ref}}$ for any $Q \in SO(3)$ turns every pose into $R_i Q^{\top}$ and leaves the fit unchanged. Only relative orientations $R_i R_j^{\top}$ are determined by the data. By convention the gauge is fixed so the reference looks natural, e.g. with a symmetry axis along $z$.
- It is reported as Euler angles; software packages differ on the axis convention.
- **How the pose is used.** In [[Single-Particle Analysis]], only $R_i$ and the in-plane shift $t_i \in \mathbb{R}^2$ are observable: 5 parameters, found by 2D–3D registration of one projection. In [[Cryo-Electron Tomography]], $t_i \in \mathbb{R}^3$ is fully observable, and $R_i$ is found by 3D–3D registration of a subtomogram. Each view is a slice in the molecule frame ([[Cryo-EM Reference Frames]]).
- Beyond the global rotation gauge, projections also cannot fix the hand of the structure ([[Handedness Ambiguity]]).
- Estimating poses is the alignment step of [[Subtomogram Averaging]] and [[Single-Particle Analysis]].

# Questions
> [!question]- If the reference has a symmetry group $H \le SO(3)$ ($h \cdot f_{\text{ref}} = f_{\text{ref}}$ for all $h \in H$), how well is $R_i$ determined?
> Only up to right multiplication by $H$: $(R_i h) \cdot f_{\text{ref}} = R_i \cdot (h \cdot f_{\text{ref}}) = R_i \cdot f_{\text{ref}}$, so $R_i$ and $R_i h$ explain the data equally well. The identifiable object is the coset $R_i H$. On top of this, the global gauge $Q$ makes only the relative orientations meaningful.

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
