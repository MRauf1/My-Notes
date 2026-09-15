---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Representation (Machine Learning))[^1]
> The activations at a given layer of a network, viewed as an embedding of the input data into that layer's representational space.

# Properties
- Each layer of a [[Deep Neural Network|deep net]] computes a different representation, or **embedding**, of the data; viewing the net as a [[Neural Network as Distribution Transformer|distribution transformer]], the distribution of activations at layer $\ell$ is denoted $p_\ell$.
- A network trained to make semantic classes easy to separate, such as one trained with contrastive language-image pre-training (CLIP), disentangles the input data layer by layer: early-layer representations may not separate semantic classes well, while late-layer representations, closer to the output, occupy visibly different parts of representational space for different classes.
- The geometry of a representation can be highly non-uniform; see [[ReLU Function Geometric Properties]] for how ReLU activations concentrate representational density along the axes of the positive orthant, leaving much of high-dimensional representational space unoccupied.

[^1]: [MIT Vision Book - Neural Networks as Distribution Transformers](https://visionbook.mit.edu/neural_nets_as_distribution_transformers.html)
