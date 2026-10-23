---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Intrinsic Dimension[^1]
> The number of degrees of freedom $k$ needed to describe a dataset in $\mathbb{R}^D$ locally: the dimension of the [[Manifold|manifold]] on which it lies ([[Manifold Hypothesis]]). For a distribution $P$ that is not exactly on a manifold, the local intrinsic dimension at $\mathbf{x}$ is the exponent in the small-ball scaling
> $$
> \begin{align}
> P\left(B_r(\mathbf{x})\right) \approx c(\mathbf{x})\, r^{k}, \qquad \text{i.e.} \qquad k(\mathbf{x}) = \lim_{r \to 0} \frac{\log P\left(B_r(\mathbf{x})\right)}{\log r}
> \end{align}
> $$
> A global version is the **correlation dimension** $\nu = \lim_{r \to 0} \log C(r) / \log r$ with $C(r) = P(\|\mathbf{X} - \mathbf{X}'\| < r)$ for independent $\mathbf{X}, \mathbf{X}' \sim P$.

# Properties
- **Link to density blow-up**: since $\operatorname{vol}(B_r) = \omega_D r^D$, the density quotient behaves as $P(B_r(\mathbf{x})) / \operatorname{vol}(B_r(\mathbf{x})) \propto r^{k - D}$. If $k = D$ this tends to a finite [[Probability Density Function|pdf]] value; if $k < D$ it diverges, so $P$ is [[Mutually Singular Measures|singular]] with respect to [[Lebesgue Measure]] and has no density.
- Agrees with the Hausdorff dimension of the support for well-behaved sets, and with $k$ for distributions with a positive continuous density on a smooth $k$-manifold.
- **Levina-Bickel estimator**: modeling neighbor counts near $\mathbf{x}$ as a Poisson process with rate $\propto r^{k}$ and applying [[Maximum Likelihood Estimation|maximum likelihood]] gives, with $T_j(\mathbf{x})$ the distance to the $j$-th nearest neighbor,[^2]
$$
\begin{align}
\hat{k}_K(\mathbf{x}) = \left[\frac{1}{K - 1}\sum_{j=1}^{K-1} \log\frac{T_K(\mathbf{x})}{T_j(\mathbf{x})}\right]^{-1}
\end{align}
$$
  averaged over data points for a global estimate.
- **Linear vs. nonlinear**: [[Principal Component Analysis]] counts the dimensions of the best-fitting linear subspace, which overestimates $k$ for curved manifolds; nearest-neighbor estimators measure the nonlinear dimension.
- **Scale dependence**: estimates depend on the scale $r$ probed. Below the noise level, data looks $D$-dimensional; at the scale of semantic variation, it looks $k$-dimensional. It can also vary across the data (e.g. between classes).[^3]
- **Learning**: the sample complexity of learning and the difficulty of generalization scale with the intrinsic rather than the ambient dimension, which is how methods escape the [[Curse of Dimensionality]].[^3]

[^1]: Supplementary notes provided by the creator; Grassberger & Procaccia (1983) in `REFERENCES.md`.
[^2]: Levina & Bickel (2004) in `REFERENCES.md`.
[^3]: Pope et al. (2021); Brown et al. (2023) in `REFERENCES.md`.
