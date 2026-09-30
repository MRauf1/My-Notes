---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Regular Exponential Class (One Parameter)[^1][^2]
> Let $\Omega = \{\theta : \gamma < \theta < \delta\}$ with $\gamma, \delta$ known constants (possibly $\pm\infty$), and let
> $$
> \begin{align}
> f(x; \theta) = \begin{cases} \exp[p(\theta)K(x) + H(x) + q(\theta)] & x \in S \\ 0 & \text{elsewhere} \end{cases}
> \end{align}
> $$
> where $S$ is the support of $X$. This pdf or pmf is a member of the regular exponential class if:
> 1. $S$ does not depend on $\theta$;
> 2. $p(\theta)$ is a nontrivial continuous function of $\theta \in \Omega$;
> 3. (a) if $X$ is continuous, $K'(x) \not\equiv 0$, and both $K'(x)$ and $H(x)$ are continuous functions of $x \in S$ (the printed "$K'(x) \equiv 0$" is a typo for $\not\equiv$); (b) if $X$ is discrete, $K(x)$ is a nontrivial function of $x \in S$.

> [!info] Regular Exponential Class (m Parameters)[^3][^4]
> Let $\boldsymbol{\theta} \in \Omega \subset \mathbb{R}^m$, with support $S = (a, b)$ if $X$ is continuous or $S = \{a_1, a_2, \dots\}$ if discrete, and
> $$
> \begin{align}
> f(x; \boldsymbol{\theta}) = \begin{cases} \exp\left[\sum_{j=1}^m p_j(\boldsymbol{\theta})K_j(x) + H(x) + q(\boldsymbol{\theta})\right] & x \in S \\ 0 & \text{elsewhere} \end{cases}
> \end{align}
> $$
> This is a member of the exponential class. It is a regular case if, in addition:
> 1. the support does not depend on $\boldsymbol{\theta}$;
> 2. $\Omega$ contains a nonempty $m$-dimensional open rectangle;
> 3. the $p_j(\boldsymbol{\theta})$ are nontrivial, functionally independent, continuous functions of $\boldsymbol{\theta}$;
> 4. (a) if $X$ is continuous, the $K_j'(x)$ are continuous on $(a, b)$, no one is a linear homogeneous function of the others, and $H(x)$ is continuous; (b) if $X$ is discrete, the $K_j(x)$ are nontrivial functions on $S$ and no one is a linear homogeneous function of the others.

> [!info] k-Dimensional Random Vector[^5]
> For a random vector $\mathbf{X} \in \mathbb{R}^k$ with support $S \subset \mathbb{R}^k$ and $\boldsymbol{\theta} \in \Omega \subset \mathbb{R}^p$, the same form $f(\mathbf{x}; \boldsymbol{\theta}) = \exp[\sum_{j=1}^m p_j(\boldsymbol{\theta})K_j(\mathbf{x}) + H(\mathbf{x}) + q(\boldsymbol{\theta})]$ on $S$ defines the exponential class. It is regular if $p = m$, the support is free of $\boldsymbol{\theta}$, and conditions analogous to those above hold.

> [!abstract] Theorem 7.5.1 (Distribution of the Sufficient Statistic)[^6][^7]
> Let $X_1, \dots, X_n$ be a random sample from a regular case of the one-parameter exponential class, and let $Y_1 = \sum_{i=1}^n K(X_i)$. Then:
> 1. $f_{Y_1}(y_1; \theta) = R(y_1)\exp[p(\theta)y_1 + nq(\theta)]$ for $y_1 \in S_{Y_1}$, where neither $S_{Y_1}$ nor $R(y_1)$ depends on $\theta$;
> 2. $E(Y_1) = -n\dfrac{q'(\theta)}{p'(\theta)}$;
> 3. $\text{Var}(Y_1) = n\dfrac{1}{p'(\theta)^3}\{p''(\theta)q'(\theta) - q''(\theta)p'(\theta)\}$.

> [!abstract] Theorem 7.5.2 (Complete Sufficient Statistic)[^7]
> If $X_1, \dots, X_n$ ($n$ fixed) is a random sample from a regular case of the exponential class, then $Y_1 = \sum_{i=1}^n K(X_i)$ is a [[Sufficient Statistic]] for $\theta$, and $\{f_{Y_1}(y_1; \theta) : \gamma < \theta < \delta\}$ is complete. That is, $Y_1$ is a complete sufficient statistic.

**Multiparameter case.**[^4] The joint pdf of the sample is
$$
\begin{align}
\prod_{i=1}^n f(x_i; \boldsymbol{\theta}) = \exp\left[\sum_{j=1}^m p_j(\boldsymbol{\theta})\sum_{i=1}^n K_j(x_i) + nq(\boldsymbol{\theta})\right]\exp\left[\sum_{i=1}^n H(x_i)\right]
\end{align}
$$
- By the [[Neyman Factorization Theorem]], $Y_j = \sum_{i=1}^n K_j(X_i)$, $j = 1, \dots, m$, are jointly sufficient.
- The joint pdf of $\mathbf{Y}$ is $R(\mathbf{y})\exp[\sum_j p_j(\boldsymbol{\theta})y_j + nq(\boldsymbol{\theta})]$, where $R$ and the support do not depend on $\boldsymbol{\theta}$.
- The family is complete when $n > m$, so $Y_1, \dots, Y_m$ are joint complete sufficient statistics.
- The same holds for the $k$-dimensional case.[^5] If $T = h(\mathbf{Y})$ has $E(T) = \delta = g(\boldsymbol{\theta})$, then $T$ is the unique MVUE of $\delta$ ([[Lehmann-Scheffé Theorem]]).

This is Hogg's parametrization of the [[Exponential Family]]: $\eta = p(\theta)$ is the natural parameter, $T(x) = K(x)$ is the sufficient statistic, $h(x) = e^{H(x)}$, and $A(\theta) = -q(\theta)$. "Regular" rules out supports that move with $\theta$ (such as the uniform on $(0, \theta)$) and degenerate parametrizations. Those are exactly the conditions under which the MLE regularity conditions hold ([[Maximum Likelihood Regularity Conditions]]), and under which the statistic $\sum K(X_i)$ captures everything about $\theta$.

# Properties
- Theorem 7.5.1 follows because the distribution of $Y_1$ is itself a one-parameter exponential family. Differentiating $\int f_{Y_1} = 1$ with respect to $\theta$ gives $E[p'(\theta)Y_1 + nq'(\theta)] = 0$. Differentiating again gives the variance.
- Sufficient statistics of fixed dimension $m$, whatever the sample size $n$, essentially characterize exponential families among families with fixed support (Pitman-Koopman-Darmois).
- The [[Maximum Likelihood Estimation|MLE]] solves $E_\theta[Y_1] = y_1$, i.e. it matches the expected and observed sufficient statistics.
- Members include the [[Normal Distribution]], [[Poisson Distribution]], [[Binomial Distribution]] (fixed $n$), [[Gamma Distribution]], [[Beta Distribution]], and [[Multinomial Distribution]]. A complete sufficient statistic in this class is independent of every [[Ancillary Statistic]] ([[Basu's Theorem]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=451&annotation=UX5WVPEV)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=452&annotation=ZB6FF5HA)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=464&annotation=6DF3BYHI)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=465&annotation=2UBUL3UI)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=466&annotation=XQ9AUP4U)
[^6]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=452&annotation=2E9MMC3Y)
[^7]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=453&annotation=87CTBGIN)
