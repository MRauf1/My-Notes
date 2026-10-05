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
- [[Convolutional Layer]] ([[Convolutional Neural Network]])
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
- General form with $K$ hidden layers, hidden vectors $\mathbf{h}_k$, biases $\boldsymbol{\beta}_k$, and weights $\boldsymbol{\Omega}_k$:[^3]
$$
\begin{align}
\mathbf{h}_1 &= \mathbf{a}[\boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}] \\
\mathbf{h}_{k+1} &= \mathbf{a}[\boldsymbol{\beta}_k + \boldsymbol{\Omega}_k \mathbf{h}_k], \quad k = 1, \dots, K-1 \\
\mathbf{y} &= \boldsymbol{\beta}_K + \boldsymbol{\Omega}_K \mathbf{h}_K
\end{align}
$$
with parameters $\boldsymbol{\phi} = \{\boldsymbol{\beta}_k, \boldsymbol{\Omega}_k\}_{k=0}^{K}$. If layer $k$ has $D_k$ units, then $\boldsymbol{\beta}_{k-1} \in \mathbb{R}^{D_k}$, $\boldsymbol{\beta}_K \in \mathbb{R}^{D_o}$, $\boldsymbol{\Omega}_0 \in \mathbb{R}^{D_1 \times D_i}$, $\boldsymbol{\Omega}_k \in \mathbb{R}^{D_{k+1} \times D_k}$, and $\boldsymbol{\Omega}_K \in \mathbb{R}^{D_o \times D_K}$. Equivalently, $\mathbf{y} = \boldsymbol{\beta}_K + \boldsymbol{\Omega}_K \mathbf{a}[\boldsymbol{\beta}_{K-1} + \boldsymbol{\Omega}_{K-1} \mathbf{a}[\dots \boldsymbol{\beta}_1 + \boldsymbol{\Omega}_1 \mathbf{a}[\boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}] \dots]]$.
- The number of hidden units per layer is the **width** and the number of hidden layers the **depth**; the total number of hidden units measures [[Model Capacity|capacity]]. Modern networks may have over a hundred layers with thousands of units each.[^4]
- $K$ and $D_1, \dots, D_K$ are [[Hyperparameter|hyperparameters]]: for fixed hyperparameters the network describes a family of functions and the parameters pick one, so neural networks represent a family of families of functions.[^4]
- With [[ReLU Function|ReLU]] activations it is piecewise linear, with many more linear regions per parameter than a [[Shallow Neural Network]] ([[Linear Regions of ReLU Network]], [[Neural Network Folding]]).
- Practical advantages over shallow networks: some functions need exponentially fewer units ([[Depth Separation]], [[Width Efficiency]]); local-to-global processing, e.g. integrating information over increasingly large image regions, is hard to specify without multiple layers; moderately deep networks are usually easier to fit, perhaps because [[Overparameterized Model|over-parameterized]] deep models have a large family of roughly equivalent, easy-to-find solutions, though training becomes harder again with many more layers; and they seem to generalize better. The last two effects are not well understood.[^5]

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=19)
[^2]: https://visionbook.mit.edu/neural_nets.html
[^3]: [Prince, p. 49](zotero://open-pdf/library/items/BWT7FYX5?page=63&annotation=4H3JUA84); [Prince, p. 49](zotero://open-pdf/library/items/BWT7FYX5?page=63&annotation=HEQQF3EQ)
[^4]: [Prince, p. 46](zotero://open-pdf/library/items/BWT7FYX5?page=60&annotation=AIZB9MQV); [Prince, p. 46](zotero://open-pdf/library/items/BWT7FYX5?page=60&annotation=3BIZK6QZ)
[^5]: [Prince, p. 50](zotero://open-pdf/library/items/BWT7FYX5?page=64&annotation=Z47Q3DJK); [Prince, p. 51](zotero://open-pdf/library/items/BWT7FYX5?page=65&annotation=RHI4F738); [Prince, p. 51](zotero://open-pdf/library/items/BWT7FYX5?page=65&annotation=FXJI5B96); [Prince, p. 51](zotero://open-pdf/library/items/BWT7FYX5?page=65&annotation=RAAB8TPA)
