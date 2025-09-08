---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition 1 (Plenoptic Function)
> $$
> \begin{align}
> P(\theta, \Phi, \lambda, t, X, Y, Z)
> \end{align}
> $$
> where $P$ is the [[Light|light]] intensity of a light [[Ray|ray]] passing through the world location $(X, Y, Z)$ in the direction given by angle $(\theta, \Phi)$ with [[Wavelength|wavelength]] $\lambda$ and [[Time|time]] $t$.[^1]

The plenoptic function contains all the information needed to describe the complete pattern of light rays that fills the space.

It does not include information about the observer.

Observer typically has access only to a small slice of the plenoptic function rather than it in its completeness.

[^1]: https://visionbook.mit.edu/taxonomy.html