---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] 3D Classification[^1]
> Modelling discrete [[Conformational Heterogeneity]] with a [[Mixture Distribution|mixture model]] of $K$ structures:
> $$
> \begin{align}
> v_i = g_i \cdot f_{c_i} + \varepsilon_i, \qquad c_i \in \{1, \dots, K\},
> \end{align}
> $$
> with both the class $c_i$ and the [[Particle Pose]] $g_i$ latent. The structures $f_1, \dots, f_K$ are fitted by maximum likelihood (or MAP) with the [[Expectation-Maximization Algorithm]], marginalizing jointly over classes and poses. Each class is then averaged separately.

# Properties
- Each class has only about $N/K$ copies, so its noise reduction is about $\sqrt{N/K}$ rather than $\sqrt{N}$.
- *Focused* classification masks one region, so variability elsewhere does not dominate.
- In tomography the likelihood must include each copy's [[Missing Wedge]]; otherwise classes separate by orientation.
- **Limits as $K$ grows.** Each class gets fewer images, assignment becomes harder, and cost grows linearly in $K$. In practice: classify with small $K$, discard bad classes, then reclassify hierarchically, often with masks. The amount of manual tweaking puts reliability and reproducibility in question ([[Open Problems in Cryo-EM]]).

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
