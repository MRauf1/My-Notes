---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Kam's Method (Method of Moments for Cryo-EM)[^1]
> Pose-free [[Ab Initio Reconstruction]]. Assume particle orientations uniform on $SO(3)$, and average low-order moments of the images, such as their autocorrelation (second moment), over all particles. These averages are rotation-invariant functionals of $f$, computable without estimating any pose. Expand $\hat f$ in spherical harmonics, $\hat f(k) = \sum_{\ell, m} a_{\ell m}(|k|)\, Y_\ell^m(k/|k|)$. Then the averaged second moment determines, for each degree $\ell$, the Gram matrix
> $$
> \begin{align}
> C_\ell(r_1, r_2) = \sum_{m=-\ell}^{\ell} a_{\ell m}(r_1)\, \overline{a_{\ell m}(r_2)},
> \end{align}
> $$
> i.e. the coefficient matrix $A_\ell = [a_{\ell m}(r)]$ up to an unknown unitary (for real $f$, orthogonal) matrix $O_\ell$ acting on $m$: $A_\ell \mapsto A_\ell O_\ell$.

# Properties
- **Second moments are not enough.** Recovering the $O_\ell$ needs extra information: third moments, a reference, or priors such as positivity or sparsity ("orthogonal matrix retrieval")[^2].
- **Noise and sample complexity.** The $q$-th moment is estimated with variance about $\sigma^{2q}/N$, so the lowest identifying moment sets the rate ([[Orbit Recovery Sample Complexity]]). With uniform rotations, the third moment determines the structure uniquely, giving $\sigma^6$. With a generic non-uniform distribution, the second moment suffices, giving $\sigma^4$; an efficient provable algorithm for this case appeared in 2026[^4].[^3]
- **One pass.** The moments need a single pass over the data, so they can be accumulated on the fly during data collection. The CTF and shifts can be included in the moment equations.
- **Heterogeneity.** For a heterogeneous ensemble, second moments of the images encode the mean and the 3D covariance of the structures ([[Cryo-EM Covariance Estimation]]).

[^1]: [Kam (1980), The reconstruction of structure from electron micrographs of randomly oriented particles, J. Theor. Biol. 82:15–39](https://doi.org/10.1016/0022-5193(80)90088-0)
[^2]: [Bhamre, Zhang & Singer, Orthogonal Matrix Retrieval in Cryo-Electron Microscopy](https://arxiv.org/abs/1412.0494)
[^3]: [Bendory et al., 2020, p. 15](zotero://open-pdf/library/items/N4ZIHINK?page=15&annotation=36G72R3M)
[^4]: [Bendory, Edidin, Katz, Kreymer & Sharon (2026), Provable orbit recovery over SO(3) from the non-uniform second moment (arXiv:2602.20590)](https://arxiv.org/abs/2602.20590)
