---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Probabilistic Formulation of Regression[^1]
> Instead of treating a fitted function $y(\mathbf{x}, \mathbf{w})$ as producing a single number, treat each prediction as a **distribution** over the target: given $\mathbf{x}$, the target $t$ is Gaussian with mean equal to the model's output and precision (inverse variance) $\beta$,
> $$
> \begin{align}
> p(t | \mathbf{x}, \mathbf{w}, \beta) = \mathcal{N}\big(t \,|\, y(\mathbf{x}, \mathbf{w}), \beta^{-1}\big)
> \end{align}
> $$
> For i.i.d. training data $\{(\mathbf{x}_n, t_n)\}_{n=1}^N$ the [[Log-Likelihood Function|log likelihood]] is
> $$
> \begin{align}
> \ln p(\mathbf{t} | \mathbf{X}, \mathbf{w}, \beta) = -\frac{\beta}{2}\sum_{n=1}^N \{y(\mathbf{x}_n, \mathbf{w}) - t_n\}^2 + \frac{N}{2}\ln\beta - \frac{N}{2}\ln(2\pi)
> \end{align}
> $$

The model's output is thus reinterpreted as the **mean** of a predicted Gaussian, and the spread $\beta^{-1}$ quantifies how far the observed targets are expected to scatter around that mean.

**Curve fitting as maximum likelihood.** Only the first term depends on $\mathbf{w}$, so [[Maximum Likelihood Estimation|maximizing the likelihood]] over $\mathbf{w}$ is exactly minimizing the sum-of-squares error $\frac{1}{2}\sum_n \{y(\mathbf{x}_n, \mathbf{w}) - t_n\}^2$. Least squares is therefore the special case of maximum likelihood under a Gaussian noise assumption. The precision then decouples and is fitted afterwards as the mean squared residual:
$$
\begin{align}
\frac{1}{\beta_{\mathrm{ML}}} = \frac{1}{N}\sum_{n=1}^N \{y(\mathbf{x}_n, \mathbf{w}_{\mathrm{ML}}) - t_n\}^2
\end{align}
$$
Substituting both gives the plug-in [[Predictive Distribution|predictive distribution]] $p(t | \mathbf{x}, \mathbf{w}_{\mathrm{ML}}, \beta_{\mathrm{ML}}) = \mathcal{N}(t \,|\, y(\mathbf{x}, \mathbf{w}_{\mathrm{ML}}), \beta_{\mathrm{ML}}^{-1})$, a distribution over $t$ rather than a point estimate.[^2]

**Curve fitting with a prior as MAP.** With a Gaussian prior $p(\mathbf{w} | \alpha) = \mathcal{N}(\mathbf{w} | \mathbf{0}, \alpha^{-1}\mathbf{I})$, [[Maximum a Posteriori Learning|MAP]] minimizes
$$
\begin{align}
\frac{\beta}{2}\sum_{n=1}^N \{y(\mathbf{x}_n, \mathbf{w}) - t_n\}^2 + \frac{\alpha}{2}\mathbf{w}^T\mathbf{w}
\end{align}
$$
which is [[L2 Regularization|ridge regression]] with $\lambda = \alpha/\beta$.

**The general recipe.** Any fitting algorithm that minimizes a loss can be read as maximum likelihood under some noise model, since the negative log likelihood plays the role of the error function:
- Gaussian noise $\Rightarrow$ squared error ([[L2 Loss]]); the optimal point prediction is the conditional mean ([[Regression Function]]).
- Laplace noise $\Rightarrow$ absolute error; the optimal point prediction is the conditional [[Median]] ([[Minkowski Loss]] with $q = 1$).
- Bernoulli / categorical targets $\Rightarrow$ [[Cross-Entropy Loss|cross-entropy]], e.g. [[Binary Logistic Regression|logistic regression]].
- Letting the model output both a mean $\mu(\mathbf{x})$ and a variance $\sigma^2(\mathbf{x})$ ([[Heteroscedasticity (Machine Learning)|heteroscedastic]] regression) gives the loss $\sum_n \left[\frac{(t_n - \mu(\mathbf{x}_n))^2}{2\sigma^2(\mathbf{x}_n)} + \frac{1}{2}\ln\sigma^2(\mathbf{x}_n)\right]$, which learns input-dependent noise.

# Properties
- Makes the choice of loss an explicit modelling assumption about the noise, rather than an arbitrary choice, and allows [[Model Selection]] tools based on the likelihood (e.g. [[Akaike Information Criterion]]).
- The plug-in predictive variance $\beta_{\mathrm{ML}}^{-1}$ accounts only for noise on the targets; a fully Bayesian [[Predictive Distribution]] also accounts for uncertainty in $\mathbf{w}$.
- Inherits the weaknesses of maximum likelihood: the fitted $\mathbf{w}_{\mathrm{ML}}$ [[Overfitting|over-fits]] with flexible models, and $\beta_{\mathrm{ML}}^{-1}$ is biased low ([[Normal Distribution Maximum Likelihood Estimation]]), since residuals are measured against a curve fitted to the same data.
- Minimizing the negative log likelihood equals minimizing the [[Kullback-Leibler Divergence]] from the empirical data distribution to the model.

[^1]: [Bishop, 2006, p. 28](zotero://open-pdf/library/items/5G99AZ8U?page=48&annotation=MD6GM4G8)
[^2]: [Bishop, 2006, p. 30](zotero://open-pdf/library/items/5G99AZ8U?page=50&annotation=ZHNE3X3Z)
