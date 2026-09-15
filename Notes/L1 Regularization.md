---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (L1 Regularization)[^1]
> [[Lp Regularization]] with $p=1$: a regularizer $R(\theta) = \lVert\theta\rVert_1$ penalizing the sum of absolute values of the parameters. In regression settings, also known as **Lasso**.

# Properties
- Encourages many parameters to become exactly zero, producing sparse solutions, unlike [[L2 Regularization]], which shrinks parameters toward but not exactly to zero.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
