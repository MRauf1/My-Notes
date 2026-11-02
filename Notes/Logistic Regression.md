---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Logistic Regression)[^1]
> A [[Generalized Linear Model]] for a categorical response that models the response-category probabilities through the [[Logit Function|logit]] [[Link Function|link]]. For a binary response $Y$ with $\pi(x) = P(Y = 1 \mid x)$,
> $$
> \begin{align}
> \operatorname{logit}\pi(x) = \log\frac{\pi(x)}{1 - \pi(x)} = x\beta \iff \pi(x) = \frac{1}{1 + e^{-x\beta}}
> \end{align}
> $$
> so $\pi(x)$ is the [[Standard Logistic Function]] of the linear predictor.

Makes use of the [[Standard Logistic Function]].

# Types
- [[Binary Logistic Regression]]
- [[Binomial Regression]]
- [[Multinomial Logistic Regression]]
- [[Ordinal Logistic Regression]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L)
