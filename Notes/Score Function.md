---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Score [[Function]])
> Given a [[Log-Likelihood Function]] $L(\beta)$, the score function is
> $$
> \begin{align}
> u(\beta) = \frac{\partial L(\beta)}{\partial \beta}
> \end{align}
> $$

> [!info] Definition 2 (Score of One Observation)[^1]
> The score function is $\frac{\partial \log f(x; \theta)}{\partial\theta}$. The MLE solves the estimating equation $\sum_{i=1}^n \frac{\partial \log f(x_i; \theta)}{\partial\theta} = 0$, and the scores of a sample form the vector $S(\theta) = \left(\frac{\partial \log f(X_1; \theta)}{\partial\theta}, \dots, \frac{\partial \log f(X_n; \theta)}{\partial\theta}\right)^T$.[^2]

It measures how sensitive the log-density is to $\theta$ at the observed data; its variance is the [[Fisher Information]].

# Properties
- The MLE error is asymptotically $I(\theta_0)^{-1}$ times the average score ([[Maximum Likelihood Estimator Asymptotic Normality]]).
## Basic Statistical Properties
- [[Score Function Expectation]]
- [[Score Function Variance]]
- [[Score Function Normal Approximation]]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=380)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=396)
