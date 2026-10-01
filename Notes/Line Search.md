---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Line Search[^1]
> A procedure that, given a descent direction, samples the function along that direction to find the step size $\alpha$ that most decreases the loss, instead of using a fixed [[Learning Rate]].

# Properties
- Motivated by the inefficiency of fixed-step [[Gradient Descent]]: the distance moved depends entirely on the gradient magnitude, so it moves far where the function changes fast (where it should be cautious) and little where it changes slowly (where it should explore).
- One approach is **bracketing**, which repeatedly shrinks an interval known to contain the minimum along the line.
- Unnecessary for [[Newton's Method (Optimization)|Newton's method]], which sets the step from the curvature.

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
