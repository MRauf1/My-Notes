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
- **Strict propriety**: the NLL is the logarithmic score, a strictly [[Proper Scoring Rule|proper scoring rule]], rewarding calibrated probabilities. It is essentially the only *local* strictly proper scoring rule (depending only on the probability assigned to the observed outcome), up to affine transformation.[^2]
- **Efficiency bound**: asymptotically it attains the [[Rao-Cramér Lower Bound]], and it is invariant under reparameterization ([[Maximum Likelihood Estimator Invariance]]).
- **Compression**: expected NLL is cross-entropy, i.e. expected code length, which is why generative models report bits per dimension ([[Noiseless Coding Theorem]]).[^2]
- **Computational**: for i.i.d. data the log-likelihood is a sum over data points, so minibatch [[Stochastic Gradient Descent|SGD]] gives unbiased gradient estimates; it needs no samples from the model (unlike [[Generative Adversarial Network|GANs]]) and no adversary or inner optimization.[^2]
- **Universal recipe**: choose an output distribution and minimize its NLL; this single recipe yields least squares, logistic regression, and softmax cross-entropy ([[Maximum Likelihood Loss Function Recipe]]).[^2]

These advantages make MLE the default; its failures arise when its assumptions (correct specification, enough data, and data and model having densities with respect to the same reference measure) break.

## Failure modes
- **Outliers**: $\nabla_{\boldsymbol{\theta}} L = -\nabla_{\boldsymbol{\theta}} p(\mathbf{x}; \boldsymbol{\theta}) / p(\mathbf{x}; \boldsymbol{\theta})$ diverges as $p \to 0$, so a single gross outlier in a low-density region can dominate training (unbounded influence; e.g. the Gaussian mean has breakdown point zero).
- **Mass-covering under misspecification**: forward KL penalizes $p_{\boldsymbol{\theta}}(\mathbf{x}) \approx 0$ wherever $p_{\text{data}}(\mathbf{x}) > 0$ infinitely, so a misspecified model becomes over-diffuse, spreading over all modes (e.g. blurry generative samples), whereas reverse KL is mode-seeking.
- **Degenerate (unbounded) densities**: for continuous models the likelihood is a [[Probability Density Function|density]], i.e. mass per unit volume, which is unbounded (unlike a [[Probability Mass Function|pmf]], bounded by $1$). If the data distribution has no density, because it has point masses (quantized data) or lies on a lower-dimensional manifold of zero volume, a flexible model can concentrate its mass into a vanishing volume around the data and drive the likelihood to $+\infty$ without learning the distribution (e.g. a Gaussian mixture component collapsing $\sigma \to 0$ onto one point; [[Normalizing Flow|normalizing flows]] on manifold-supported data, called [[Manifold Overfitting|manifold overfitting]]; [[Manifold Hypothesis]]).[^2] The root cause is a mismatch of reference measures, not MLE itself: the data distribution is [[Mutually Singular Measures|mutually singular]] with the full-dimensional model (not [[Absolutely Continuous Measure|absolutely continuous]] with respect to [[Lebesgue Measure]]), so $D_{\mathrm{KL}}(p_{\text{data}} \| p_{\boldsymbol{\theta}})$ is infinite or undefined and *every* density-ratio-based objective breaks the same way.
	- **Bayesian inference does not cure it**: the posterior $p(\boldsymbol{\theta} | \mathcal{D}) \propto p(\mathcal{D} | \boldsymbol{\theta})\,p(\boldsymbol{\theta})$ contains the same likelihood and inherits its unboundedness ([[Bayesian Inference]]). A prior can block a specific collapse (e.g. a prior on $\sigma$ in a mixture), which is regularization ([[Maximum a Posteriori Learning|MAP]]), and full Bayesian inference over millions of network weights is intractable anyway.
	- **Remedies** change the data or the objective, not the inference framework: add noise so a density exists ([[Dequantization]], [[Diffusion Model|diffusion]] and denoising score matching); use a divergence that stays finite for mutually singular distributions ([[Wasserstein Distance]], adversarial training); learn the manifold and a density on it separately (injective/manifold flows); or train continuous-time flows by regression instead of likelihood (flow matching).
- **Finite samples**: MLE can be biased (e.g. $\hat{\sigma}^2_{\mathrm{ML}}$ is low by a factor $\frac{N-1}{N}$, [[Normal Distribution Maximum Likelihood Estimation]]), inconsistent when nuisance parameters grow with $N$ (Neyman-Scott paradox), and, for [[Overparameterized Model|overparameterized]] networks, memorizes data and becomes overconfident ([[Overfitting]]).
- **Decision misalignment**: it minimizes surprisal, not task cost; asymmetric real-world costs require [[Minimum Expected Loss Decision Rule|decision-theoretic]] treatment.
- Alternatives targeting each failure mode are listed in [[Loss Function Taxonomy]].

[^1]: Supplementary notes provided by the creator.
[^2]: Supplementary notes provided by the creator; manifold overfitting: Loaiza-Ganem, Ross, Cresswell & Caterini (2022), *Diagnosing and Fixing Manifold Overfitting in Deep Generative Models* ([arXiv:2204.07172](https://arxiv.org/abs/2204.07172)).
