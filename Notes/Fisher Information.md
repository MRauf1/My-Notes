---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Fisher Information)
> Given a [[Log-Likelihood Function]] $L(\beta)$, its Fisher Information is
> $$
> \begin{align}
> \iota(\beta) = - E[\frac{\partial^2 L(\beta)}{\partial \beta^2}]
> \end{align}
> $$

It is the negative [[Expectation]] of the [[Second Derivative]] of the [[Log-Likelihood Function]].

> [!info] Definition 2 (Fisher Information of One Observation)[^1]
> For $X$ with pdf $f(x; \theta)$ satisfying the [[Maximum Likelihood Regularity Conditions|regularity conditions]] (R0)-(R4),
> $$
> \begin{align}
> I(\theta) = E\left[\left(\frac{\partial \log f(X; \theta)}{\partial\theta}\right)^2\right] = -E\left[\frac{\partial^2 \log f(X; \theta)}{\partial\theta^2}\right] = \text{Var}\left(\frac{\partial \log f(X; \theta)}{\partial\theta}\right)
> \end{align}
> $$
> The information in a [[Random Sample]] of size $n$ is $\text{Var}\left(\frac{\partial \log L(\theta; \mathbf{X})}{\partial\theta}\right) = nI(\theta)$, since $\partial \log L/\partial\theta = \sum_i \partial \log f(X_i; \theta)/\partial\theta$ is a sum of iid terms. Definition 1 is this sample information.

**Interpretation.**[^2] $I(\theta)$ is a weighted mean, with weights $f(x; \theta)$, of the squared [[Score Function|score]] or of the negative curvature $-\partial^2 \log f/\partial\theta^2$. The more the log-density changes with $\theta$ on average, the more an observation tells about $\theta$; if $\theta$ did not appear in $\log f$ there would be zero information. The three expressions agree because the score has mean $0$ (differentiate $\int f = 1$ under the integral sign), which is where (R4) is needed.

# Properties
- [[Maximum Likelihood Estimator Variance]]
- [[Score Function Variance]]
- Bounds estimation precision: the [[Rao-Cramér Lower Bound]] $1/(nI(\theta))$ for unbiased estimators, attained asymptotically by the MLE ([[Maximum Likelihood Estimator Asymptotic Normality]]).
- For a Bernoulli $b(1, \theta)$ sample of size $n$, the information is $n/[\theta(1-\theta)]$ ([[Binomial Distribution Fisher Information]]).[^3]
- Multiparameter version: [[Fisher Information Matrix]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=379)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=380)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=381)
