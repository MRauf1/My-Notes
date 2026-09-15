---
tags:
  - computer_science
  - computer_vision
---

# Definition

If thinking of the input data $X_0$ as a data distribution, then [[Deep Neural Network]] transform the input data distribution into an output data distribution.

Each intermediate layer then, represents a certain [[Embedding]]/[[Representation (Machine Learning)|representation]] of the data. Formally, layer by layer, a deep net transforms the input data distribution $p_{data}$ into $p_1$, then $p_2$, and so on, until finally transforming the data into the output distribution $p_{out}$, where $p_\ell$ is the distribution of activations at layer $\ell$.

[[Loss Function]] then, can be thought of as penalizing the [[Divergence]] between the output distribution $p_{out}$ (equivalently $\hat{Y}$) and a target distribution $p_{target}$ (equivalently $Y$).[^1]

One can also think of it as disentangling the messy input data into a representation that can be cleanly separated. For example, the goal of a binary [[Softmax Function|softmax]] classifier is to move all class-$0$ datapoints to one point on the output layer and all class-$1$ datapoints to another. Empirically, this disentangling tends to happen gradually, layer by layer: in a network trained with contrastive language-image pre-training (CLIP) to output a direct representation of semantics, early-layer representations may not separate semantic classes well, while late-layer representations, closer to the output, place each class in a visibly different part of representational space.

[^1]: https://visionbook.mit.edu/neural_nets_as_distribution_transformers.html