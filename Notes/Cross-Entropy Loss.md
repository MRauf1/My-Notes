---
tags:
  - computer_science
  - deep_learning
---

# Definition

> [!info] Definition 1 (Cross-Entropy Loss)
> $$
> \begin{align}
> L(\hat{y}, y) = - \sum_{K}^{k=1} y_k log(\hat{y}_k)
> \end{align}
> $$
> where $\hat{y}_k$ is the [[Probability Mass Function|pmf]] $\mathbf{p}$ representing the [[Probability|probability]] that the input is of class $k$.[^1] $\mathbf{p}$ is a [[Point|point]] on the $(K - 1)$-[[Simplex|simplex]] denoted by $\mathbf{p} \in \triangle^{(K - 1)}$.

Cross-entropy is the negative of the sum of the elementwise agreements between the ground truth and the prediction.

Minimizing the cross-entropy maximizes the log likelihood of the ground truth observation $\mathbf{y}$ under the model's prediction $\hat{\mathbf{y}}$.

# Properties
- **Derivation from KL divergence**: describe the empirical data as point masses $q(y) = \frac{1}{I}\sum_{i=1}^I \delta[y - y_i]$ and minimize the [[Kullback-Leibler Divergence]] to the model $Pr(y | \boldsymbol{\theta})$. The entropy term $\int q \log q$ is independent of $\boldsymbol{\theta}$, leaving the cross-entropy $-\int q(y)\log[Pr(y | \boldsymbol{\theta})]dy$. Substituting $q$ and dropping the factor $\frac{1}{I}$ gives $\hat{\boldsymbol{\theta}} = \arg\min_{\boldsymbol{\theta}} \left[-\sum_{i=1}^I \log[Pr(y_i | \boldsymbol{\theta})]\right]$; with $\boldsymbol{\theta} = \mathbf{f}[\mathbf{x}_i, \boldsymbol{\phi}]$, this is exactly the negative log-likelihood of the [[Maximum Likelihood Loss Function Recipe]]. Hence the cross-entropy and negative log-likelihood criteria are equivalent.[^2]
- The cross-entropy can be interpreted as the uncertainty remaining in one distribution after taking into account what is known from the other.
- In the multiclass case, the network outputs pass through a [[Softmax Function|softmax]] to give the categorical probabilities; the two-class case is the [[Binary Cross-Entropy Loss]]. For class imbalance, see [[Focal Loss]].

[^1]: https://visionbook.mit.edu/intro_to_learning.html
[^2]: [Prince, Ch. 5](zotero://select/library/items/T3V9WVXD)
