---
tags:
  - statistics
  - mathematical_statistics
  - cryoEM
---

# Definition
> [!info] Multi-Target Detection (MTD)[^1]
> Estimate a signal $x \in \mathbb{R}^L$ that occurs several times at unknown locations in one long noisy measurement:
> $$
> \begin{align}
> y = x * s + \varepsilon, \qquad s \in \{0, 1\}^{N - L + 1}, \qquad \varepsilon \sim \mathcal{N}(0, \sigma^2 I),
> \end{align}
> $$
> where the ones of $s$ mark the occurrences (a blind deconvolution problem). Estimating $s$ is the analogue of [[Particle Picking]]. At low SNR, detection fails, so $x$ must be estimated **without** estimating $s$.

![[Multi-Target Detection Example.png]]

# Properties
- **Recovery without detection.** Under suitable generative models of $s$ (e.g. well-separated occurrences), $x$ can be recovered provably, **at any noise level**, from the autocorrelations of $y$ up to third order ([[Bispectrum]]). Experiments suggest this extends to mixtures $y = \sum_k x_k * s_k + \varepsilon$.
- **A model of a whole micrograph.** Each occurrence is a random projection $x = h * P(R_\omega\varphi)$ with $\omega$ drawn from a distribution on $SO(3)$. This makes MTD a framework for reconstructing $\varphi$ directly from micrographs, which could in principle break the particle-size limit that detection imposes.
- **Status.** A full analysis was lacking in 2020. Since then, 3D reconstruction directly from simulated micrographs by autocorrelation analysis and approximate EM has been demonstrated[^2], and the sample complexity of MTD has been studied[^3]. Application to experimental data remains open ([[Open Problems in Cryo-EM]]).
- **MTD vs. [[Multi-Reference Alignment|MRA]].** MTD models the micrograph **before** picking (unknown locations $s$, many copies per measurement). MRA models the particle images **after** picking (one copy per observation, unknown group element). If the copies can be detected, MTD reduces to MRA by windowing around them. If not (small particles, low SNR), MTD is the faithful model, and methods based on its autocorrelations aim to recover the structure without ever locating the particles. In the cryo-EM version each copy is itself a random projection, so MTD contains MRA ([[Cryo-EM Forward Model]]).

# Questions
> [!question]- Why do autocorrelations of the whole measurement give information about $x$ without locating the occurrences?
> Suppose the occurrences are separated by at least $L$. For lags $|\ell| < L$, each product $y[n]y[n+\ell]$ either lies within one occurrence or involves only noise. Averaging over $n$ gives $\mathbb{E}\big[\tfrac1N\sum_n y[n]y[n+\ell]\big] = \gamma\, a_x[\ell] + \sigma^2\delta[\ell]$, where $\gamma = M/N$ is the number of occurrences per sample and $a_x[\ell] = \sum_n x[n]x[n+\ell]$ is the autocorrelation of $x$. The locations enter only through $\gamma$. The same holds for third-order autocorrelations. As $N\to\infty$, these averages concentrate at any $\sigma$, and the higher-order autocorrelations determine $x$.

[^1]: [Bendory et al., 2020, p. 21](zotero://open-pdf/library/items/N4ZIHINK?page=21&annotation=VHTISTK8)
[^2]: [Expectation-Maximization for Structure Determination Directly from Cryo-EM Micrographs (arXiv:2303.02157)](https://arxiv.org/abs/2303.02157)
[^3]: [A note on the sample complexity of multi-target detection (arXiv:2501.11980)](https://arxiv.org/abs/2501.11980)
