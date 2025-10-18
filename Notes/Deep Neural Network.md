---
tags: computer_science, deep_learning, computer_vision
---

# Definition

[[Function|Function]] that can represent a very broad family of relationships between inputs and outputs. Neural network is what powers [[Deep Learning|deep learning]].[^1]

The parameters (meta-summary of the data) are a statistic of the dataset (slow functions since need to optimize over the dataset to obtain), while the activations (summary of the data) are a statistic of a datapoint/sample (fast functions since need to compute a few layers to obtain).[^2]

Both increasing depth and width can increase the complexity of the model, but increasing depth usually requires far fewer parameters as shown by empirical results (and some preliminary theoretical results).

# Components
## Linear Layers
- [[Linear Layer|Linear Layer]]
- [[Convolutional Layer]]
- [[Attention Layer]]

## Non-Linear Layer
- [[Activation Layer|Activation Layer]]
- [[Normalization Layer|Normalization Layer]]

## Output Layer
- [[Output Layer|Output Layer]]

# Advantages
- They are [[Universal Approximation Theorem|universal approximators]]
- They are [[Differentiable Function|differentiable]]
- They have good inductive biases - neural architectures reflect the real structure in the world
- They can be processed using parallel hardware
- They build increasingly abstracted representations of the data as the data moves through the layers

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=19)
[^2]: https://visionbook.mit.edu/neural_nets.html