---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Relation between [[Chi-Squared Distribution]] and [[Normal Distribution]])[^1]
> Let $Z \sim N(0, 1)$ and $Z_1, \dots, Z_v \sim N(0, 1)$. Then
> $$
> \begin{align}
> Z^2 &= \chi^2(1) \\
> Z_1^2 + \dots + Z_v^2 &= \chi^2(v)
> \end{align}
> $$

In particular,[^2] if $X \sim N(\mu, \sigma^2)$ with $\sigma^2 > 0$, then $V = (X - \mu)^2/\sigma^2 \sim \chi^2(1)$. The multivariate version is the quadratic form $(\mathbf{X} - \boldsymbol{\mu})^T\Sigma^{-1}(\mathbf{X} - \boldsymbol{\mu}) \sim \chi^2(n)$ of a [[Multivariate Normal Distribution]].

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=26)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=208)
