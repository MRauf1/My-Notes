---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Lehmann-Scheffé Theorem[^1]
> Let $X_1, \dots, X_n$, with $n$ a fixed positive integer, be a random sample from a distribution with pdf or pmf $f(x; \theta)$, $\theta \in \Omega$. Let $Y_1 = u_1(X_1, \dots, X_n)$ be a [[Sufficient Statistic]] for $\theta$, and let the family $\{f_{Y_1}(y_1; \theta) : \theta \in \Omega\}$ be complete ([[Complete Family (Statistics)]]). If a function of $Y_1$ is an unbiased estimator of $\theta$, then this function of $Y_1$ is the unique [[Minimum Variance Unbiased Estimator|MVUE]] of $\theta$.

> [!abstract] Vector Version[^2]
> Let $\delta = g(\boldsymbol{\theta})$ be the parameter of interest, and let $\mathbf{Y}$ be a vector of jointly complete sufficient statistics for $\boldsymbol{\theta}$. If $T = T(\mathbf{Y})$ satisfies $E(T) = \delta$, then $T$ is the unique MVUE of $\delta$.

"Unique" means that any two such estimators are equal except on a set of probability zero for every $\theta \in \Omega$.

Proof idea: let $\varphi(Y_1)$ be unbiased and let $W$ be any unbiased estimator.
1. By the [[Rao-Blackwell Theorem]], $E(W | Y_1)$ is an unbiased function of $Y_1$ with variance at most $\text{Var}(W)$.
2. By completeness, $E(W | Y_1) = \varphi(Y_1)$ almost surely.
3. Hence $\text{Var}(\varphi(Y_1)) \leq \text{Var}(W)$.

Sufficiency ensures no information is lost, Rao-Blackwell ensures the best estimator is a function of $Y_1$, and completeness ensures there is only one candidate. So any unbiased function of a complete sufficient statistic is automatically optimal. In practice, one only has to find some function of $Y_1$ with the right expectation, for example by bias-correcting the MLE.

# Properties
- For the [[Regular Exponential Class]], $Y_1 = \sum K(X_i)$ is complete and sufficient by inspection. The theorem then turns the MVUE problem into solving $E[\varphi(Y_1)] = \theta$ (or $= g(\theta)$).
- The resulting MVUE need not be a good estimator. See Remark 7.6.1 in [[Minimum Variance Unbiased Estimator]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=448&annotation=SFR4T3G8)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=464&annotation=64BTQ33F)
