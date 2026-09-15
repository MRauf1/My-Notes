---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Learning Rate Schedule)[^1]
> A function $\text{lr}(\eta^0, k)$ giving the [[Learning Rate]] $\eta^k$ to use on iteration $k$ of [[Gradient Descent|gradient descent]], typically decaying from an initial value $\eta^0$ so that $\eta^{k+1} < \eta^k$, taking smaller steps as the minimizer is approached.

# Properties
- Common schedules include exponential decay, $\text{lr}(\eta^0,k) = \beta^{-k}\eta^0$; stepwise exponential decay, $\text{lr}(\eta^0,k) = \beta^{-\lfloor k/M \rfloor}\eta^0$; and linear decay, $\text{lr}(\eta^0,k) = \frac{K-k}{K}\eta^0$; where $\beta$ and $M$ are additional hyperparameters.
- Linear decay depends on the total number of steps $K$, which makes it harder to compare optimization runs of different lengths; more advanced schedules, such as cosine decay, share this issue for some settings of $K$.
- Variations include only decaying the learning rate when a plateau is reached, i.e. when the loss has not decreased for many iterations in a row.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
