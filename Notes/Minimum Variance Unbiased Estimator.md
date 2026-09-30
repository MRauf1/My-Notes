---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Minimum Variance Unbiased Estimator (MVUE)[^1]
> For a given positive integer $n$, $Y = u(X_1, \dots, X_n)$ is a minimum variance unbiased estimator of $\theta$ if $Y$ is [[Unbiased Estimator|unbiased]], $E(Y) = \theta$, and
> $$
> \begin{align}
> \text{Var}(Y) \leq \text{Var}(Y') \quad \text{for every other unbiased estimator } Y' \text{ of } \theta
> \end{align}
> $$
> The MVUE is also called the uniformly minimum variance unbiased estimator (UMVUE), since the inequality must hold for every $\theta \in \Omega$.

Within the class of unbiased estimators, [[Mean Squared Error|MSE]] equals variance, so the MVUE is the minimum-risk estimator under squared-error loss when the search is restricted to unbiased rules ([[Risk Function (Statistics)]]). That restriction is what makes a uniformly best estimator possible: without it, no estimator minimizes the risk at every $\theta$.

**How it is found.** The standard route is:
1. Find a [[Sufficient Statistic]] $Y_1$, for example with the [[Neyman Factorization Theorem]], so that no information about $\theta$ is discarded.
2. Restrict the search to functions of $Y_1$. The [[Rao-Blackwell Theorem]] justifies this, since conditioning any unbiased estimator on $Y_1$ never increases its variance.
3. If $Y_1$ is also complete ([[Complete Family (Statistics)]]), the unbiased function of $Y_1$ is unique, and by the [[Lehmann-Scheffé Theorem]] it is the MVUE. For the [[Regular Exponential Class]], $Y_1 = \sum K(X_i)$ is complete and sufficient by inspection.

For a vector parameter, the target is usually a function $\delta = g(\boldsymbol{\theta})$. If $\mathbf{Y}$ is jointly complete and sufficient and $T = T(\mathbf{Y})$ has $E(T) = \delta$, then $T$ is the unique MVUE of $\delta$.[^2]

**A frequentist concept.** The MVUE treats $\theta$ as a fixed, non-random constant. Bias and variance are computed over the sampling distribution of repeated hypothetical samples, $E_\theta$ and $\text{Var}_\theta$ ([[Probability Frequentist Framework]]).
- In Bayesian statistics, $\theta$ is a random variable with a prior. The optimality criterion is to minimize the posterior expected loss given the observed data, with no unbiasedness constraint ([[Bayes Estimator]]).
- Non-degenerate Bayes estimators are almost always biased in the frequentist sense, because they shrink toward the prior.
- Bayes estimators can still be judged by frequentist criteria such as risk and admissibility. Under squared-error loss, proper-prior Bayes estimators are admissible, and many are minimax ([[Minimax Decision Rule]]).

**Comparison of estimator properties.**

| Property | Definition | What it guarantees | Limitation |
| --- | --- | --- | --- |
| Unbiased ([[Unbiased Estimator]]) | $E_\theta(\hat{\theta}) = \theta$ for all $\theta$ | No systematic over- or under-estimation at any fixed $n$ | Variance can be huge, so individual estimates can be unreliable. Unbiasedness is not preserved by nonlinear functions |
| Consistent ([[Consistent Estimator]]) | $\hat{\theta}_n \xrightarrow{P} \theta$ | Enough data gives an estimate arbitrarily close to $\theta$ with high probability | Says nothing about small samples; can be badly biased at fixed $n$ |
| Sufficient ([[Sufficient Statistic]]) | Conditional distribution of the sample given $Y_1$ is free of $\theta$ | $Y_1$ keeps all the information about $\theta$ in the sample, so the raw data can be discarded | A property of a data reduction, not of accuracy. A sufficient statistic need not estimate $\theta$ well, or be on the scale of $\theta$ at all |
| MVUE | Unbiased with the smallest variance among unbiased estimators, for every $\theta$ | Best finite-sample precision among unbiased estimators | May not exist or may be hard to find. Can be a poor estimator (see below), and a biased estimator can have smaller MSE |

These properties are used as building blocks rather than rivals. Sufficiency reduces the data without loss, unbiasedness removes systematic error, and minimizing variance within that class gives the MVUE. The MVUE is a function of a sufficient statistic, and in regular models it is usually also consistent.

# Properties
- Relation to efficiency: an [[Efficient Estimator]], one attaining the [[Rao-Cramér Lower Bound]], is the MVUE. The converse fails, since the MVUE may have variance strictly above the bound when no efficient estimator exists.
- Uniqueness: if an MVUE exists it is unique with probability one. Two MVUEs $T_1, T_2$ would make $(T_1 + T_2)/2$ unbiased with variance no larger, which forces $T_1 = T_2$ almost surely.
- A principle, not a theorem (Remark 7.6.1):[^3] the MVUE can be a poor estimator. For $X \sim$ [[Poisson Distribution|Poisson]]$(\theta)$ with $n = 1$, $X$ is complete and sufficient, and $E[(-1)^X] = e^{-2\theta}$. So $(-1)^X$ is the MVUE of $e^{-2\theta} \in (0, 1)$, yet it only takes the values $\pm 1$. The [[Maximum Likelihood Estimation|MLE]] $e^{-2X}$, though biased, is a much better estimator in practice.
- Unbiasedness can be too restrictive. Minimizing [[Mean Squared Error]] $= \text{bias}^2 + \text{variance}$ instead can favor biased estimators ([[Bias-Variance Tradeoff]]).
  - Unconstrained minimum variance is meaningless: a constant estimator has variance $0$ but ignores the data.
  - Biased estimators instead obey the biased form of the [[Rao-Cramér Lower Bound]], $\text{Var}(\hat{\theta}) \geq (1 + b'(\theta))^2/(nI(\theta))$.
  - Examples that beat the MVUE in MSE: $\frac{1}{n+1}\sum(X_i - \bar{X})^2$ for normal $\sigma^2$, ridge regression ([[L2 Regularization]]) versus OLS, and the [[James-Stein Estimator]] for $p \geq 3$ normal means.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=429&annotation=N5SA2ALC)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=464&annotation=64BTQ33F)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=459&annotation=9353UG6H)
