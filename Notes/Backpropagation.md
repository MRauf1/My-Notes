---
tags:
  - computer_science
  - computer_vision
---

# Definition

Backpropagation is an algorithm for calculating the gradient of the [[Loss Function]] with respect to every parameter in a [[Computation Graph]].

In a [[Deep Neural Network]] with parameters $\theta$, the forward pass is $x_{out} = f(x_{in}, \theta)$. The backward pass is the part for calculating and updating gradients. 

Backward pass for a [[Linear Function]] is the same as the forward pass for a linear layer, but with the weights transposed. Backward pass itself can be viewed as a reversed neural network of the forward pass.
Forward network is a [[Hypernetwork]] that parameterizes the backward network.
The backward pass can always be represented solely by linear layers since the chain rule is just a product of [[Jacobian Matrix]].

The [[Gradient Vector]] for each parameter is calculated using [[Chain Rule]] and these gradients are used to update the parameters.[^1]

For efficiency purposes, during the forward pass, some of the calculations/information can be stored and reused in the backward pass since there is a lot of repeated calculations that must be done. Thus, by using [[Dynamic Programming]], the results are stored and reused when needed. It will take additional memory, but it will bring about speed improvements.

![[Pasted image 20250923175817.png]]

Concretely, the gradients for different parameters, $\partial J/\partial\theta_1$ and $\partial J/\partial\theta_2$, written out via the [[Chain Rule|chain rule]], share most of the same factors, e.g. $\partial J/\partial\mathbf{x}_L, \partial\mathbf{x}_L/\partial\mathbf{x}_{L-1}, \dots, \partial\mathbf{x}_2/\partial\mathbf{x}_1$; rather than evaluating each parameter's gradient independently, backpropagation evaluates each shared factor once and reuses it for every parameter that needs it. Operationally, this is organized as a **forward pass**, evaluating layer by layer to produce the sequence of activations $\mathbf{x}_0, \mathbf{x}_1, \dots, \mathbf{x}_L$, followed by a **backward pass**, iteratively evaluating a corresponding sequence of gradients $\mathbf{g}_L, \mathbf{g}_{L-1}, \dots, \mathbf{g}_0$ alongside the parameter gradient for each layer.

For computing the gradients over a batch, use the following identity: $\frac{\partial \frac{1}{N} \sum_{i=1}^N J_i(\theta)}{\partial \theta} = \frac{1}{N} \sum_{i=1}^N \frac{\partial J_i(\theta)}{\partial \theta}$.

# Properties
- Does not distinguish between parameters and data — both are treated as generic inputs to parameterless modules of the [[Computation Graph]]. For a learning problem using neural net $F = f_L \circ \dots \circ f_1$ and loss function $\mathcal{L}$, the full computation graph is $\mathcal{L}(F(\mathbf{x}_0), \mathbf{y}, \theta) \triangleq J(\mathbf{x}_0, \mathbf{y}, \theta)$: in the forward direction, the inputs are the data and parameters and the output is the loss; in the backward direction, the input is the number $1$ and the outputs are the gradients of the loss with respect to both the data and the parameters.
- Because data and parameter inputs play symmetric roles, just as one can optimize parameters to minimize the loss by descending the parameter gradient, one can equally optimize the input data to minimize (or maximize) some quantity by descending (or ascending) the data gradient; [[Activation Maximization]] is one application of this, used to visualize which inputs a given neuron is sensitive to.

# Alternatives
- [[Hebbian Learning]], a more biologically plausible, bottom-up alternative that updates weights locally based on feedforward activity rather than backpropagated error.
- Zeroth-order optimizers, such as an [[Evolution Strategy]], which can optimize a neural network's parameters using only [[Cost Function|cost]] values, without computing any gradients at all.

[^1]: https://visionbook.mit.edu/backpropagation.html