---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (L2 Regularization)[^1]
> [[Lp Regularization]] with $p=2$: a regularizer $R(\theta) = \lVert\theta\rVert_2^2$ penalizing the squared Euclidean norm of the parameters. Also known as **Tikhonov regression** or **ridge regression**, and, in the context of neural networks, as **weight decay**.

# Properties
- Encourages most parameters to be small (near zero) rather than exactly zero, unlike [[L1 Regularization]].
- Corresponds, under the probabilistic interpretation of regularizers as priors, to a Gaussian prior on $\theta$: with prior precision $\alpha$ and noise precision $\beta$, [[Maximum a Posteriori Learning|MAP]] gives $\lambda = \alpha/\beta$ ([[Probabilistic Formulation of Regression]]).
- For sum-of-squares error, the regularized error $\tilde{E}(\mathbf{w}) = \frac{1}{2}\sum_{n=1}^N \{y(x_n, \mathbf{w}) - t_n\}^2 + \frac{\lambda}{2}\lVert\mathbf{w}\rVert^2$ can be minimized exactly in closed form.[^2]
- **The bias is treated separately**: the coefficient $w_0$ is often omitted from the regularizer, because penalizing it makes the results depend on the choice of origin for the target variable; alternatively it is included with its own regularization coefficient.[^2]
- An instance of **shrinkage methods** in statistics, so named because they shrink the values of the coefficients.[^2]

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
[^2]: [Bishop, 2006, p. 10](zotero://open-pdf/library/items/5G99AZ8U?page=30&annotation=D2XBTALG)
