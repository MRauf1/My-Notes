---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Output Distributions for Loss Functions[^1]
> The distribution in step 1 of the [[Maximum Likelihood Loss Function Recipe]] is chosen to match the domain of the prediction:
>
> | Data type | Domain | Distribution | Use |
> | --- | --- | --- | --- |
> | univariate, continuous, unbounded | $y \in \mathbb{R}$ | univariate [[Normal Distribution\|normal]] | [[Regression]] |
> | univariate, continuous, unbounded | $y \in \mathbb{R}$ | [[Laplace Distribution\|Laplace]] or [[t-Distribution\|t-distribution]] | robust regression |
> | univariate, continuous, unbounded | $y \in \mathbb{R}$ | [[Mixture Distribution\|mixture of Gaussians]] | multimodal regression |
> | univariate, continuous, bounded below | $y \in \mathbb{R}^+$ | [[Exponential Distribution\|exponential]] or [[Gamma Distribution\|gamma]] | predicting magnitude |
> | univariate, continuous, bounded | $y \in [0, 1]$ | [[Beta Distribution\|beta]] | predicting proportions |
> | multivariate, continuous, unbounded | $\mathbf{y} \in \mathbb{R}^K$ | [[Multivariate Normal Distribution\|multivariate normal]] | [[Multivariate Regression]] |
> | univariate, continuous, circular | $y \in (-\pi, \pi]$ | von Mises | predicting direction |
> | univariate, discrete, binary | $y \in \{0, 1\}$ | [[Bernoulli Distribution\|Bernoulli]] | [[Binary Classification]] |
> | univariate, discrete, bounded | $y \in \{1, 2, \dots, K\}$ | categorical | [[Multiclass Classification]] |
> | univariate, discrete, bounded below | $y \in \{0, 1, 2, \dots\}$ | [[Poisson Distribution\|Poisson]] | predicting event counts |
> | multivariate, discrete, permutation | $\mathbf{y} \in \mathrm{Perm}[1, 2, \dots, K]$ | Plackett-Luce | ranking |

![[Distributions for Loss Functions.png]]

# Properties
- The network output is passed through a function mapping it to the valid range of the distribution's parameters, e.g. the logistic [[Sigmoid Function|sigmoid]] for the Bernoulli parameter ([[Binary Cross-Entropy Loss]]) or the [[Softmax Function|softmax]] for the categorical probabilities ([[Cross-Entropy Loss]]).
- Heavy-tailed choices (Laplace, t) reduce sensitivity to outliers, one of the [[Maximum Likelihood Loss Optimality and Failure Modes|failure modes]] of the normal likelihood.

[^1]: [Prince, Ch. 5, Fig. 5.11](zotero://select/library/items/T3V9WVXD)
