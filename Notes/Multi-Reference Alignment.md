---
tags:
  - statistics
  - mathematical_statistics
  - cryoEM
---

# Definition
> [!info] Multi-Reference Alignment (MRA)[^1]
> Let $G$ be a known compact group acting on a signal space (e.g. band-limited signals in $\mathbb{R}^L$), and $T_i$ known linear operators. Observe
> $$
> \begin{align}
> y_i = T_i(g_i \circ x) + \varepsilon_i, \qquad g_i \in G \text{ unknown}, \qquad \varepsilon_i \sim \mathcal{N}(0, \sigma^2 I), \qquad i = 1, \dots, N.
> \end{align}
> $$
> The task is to estimate $x$. The distribution of $y$ is unchanged if $x$ is replaced by $g\circ x$ for a fixed $g$, so only the **orbit** $\{g \circ x : g \in G\}$ of $x$ under the [[Group Action|group action]] is identifiable.

**Cryo-EM is a special case.** With perfect particle picking, $G = SO(3)$, and $T_i$ projects along $z$, convolves with the CTF and samples on the pixel grid ([[Cryo-EM Image Formation Model]]). The global rotation ambiguity of [[Particle Pose]] is exactly the orbit ambiguity.

![[Multi-Reference Alignment Example.png]]

# Properties
- **Simplest instance**: 1D signals under cyclic shifts, $G = \mathbb{Z}/L$, $T = I$ (figure).
- **Other instances**: structure from motion, SLAM in robotics, specimen populations, optical trapping, denoising permuted data.
- **Alignment fails at low SNR.** Estimate $g_i$ by template matching against the true $x$. As $\sigma \to \infty$, the correlation peak becomes uniformly distributed on the group, for *any* estimator. For the rotation of a single signal, the Cramér–Rao bound ([[Rao-Cramér Lower Bound]]) is proportional to $\sigma^2$ and independent of $N$: more observations never pin down the individual $g_i$. The same holds in cryo-EM, where at high noise the correlation over $SO(3)$ has no salient peak.
- **So estimate $x$ without estimating the $g_i$**: by [[Cryo-EM Maximum Likelihood Reconstruction|marginalized likelihood]], or by invariants and moments ([[Kam's Method]], [[Bispectrum]]). The achievable rates are given by the [[Orbit Recovery Sample Complexity]].
- **MRA vs. [[Multi-Target Detection|MTD]].** MRA models cryo-EM **after** particle picking: each observation holds exactly one, roughly centred copy, and the nuisance is its group element (rotation plus small shift). MTD models the raw micrograph **before** picking: one long measurement with many copies at unknown locations. When detection succeeds, MTD reduces to MRA (find the copies, box them out); picking is that reduction. At low SNR detection fails, so MRA describes data one cannot actually obtain, while MTD still describes the measurement. The full cryo-EM micrograph is MTD over locations layered on MRA over rotations ([[Cryo-EM Forward Model]]).

# Questions
> [!question]- Why can $x$ only be recovered up to its orbit?
> If $x' = g\circ x$, then $g_i \circ x' = (g_i g)\circ x$. Since $g_i$ is unknown (and, for a uniform distribution, so is $g_i g$), the observations from $x'$ have the same distribution as those from $x$. No estimator can distinguish distributions that are identical.

> [!question]- If no individual $g_i$ can be estimated at low SNR, why can $x$ still be estimated consistently?
> Each $g_i$ is a new nuisance parameter with fixed information per observation, so its error never shrinks (the Cramér–Rao bound for it is independent of $N$). But $x$ is a fixed parameter shared by all observations. Quantities whose expectations do not depend on the $g_i$, such as invariant moments (power spectrum, bispectrum) or the marginalized likelihood, average the noise down as $N \to \infty$. This is the same incidental-parameter split as in the [[Neyman–Scott Problem]].

[^1]: [Bendory et al., 2020, p. 20](zotero://open-pdf/library/items/N4ZIHINK?page=20&annotation=KA58DCEN)
