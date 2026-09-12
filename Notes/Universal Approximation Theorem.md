---
tags:
  - computer_science
  - computer_vision
---

# Definition

[[Deep Neural Network|DNNs]] are universal approximation [[Function|functions]] meaning that they can approximate any continuous function on compact subsets of $\mathbb{R}^N$ (cannot fit non-computable functions). This holds true even for a DNN with only one hidden layer.[^1]

Proof idea (one hidden layer, step/sigmoid activations): a pair of oppositely-signed, shifted step functions sums to a rectangular "bump" that is nonzero only on a small interval; the hidden layer can construct many such weighted bumps, each approximating the target function's value on a small sub-interval of the domain, and summing enough of them approximates the target function arbitrarily well on a compact domain (similar in spirit to a Riemann sum with a piecewise-constant approximation).

[^1]: https://visionbook.mit.edu/neural_nets.html