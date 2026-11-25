---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Covariance Estimation[^1]
> Estimation of the mean $\mu$ and [[Covariance Matrix|covariance]] $\Sigma$ of the random structure $f$ in [[Conformational Heterogeneity]], from aligned observations that each see only part of $f$: $y_i = P_i f_i + \varepsilon_i$, with $\varepsilon_i$ white noise of variance $\sigma^2$. Here $P_i$ is copy $i$'s known linear observation operator: a tomographic projection in [[Single-Particle Analysis]], or the projector onto frequencies outside the rotated [[Missing Wedge]] in [[Subtomogram Averaging]]. For orthogonal projectors $P_i$, the moments satisfy
> $$
> \begin{align}
> \mathbb{E}[y_i] = P_i \mu, \qquad \operatorname{Cov}(y_i) = P_i \Sigma P_i + \sigma^2 P_i,
> \end{align}
> $$
> and $\mu$, $\Sigma$ are estimated by least squares over all $i$. The leading eigenvectors of $\Sigma$ are the principal modes of variability ([[Principal Component Analysis]]).

# Properties
- The least-squares normal equations for $\Sigma$ involve the operator $\Sigma \mapsto \sum_i P_i \Sigma P_i$. It is invertible only where the masks jointly cover all pairs of frequencies, which is why diverse poses are needed. It can be inverted iteratively, e.g. by conjugate gradient, where stopping early acts as regularization.
- In the projected eigenbasis, each copy has low-dimensional coordinates, which can then be clustered or used to traverse the conformational landscape.
- **Fourier slice theorem for covariance.** Two non-collinear frequencies, together with the origin, define a unique central plane. The covariance between them is therefore measured only by images whose slice is that plane. Estimating every covariance entry needs **full** coverage of viewing directions, far more than the mean, which needs only every frequency to lie on some slice.
- **Cost.** The covariance is $L^3 \times L^3$ ($O(L^6)$ entries), and both computation and sample size grow quickly in $L$. So it is usually estimated at low resolution. The variance map still shows flexible regions, and the leading eigenvectors still give strong dimension reduction.

# Questions
> [!question]- Why does covariance estimation need full coverage of viewing directions, while mean reconstruction does not?
> The mean needs each frequency $k$ to lie on at least one measured central plane. A covariance entry $\operatorname{Cov}(\hat f(k_1), \hat f(k_2))$ needs both values observed in the same image. Both lie on one central plane only if that plane is $\operatorname{span}(k_1, k_2)$, which is unique for non-collinear $k_1, k_2$. So every plane through the origin must be sampled, i.e. all viewing directions.

> [!question]- Connection: Which missing-data problem is estimating $\Sigma$ from masked copies an instance of, and where does the analogy break?
> **PCA / covariance estimation with missing entries (matrix completion).** The dictionary:
> - an unobserved coordinate corresponds to an unmeasured frequency in $R_i^{\top} W$;
> - a sample's observation pattern corresponds to its mask $P_i$;
> - a random sampling pattern corresponds to random poses spreading the wedges;
> - "every pair of entries is observed often enough" corresponds to the operator $\sum_i P_i \Sigma P_i$ being invertible.
>
> **Where it breaks:** the masks are not random coordinate subsets but rotations of one structured set (a wedge, or a central plane in SPA). They are also not known in advance: they depend on poses that must be estimated from the same data, so the problem is coupled to alignment.

[^1]: [Andén & Singer (2018), Structural Variability from Noisy Tomographic Projections](https://doi.org/10.1137/17M1153509)
