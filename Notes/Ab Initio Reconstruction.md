---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Ab Initio Reconstruction[^1]
> In [[Single-Particle Analysis]], the estimation of a first 3D structure $f$ from particle images with **unknown poses and no starting model**. It is the non-convex problem of jointly recovering $f$ and the [[Particle Pose|poses]] $\{R_i, t_i\}$, or of recovering $f$ while avoiding the poses entirely. Its output initializes refinement.

# Types
- [[Common Lines]]: relative orientations from intersections of central slices, usually on class averages.
- Stochastic optimization over $f$ with pose search or marginalization, e.g. stochastic gradient descent on the marginal likelihood.
- [[Kam's Method]] (method of moments): pose-free, from image moments.
- Amortized pose estimation: a network maps each image to its pose.

# Properties
- The result is determined only up to a global rotation (the gauge of [[Particle Pose]]) and the [[Handedness Ambiguity]].
- The same subproblem exists for heterogeneous ensembles, where the poses and the conformations are unknown together ([[Conformational Heterogeneity]]).
- **SGD.** The marginal log-posterior is a sum of per-image terms, $f(\varphi) = \sum_i \big(\log\Pr(I_i\mid\varphi) + \tfrac1n\log\Pr(\varphi)\big)$, so minibatch [[Stochastic Gradient Descent]] applies. Its noise is believed to help escape local optima, and in practice it is nearly insensitive to initialization, even random. Because it fluctuates rather than converging, it gives low-resolution models (to about $10$ Å) that seed [[Iterative Refinement (Cryo-EM)]].

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
