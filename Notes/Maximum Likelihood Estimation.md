---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

A technique for [[Parameter Estimation]]. The maximum likelihood estimate is the parameter value that maximizes the [[Likelihood Function]], denoted as $\hat{\beta}$ (parameter value under which the observed data has the highest probability of occurring).

Instead of maximizing the likelihood function directly, we instead maximize the [[Log-Likelihood Function]], which converts products into sums, which are easier to deal with.[^1]

> [!info] Definition 1 (Maximum Likelihood Estimator)[^2]
> For the [[Likelihood Function]] $L(\theta)$ of a [[Random Sample]], if the maximizer is unique, the maximum likelihood estimator is
> $$
> \begin{align}
> \hat{\theta} = \operatorname{Argmax}_{\theta \in \Omega} L(\theta)
> \end{align}
> $$
> Since $\log$ is strictly increasing, $\hat{\theta}$ also maximizes $l(\theta) = \log L(\theta)$, and for differentiable models it frequently solves the estimating equations (EE) $\partial l(\theta)/\partial\theta = 0$, a system of equations when $\theta$ is a vector.

It uses the value of $\theta$ under which the observed data are most probable as a measure of the center of $L(\theta)$. It is justified asymptotically by the [[Likelihood Maximization at True Parameter Theorem]]: with probability tending to one, the likelihood is maximized at the true parameter.[^3] There is no guarantee that the MLE exists or, if it does, that it is unique.[^4]

Steps:
1) Calculate the [[Log-Likelihood Function]] ($L(\beta) = log(l(\beta))$).
2) Calculate the [[Score Function]] and set it equal to $0$ ($u(\beta) = \frac{\partial L(\beta)}{\partial \beta} = 0$). If solving for multiple parameters, the [[Partial Derivative]] will turn into the [[Gradient Vector]].
4) Solve for $\beta$. Once solved, it is now denoted as $\hat{\beta}$.

# Properties
- [[Maximum Likelihood Estimation Properties]]
- [[Maximum Likelihood Estimator Invariance]]
- [[Maximum Likelihood Estimator Asymptotic Normality]], under the [[Maximum Likelihood Regularity Conditions]]
- Computed with missing or latent data by the [[Expectation-Maximization Algorithm]]
- A frequentist estimator: maximizing $p(\mathcal{D} | \mathbf{w})$ chooses the $\mathbf{w}$ under which the observed data is most probable. Maximizing the probability of the data given the parameters, rather than of the parameters given the data, is related to the latter through [[Bayes' Theorem]] ([[Maximum Likelihood vs Maximum a Posteriori Estimation]]).[^2][^3]
- The log is used not only for convenience but for numerical stability: a product of many small probabilities underflows floating-point precision, while the sum of log probabilities does not.[^4]
- Equivalent to minimizing the [[Kullback-Leibler Divergence]] from the data distribution to the model.
- Systematically biased for some quantities (e.g. Gaussian variance, [[Normal Distribution Maximum Likelihood Estimation]]), and this bias lies at the root of [[Overfitting|over-fitting]] in complex models; it also gives extreme estimates from small samples.

## Basic Statistical Properties
- [[Maximum Likelihood Estimator Variance]]
- [[Maximum Likelihood Estimator Standard Error]]

## Hypothesis Testing
These three have certain asymptotic equivalences.

- [[Wald Test]]
- [[Likelihood Ratio Test]]
- [[Score Test]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=27)
[^2]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=4KU9QTLZ)
[^3]: [Bishop, 2006, p. 26](zotero://open-pdf/library/items/5G99AZ8U?page=46&annotation=7JADG3MS)
[^4]: [Bishop, 2006, p. 26](zotero://open-pdf/library/items/5G99AZ8U?page=46&annotation=8E3NKN4J)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=243)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=372)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=373)
