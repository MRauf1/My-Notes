---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Batch Size)[^1]
> In [[Stochastic Gradient Descent]], the hyperparameter $B$ giving the number of training examples randomly subsampled, without replacement, to estimate the gradient of the [[Cost Function]] at each iteration, out of a full training set of size $N$.

# Properties
- Trades off the accuracy of the estimated gradient against its computational cost: a batch nearly as large as $N$ gives a gradient estimate close to the true, full-dataset gradient, while a smaller batch is less accurate but faster to compute.
- Once every example in the training set has been sampled in some batch, one **epoch** of training has completed.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
