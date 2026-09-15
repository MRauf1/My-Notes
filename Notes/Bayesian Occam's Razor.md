---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Bayesian Occam's Razor)[^1]
> A probabilistic justification for [[Occam's Razor]]: because the total prior probability mass over all hypotheses in a [[Hypothesis Space]] must sum to $1$, a more complex hypothesis space, which covers more possible hypotheses, must assign less prior mass to any single hypothesis within it. Simpler hypotheses are therefore, all else being equal, more probable a priori.

# Properties
- Justifies interpreting a [[Regularization|regularizer]] as a [[Bayes' Theorem|prior]] $p(\theta)$ that is not arbitrarily chosen, but reflects how prior mass is necessarily distributed more thinly over more expressive hypothesis spaces.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
