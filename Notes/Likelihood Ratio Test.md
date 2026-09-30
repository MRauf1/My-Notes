---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

[[Statistical Hypothesis Test|Hypothesis Test]] for [[Maximum Likelihood Estimation]].

It is a middle-ground between [[Wald Test]] and [[Score Test]] in terms of both efficiency and effectiveness. It is preferred when $n$ is relatively small.

> [!info] Definition 1 (Likelihood Ratio Test)[^1][^2]
> For $H_0: \boldsymbol{\theta} \in \omega$ versus $H_1: \boldsymbol{\theta} \in \Omega \cap \omega^c$, where $\omega$ is defined by $q$ independent continuously differentiable constraints $g_1(\boldsymbol{\theta}) = a_1, \dots, g_q(\boldsymbol{\theta}) = a_q$ (so $\omega$ has dimension $p - q$), the likelihood ratio is
> $$
> \begin{align}
> \Lambda = \frac{\max_{\boldsymbol{\theta} \in \omega} L(\boldsymbol{\theta})}{\max_{\boldsymbol{\theta} \in \Omega} L(\boldsymbol{\theta})} = \frac{L(\hat{\omega})}{L(\hat{\Omega})}
> \end{align}
> $$
> with $L(\hat{\Omega}) = L(\hat{\boldsymbol{\theta}})$ the unrestricted maximum and $L(\hat{\omega}) = L(\hat{\boldsymbol{\theta}}_0)$ the maximum under $H_0$. The test rejects $H_0$ if $\Lambda \leq c$, with $c$ chosen so that $\alpha = \max_{\boldsymbol{\theta} \in \omega} P_{\boldsymbol{\theta}}[\Lambda \leq c]$. For a simple null $H_0: \theta = \theta_0$, $\Lambda = L(\theta_0)/L(\hat{\theta})$.

$\Lambda \leq 1$; by the [[Likelihood Maximization at True Parameter Theorem]], $\Lambda$ should be close to $1$ when $H_0$ holds and small when $H_1$ holds.

> [!abstract] Theorem 1 (Wilks)[^3][^4]
> Under the regularity conditions of [[Maximum Likelihood Estimator Asymptotic Normality]], and $H_0$, $-2\log\Lambda \xrightarrow{D} \chi^2(q)$; for $H_0: \theta = \theta_0$ with a scalar parameter, $-2\log\Lambda \xrightarrow{D} \chi^2(1)$. So "reject if $\chi^2_L = -2\log\Lambda \geq \chi^2_\alpha(q)$" has asymptotic level $\alpha$, usable when the exact distribution of $\Lambda$ is unavailable.

# Properties
- The degrees of freedom $q$ equal the number of constraints, i.e. the drop in dimension from $\Omega$ to $\omega$.
- The likelihood ratio, [[Wald Test|Wald]], and [[Score Test|score]] tests are asymptotically equivalent under $H_0$ and have the same asymptotic efficiency, and finite-sample comparisons have not shown any of them to be best overall.[^5]
## Basic Hypothesis Test Properties
- [[Likelihood Ratio Test Statistic]]
- [[Likelihood Ratio Test Confidence Interval]]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=393)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=412)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=395)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=414)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=399)
