---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Model Capacity)[^1]
> The expressivity of a [[Hypothesis Space]]: roughly, how wide a range of input-output mappings it is able to represent.

# Properties
- The number of free parameters is only a rough proxy for model capacity, not the full story: a single infinite-precision parameter can already parameterize an arbitrarily complex function and so define a very expressive (high-capacity) hypothesis space, while a million parameters that are [[Regularization|regularized]] to be almost all zero may define only a simple class of functions.
- Should follow a "Goldilocks principle": a hypothesis space should be expressive enough to fit the data, but not so flexible that it [[Overfitting|overfits]] it.
- **Why overparameterized deep networks often do not overfit despite very high nominal capacity** is an active area of research; several strands of evidence and theory bear on it:
	- **Double descent**: as capacity increases past the point of exactly interpolating the training data, test error can first worsen (as classical theory predicts) but then *decrease* again into the heavily overparameterized regime, contrary to the classical U-shaped bias-variance tradeoff curve.
	- **Benign overfitting**: overparameterized models can perfectly interpolate noisy training data while still generalizing well, because the interpolating solution found by training spreads the fit to noise thinly across many directions instead of concentrating it, so it barely harms predictions elsewhere.
	- **Implicit regularization of [[Gradient Descent|gradient-based]] training**: among the many parameter settings that fit the training data, [[Stochastic Gradient Descent|(stochastic) gradient descent]] tends to converge to comparatively simple, low-norm, or flat-minimum solutions rather than an arbitrary interpolating one, effectively regularizing the model without an explicit regularizer.
	- Together, these suggest that a model's *effective* capacity, as constrained by its architecture and optimizer, can be far lower than its nominal parameter count would suggest.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
