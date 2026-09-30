---
tags:
  - statistics
  - statistical_learning
---

# Definition

> [!info] Definition 1 (Mean Squared Error)[^1]
> For labels $y_i$ and predictions $\hat{f}(x_i)$, the mean squared error is
> $$
> \begin{align}
> MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{f}(x_i))^2
> \end{align}
> $$

> [!info] Definition 2 (MSE of an Estimator)
> For an [[Estimator]] $\hat{\theta}$ of a fixed parameter $\theta$,
> $$
> \begin{align}
> \text{MSE}_\theta(\hat{\theta}) = E_\theta[(\hat{\theta} - \theta)^2] = \text{Var}_\theta(\hat{\theta}) + [E_\theta(\hat{\theta}) - \theta]^2
> \end{align}
> $$
> This is the [[Risk Function (Statistics)|risk]] under squared-error loss ([[Bias-Variance-MSE Decomposition of an Estimator]]).

# Properties
- Minimum-MSE criterion: rather than requiring unbiasedness and minimizing variance ([[Minimum Variance Unbiased Estimator]]), choose the estimator with the smallest bias$^2$ + variance. This allows a small bias in exchange for a large drop in variance ([[Bias-Variance Tradeoff]]).
- Minimizing variance alone, with no bias constraint, is degenerate: a constant estimator has variance $0$. Biased estimators obey the biased [[Rao-Cramér Lower Bound]] $\text{Var}(\hat{\theta}) \geq (1 + b'(\theta))^2/(nI(\theta))$.
- Biased estimators with lower MSE than the unbiased one:
  - $\frac{1}{n+1}\sum_i (X_i - \bar{X})^2$ for normal $\sigma^2$, which minimizes MSE among multiples of $\sum_i (X_i - \bar{X})^2$ and beats both $S^2$ (divisor $n - 1$) and the MLE (divisor $n$);
  - ridge regression versus OLS ([[L2 Regularization]]);
  - the [[James-Stein Estimator]].
- A uniformly minimum-MSE estimator over all estimators does not exist. MSE functions of different estimators cross, which is why minimax or Bayes criteria are needed ([[Minimax Decision Rule]], [[Bayes Estimator]]).

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=38)