---
tags:
  - statistics
  - mathematical_statistics
  - cryoEM
---

# Definition
> [!info] Orbit Recovery Sample Complexity[^1]
> For [[Multi-Reference Alignment]] with noise level $\sigma$:
> - **High SNR**: the group elements can be estimated (e.g. by [[Rotation Synchronization|synchronization]]), the observations aligned and averaged, and the error variance scales like $1/(N \cdot \mathrm{SNR})$. So $N \propto 1/\mathrm{SNR}$ samples suffice.
> - **Low SNR** ($\sigma \to \infty$): let $q$ be the order of the **first moment that distinguishes** different orbits. Then any estimator's error stays bounded away from zero while $N\cdot\mathrm{SNR}^q$ is bounded. The sample complexity is $N \propto 1/\mathrm{SNR}^q$, i.e. $\sigma^{2q}$ samples.

For **cryo-EM** (perfect picking, no CTF, no shifts):
$$
\begin{align}
N \propto \begin{cases} \sigma^6 \ (q = 3) & \text{uniform rotations}, \\ \sigma^4 \ (q = 2) & \text{generic non-uniform rotations}. \end{cases}
\end{align}
$$

# Properties
- **Why $\sigma^{2q}$.** The $q$-th moment is an average of products of $q$ noisy entries. Its estimate has variance of order $\sigma^{2q}/N$ ([[Kam's Method]]), so resolving differences between signals at order $q$ needs $N \gtrsim \sigma^{2q}$.
- **The cost of low SNR is a polynomial blow-up in the exponent**, not just a constant. This is a central reason cryo-EM needs $10^5$–$10^6$ particles, and why it is hard for small particles.
- **Recent progress (2024–2026)**:
  - an efficient, provable second-moment algorithm for non-uniform rotations[^2];
  - a provable method of moments for cryo-EM at the $\sigma^6$ scale[^3];
  - orbit recovery under the full rigid-motion group, i.e. with shifts[^4];
  - maximum likelihood in the high-noise orbit model, Annals of Statistics 2024[^5].
- The sample complexity of the **full** problem (CTF, shifts, picking, heterogeneity, finite resolution) remains open ([[Open Problems in Cryo-EM]]).

# Questions
> [!question]- Why does a uniform rotation distribution need the third moment, while a generic non-uniform one only needs the second?
> Under uniform rotations, the averaged second moment of the images is rotation-invariant. It determines only the Gram matrices of the spherical-harmonic coefficients of $\hat f$, i.e. $f$ up to an unknown orthogonal matrix per degree $\ell$ ([[Kam's Method]]). A third-order invariant is needed to fix those matrices. A non-uniform distribution breaks the averaging: the second moment then retains orientation-dependent information, which generically determines $f$ (and the distribution) up to a global rotation.

> [!question]- Why does high SNR give $1/\mathrm{SNR}$ while low SNR gives $1/\mathrm{SNR}^q$?
> At high SNR, alignment succeeds, so averaging $N$ aligned copies leaves noise variance $\sigma^2/N$, which is linear in $1/\mathrm{SNR}$. At low SNR, alignment fails, and information about $x$ is only accessible through invariant moments. The lowest informative one, of order $q$, is estimated with variance about $\sigma^{2q}/N$.

[^1]: [Bendory et al., 2020, p. 21](zotero://open-pdf/library/items/N4ZIHINK?page=21&annotation=FNT3YEBI)
[^2]: [Bendory, Edidin, Katz, Kreymer & Sharon (2026), Provable orbit recovery over SO(3) from the non-uniform second moment (arXiv:2602.20590)](https://arxiv.org/abs/2602.20590)
[^3]: [Provable method of moments for cryo-EM (arXiv:2610.17892)](https://arxiv.org/abs/2610.17892)
[^4]: [Orbit recovery under the rigid motions group (arXiv:2512.07405)](https://arxiv.org/abs/2512.07405)
[^5]: Maximum likelihood for high-noise group orbit estimation and single-particle cryo-EM (Annals of Statistics, 2024)
