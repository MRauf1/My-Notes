---
tags:
  - computer_science
  - deep_learning
  - computer_vision
---

# Definition

[[Function|Function]] that can represent a very broad family of relationships between inputs and outputs. Neural network is what powers [[Deep Learning|deep learning]].[^1]

The parameters (meta-summary of the data) are a statistic of the dataset (slow functions since need to optimize over the dataset to obtain), while the activations (summary of the data) are a statistic of a datapoint/sample (fast functions since need to compute a few layers to obtain).[^2] Both are [[Tensor|tensors]] of variables.

Each layer can be viewed as a function $\mathbf{x}_{l+1} = f_{l+1}(\mathbf{x}_l, \theta_{l+1})$ of both the previous layer's activations and the current layer's parameters, so a deep net as a whole is the composition $f(\mathbf{x}) = f_L(f_{L-1}(\dots f_2(f_1(\mathbf{x}))))$. Because activations and parameters enter a layer symmetrically, anything that can be done by varying the parameters can instead be done by varying the (input) activations, and vice versa; this is the basis of techniques such as network prompting, adversarial attacks, and network visualization (e.g. [[Activation Maximization]]), which hold the parameters fixed and instead optimize the input activations to achieve some objective.

Both increasing depth and width (the number of neurons in a single hidden layer) can increase the complexity of the model, but increasing depth usually requires far fewer parameters as shown by empirical results (and some preliminary theoretical results); see [[Depth Separation]] for one line of theory explaining this.

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
- They are [[Universal Approximation Theorem|universal approximators]]: a sufficiently large network's [[Hypothesis Space]] is big enough that the true solution, or a close approximation to it, very likely lies within it.
- They are [[Differentiable Function|differentiable]]: [[Gradient Descent|gradients]] make searching this large hypothesis space for a good fit tractable, unlike a hypothesis space that could only be searched by [[Zeroth-Order Optimization|zeroth-order]] methods.
- They have good [[Inductive Bias|inductive biases]] - neural architectures reflect the real structure in the world, biasing the search toward solutions that capture true structure and therefore generalize, rather than toward arbitrary functions that merely fit the training data.
- They can be processed using parallel hardware: both matrix multiplies (linear layers) and pointwise operations (e.g., activation layers) parallelize well on GPUs, and batches of data can be split across parallel compute nodes.
- They build increasingly abstracted representations of the data as the data moves through the layers

# Properties
- [[Latent Variables]]

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=19)
[^2]: https://visionbook.mit.edu/neural_nets.html