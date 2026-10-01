---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Saddle Point[^1]
> A point where the gradient is zero but the function increases in some directions and decreases in others; equivalently, a stationary point at which the [[Hessian Matrix]] has both positive and negative eigenvalues (positive in the directions where the point is a minimum, negative in those where it is a maximum).

# Properties
- Classification of stationary points by the Hessian's eigenvalues: all positive gives a minimum, all negative a maximum, mixed signs a saddle point.
- [[Gradient Descent]] can escape if not exactly at the saddle point, but the surface nearby is flat, so terminating when the gradient is small may stop erroneously near one.
- [[Stochastic Gradient Descent]] reduces the chance of getting stuck, since some batches are likely to have significant gradient at any point.

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
