---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Loss Function Taxonomy[^1]
> [[Loss Function|Loss functions]] can be organized by their mathematical formulation into five families:
> 1. **Information-theoretic / likelihood losses**: $-\log p(\mathbf{y} | \mathbf{x}, \boldsymbol{\theta})$ under an assumed parametric family ([[Maximum Likelihood Loss Function Recipe]]).
> 2. **Geometric / norm-based losses**: a distance $d(\mathbf{y}, \hat{\mathbf{y}})$ between point predictions, without explicit probabilistic assumptions.
> 3. **Margin-based classification losses**: functions of the signed margin $z = y f(\mathbf{x})$ with $y \in \{-1, +1\}$.
> 4. **[[Proper Scoring Rule|Proper scoring rules]]**: evaluate a full predicted distribution against the realized outcome.
> 5. **Metric / contrastive losses**: act on relative distances between embeddings rather than fixed targets.

# Types
- **Likelihood**: Gaussian NLL ([[Mean Squared Error]]), Bernoulli NLL ([[Binary Cross-Entropy Loss]]), categorical NLL ([[Cross-Entropy Loss]]), Poisson NLL $\lambda - y\log\lambda$, [[Kullback-Leibler Divergence]]. Best for calibrated probabilistic models when the generative family is known.
- **Geometric**: [[L2 Loss]], [[L1 Loss]], $L_\infty$, [[Minkowski Loss]], Huber loss (quadratic for small residuals, linear for large ones), cosine distance, Wasserstein distance. Used when point predictions suffice.
- **Margin-based**: hinge loss $\max(0, 1 - z)$ (support vector machines; ignores points beyond the margin), logistic loss $\log(1 + e^{-z})$ (smooth convex [[Surrogate Loss Function|surrogate]] for the 0-1 loss), exponential loss $e^{-z}$ (AdaBoost; penalizes negative margins heavily), perceptron loss ([[Perceptron]]). Target the decision boundary rather than posterior probabilities.
- **Scoring rules**: logarithmic score (the NLL), Brier score $\sum_k (p_k - y_k)^2$, continuous ranked probability score $\mathrm{CRPS}(F, y) = \int_{-\infty}^{\infty} (F(t) - \mathbb{1}[t \geq y])^2\, dt$, energy score. Important where calibration and tail risk matter (weather, finance).
- **Contrastive**: contrastive loss, triplet loss, InfoNCE, NT-Xent, CLIP's symmetric cross-entropy. Used for representation learning.

# Properties
- **Unification**: the NLL of every regular [[Exponential Family]] distribution is, up to parameter-independent terms, a [[Bregman Divergence]] between $\mathbf{y}$ and the predicted mean; e.g. squared error (Gaussian), binary cross-entropy (Bernoulli), and generalized KL (Poisson). Choosing an MLE loss amounts to choosing a convex geometry; choosing a non-MLE loss (Huber, hinge, Wasserstein) deliberately departs from the exponential-family assumption to buy robustness, margin separation, or transport geometry.
- **Choosing an alternative to the likelihood loss** by failure mode ([[Maximum Likelihood Loss Optimality and Failure Modes]]):
	- outliers and heavy noise: Huber, Tukey's biweight, $\beta$-divergence, which cap the influence of large residuals;
	- calibration on rare events: Brier score or CRPS, which avoid the logarithm's unbounded tail penalty;
	- class imbalance: [[Focal Loss]];
	- distribution shift: Wasserstein distributionally robust optimization, minimizing the worst-case loss in a transport ball around the empirical data ([[Robustness to Distributional Shift]]);
	- misspecified generative densities: reverse KL, Jensen-Shannon, or Wasserstein objectives, which favour sharp modes over the blurry, mass-covering fits of forward KL;
	- high dimension and overfitting: [[Maximum a Posteriori Learning|MAP]] / penalized likelihood ([[L2 Regularization|weight decay]], LASSO).

[^1]: Supplementary notes provided by the creator.
