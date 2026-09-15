---
tags:
  - computer_science
  - computer_vision
---

# Definition

[[Deep Neural Network|DNNs]] are universal approximation [[Function|functions]] meaning that they can approximate any continuous function on compact subsets of $\mathbb{R}^N$ (cannot fit non-computable functions). This holds true even for a DNN with only one hidden layer.[^1]

Proof idea (one hidden layer, step/sigmoid activations): a pair of oppositely-signed, shifted step functions sums to a rectangular "bump" that is nonzero only on a small interval; the hidden layer can construct many such weighted bumps, each approximating the target function's value on a small sub-interval of the domain, and summing enough of them approximates the target function arbitrarily well on a compact domain (similar in spirit to a Riemann sum with a piecewise-constant approximation).

# Properties
- A nonconstructive existence result: it guarantees a network with the right weights exists, but says nothing about whether [[Gradient Descent|gradient-based training]] will actually find those weights, nor how many training examples or how much compute that would take.
- The single-hidden-layer construction used in the proof is rarely how networks are built in practice; modern networks instead favor depth, both because certain functions need exponentially fewer neurons at greater depth (see [[Depth Separation]]) and because deep, compositional architectures tend to have better [[Inductive Bias|inductive biases]] and more favorable optimization landscapes than very wide, shallow ones.
- Later theoretical work has focused on approximation *rates*: how many parameters are needed to reach a given accuracy. Naively, fitting a general smooth function in high dimensions suffers from the curse of dimensionality, but when the target function has compositional or hierarchical structure, deep networks can approximate it with far fewer parameters than this naive rate would suggest.
- The classical Kolmogorov-Arnold representation theorem, which shows that any continuous multivariate function can be written as a finite composition of continuous univariate functions and addition, inspired **Kolmogorov-Arnold Networks (KANs)**, a 2024 architecture that places learnable univariate activation functions on the network's edges rather than fixed pointwise nonlinearities on its nodes, as an alternative route to universal approximation with potentially better parameter efficiency and interpretability on some tasks.

[^1]: https://visionbook.mit.edu/neural_nets.html