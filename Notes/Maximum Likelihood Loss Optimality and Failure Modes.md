---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Maximum Likelihood Loss Optimality and Failure Modes[^1]
> Negative log-likelihood losses ([[Maximum Likelihood Loss Function Recipe]]) are optimal only conditionally: under correct model specification and large samples they are asymptotically efficient, KL-minimizing, and strictly proper; outside those assumptions they can fail badly.

# Properties
## Senses of optimality
- **Asymptotic efficiency**: under [[Maximum Likelihood Regularity Conditions|regularity conditions]], the [[Maximum Likelihood Estimation|MLE]] is consistent and [[Maximum Likelihood Estimator Asymptotic Normality|asymptotically normal]], $\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_0) \xrightarrow{D} \mathcal{N}(\mathbf{0}, \mathbf{I}(\boldsymbol{\theta}_0)^{-1})$ with [[Fisher Information Matrix]] $\mathbf{I}$, and no regular estimator has lower asymptotic covariance (Hájek-Le Cam).
- **Information-theoretic**: minimizing the expected NLL equals minimizing $D_{\mathrm{KL}}(p_{\text{data}} \| p_{\boldsymbol{\theta}})$ ([[Kullback-Leibler Divergence]]), so if $p_{\text{data}}$ is in the model family the minimizer recovers it.
- **Strict propriety**: the NLL is the logarithmic score, a strictly [[Proper Scoring Rule|proper scoring rule]], rewarding calibrated probabilities.

## Failure modes
- **Outliers**: $\nabla_{\boldsymbol{\theta}} L = -\nabla_{\boldsymbol{\theta}} p(\mathbf{x}; \boldsymbol{\theta}) / p(\mathbf{x}; \boldsymbol{\theta})$ diverges as $p \to 0$, so a single gross outlier in a low-density region can dominate training (unbounded influence; e.g. the Gaussian mean has breakdown point zero).
- **Mass-covering under misspecification**: forward KL penalizes $p_{\boldsymbol{\theta}}(\mathbf{x}) \approx 0$ wherever $p_{\text{data}}(\mathbf{x}) > 0$ infinitely, so a misspecified model becomes over-diffuse, spreading over all modes (e.g. blurry generative samples), whereas reverse KL is mode-seeking.
- **Finite samples**: MLE can be biased (e.g. $\hat{\sigma}^2_{\mathrm{ML}}$ is low by a factor $\frac{N-1}{N}$, [[Normal Distribution Maximum Likelihood Estimation]]), inconsistent when nuisance parameters grow with $N$ (Neyman-Scott paradox), and, for [[Overparameterized Model|overparameterized]] networks, memorizes data and becomes overconfident ([[Overfitting]]).
- **Decision misalignment**: it minimizes surprisal, not task cost; asymmetric real-world costs require [[Minimum Expected Loss Decision Rule|decision-theoretic]] treatment.
- Alternatives targeting each failure mode are listed in [[Loss Function Taxonomy]].

[^1]: Supplementary notes provided by the creator.
