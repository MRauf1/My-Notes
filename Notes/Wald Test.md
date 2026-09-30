---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

[[Statistical Hypothesis Test|Hypothesis Test]] on [[Maximum Likelihood Estimation]] where the [[Statistical Hypothesis Test|Null Hypothesis]] is $H_0: \beta = \beta_0$, which uses the [[Wald Test Statistic]].

It is a simple and relatively effective hypothesis test that works well when $n$ is large, but it performs poorly when $n$ is small. It is less accurate than [[Likelihood Ratio Test]] and [[Score Test]].

One downside is that the Wald test can be degenerate in that it produces a single value as its confidence interval rather than an actual interval.

In Hogg et al.'s form,[^1] $\chi^2_W = \left\{\sqrt{nI(\hat{\theta})}(\hat{\theta} - \theta_0)\right\}^2$, which is asymptotically $\chi^2(1)$ under $H_0$ because $I(\hat{\theta}) \xrightarrow{P} I(\theta_0)$ ([[Maximum Likelihood Estimator Asymptotic Normality]]); reject if $\chi^2_W \geq \chi^2_\alpha(1)$. Under $H_0$, $\chi^2_W - \chi^2_L \xrightarrow{P} 0$, so it is asymptotically equivalent to the [[Likelihood Ratio Test]]. It is named after Abraham Wald.

# Properties
## Basic Hypothesis Properties
- [[Wald Test Statistic]]
- [[Wald Test Confidence Interval]]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=396)
