---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

[[Statistical Hypothesis Test|Hypothesis Test]] for [[Maximum Likelihood Estimation]].

It is the most accurate of hypothesis tests for MLE, but is costly, and as thus, is preferred only for small $n$.

In Hogg et al.'s form (Rao's score test),[^1] $\chi^2_R = \left(\frac{l'(\theta_0)}{\sqrt{nI(\theta_0)}}\right)^2$, built from the [[Score Function|scores]] $\partial \log f(X_i; \theta_0)/\partial\theta$; under $H_0$, $\chi^2_R = \chi^2_W + R_{0n}$ with $R_{0n} \xrightarrow{P} 0$, so reject if $\chi^2_R \geq \chi^2_\alpha(1)$ for an asymptotic level-$\alpha$ test. It is named after C. R. Rao.

Two refinements of the claims above: computationally the score test is usually the cheapest of the three, since it needs the model fitted only under $H_0$ (no unrestricted MLE); and asymptotically the three tests are equivalent with the same efficiency, while finite-sample studies have not found any of them uniformly best.[^2]

# Properties
## Basic Hypothesis Test Properties
- [[Score Test Statistic]]
- [[Score Test Confidence Interval]]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=396)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=399)
