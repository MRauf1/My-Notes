---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (L2 Regularization)[^1]
> [[Lp Regularization]] with $p=2$: a regularizer $R(\theta) = \lVert\theta\rVert_2$ penalizing the Euclidean norm of the parameters. Also known as **Tikhonov regression** or **ridge regression**, and, in the context of neural networks, as **weight decay**.

# Properties
- Encourages most parameters to be small (near zero) rather than exactly zero, unlike [[L1 Regularization]].
- Corresponds, under the probabilistic interpretation of regularizers as priors, to a Gaussian prior on $\theta$.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
