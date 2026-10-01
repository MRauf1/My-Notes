---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Maximum Likelihood Loss Function Recipe[^1]
> Rather than predicting $\mathbf{y}$ directly, treat the model $\mathbf{f}[\mathbf{x}, \boldsymbol{\phi}]$ as computing a conditional distribution $Pr(\mathbf{y} | \mathbf{x})$. For training data $\{\mathbf{x}_i, \mathbf{y}_i\}_{i=1}^I$:
> 1. Choose a parametric distribution $Pr(\mathbf{y} | \boldsymbol{\theta})$ defined over the domain of the predictions $\mathbf{y}$ ([[Output Distributions for Loss Functions]]).
> 2. Set the model to predict one or more of its parameters, $\boldsymbol{\theta} = \mathbf{f}[\mathbf{x}, \boldsymbol{\phi}]$, so $Pr(\mathbf{y} | \boldsymbol{\theta}) = Pr(\mathbf{y} | \mathbf{f}[\mathbf{x}, \boldsymbol{\phi}])$.
> 3. Train by minimizing the **negative log-likelihood**:
> $$
> \begin{align}
> \hat{\boldsymbol{\phi}} = \underset{\boldsymbol{\phi}}{\arg\min}\left[L[\boldsymbol{\phi}]\right] = \underset{\boldsymbol{\phi}}{\arg\min}\left[-\sum_{i=1}^I \log\left[Pr(\mathbf{y}_i | \mathbf{f}[\mathbf{x}_i, \boldsymbol{\phi}])\right]\right]
> \end{align}
> $$
> 4. For [[Inference (Machine Learning)|inference]] on a new $\mathbf{x}$, return the full distribution $Pr(\mathbf{y} | \mathbf{f}[\mathbf{x}, \hat{\boldsymbol{\phi}}])$ or the point estimate at its maximum,
> $$
> \begin{align}
> \hat{\mathbf{y}} = \underset{\mathbf{y}}{\arg\max}\left[Pr(\mathbf{y} | \mathbf{f}[\mathbf{x}, \hat{\boldsymbol{\phi}}])\right]
> \end{align}
> $$

# Properties
- The loss encourages each training output $\mathbf{y}_i$ to have high probability under the distribution computed from $\mathbf{x}_i$; it is [[Maximum Likelihood Learning]] expressed as a [[Loss Function]].
- The point estimate usually has a closed form in terms of $\boldsymbol{\theta}$, e.g. the mean $\mu$ for a univariate [[Normal Distribution]].
- Gives the squared error for a normal distribution ([[Probabilistic Formulation of Regression]]), the [[Binary Cross-Entropy Loss]] for a [[Bernoulli Distribution]], and the multiclass [[Cross-Entropy Loss]] for a categorical distribution via the [[Softmax Function]].
- Equivalent to minimizing the [[Cross-Entropy Loss|cross-entropy]], i.e. the [[Kullback-Leibler Divergence]] between the empirical data distribution and the model.
- When the predicted variance also depends on the input, the model is [[Heteroscedasticity (Machine Learning)|heteroscedastic]].
- Multiple outputs are usually handled by assuming independence ([[Loss Function for Multiple Outputs]]).
- Its optimality holds only under correct specification and large samples ([[Maximum Likelihood Loss Optimality and Failure Modes]]).

[^1]: [Prince, Ch. 5](zotero://select/library/items/T3V9WVXD)
