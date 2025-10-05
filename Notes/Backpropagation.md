---
tags: computer_science, computer_vision
---

# Definition

Backpropagation is an algorithm for calculating the gradient of the [[Loss Function]] with respect to every parameter in a [[Computation Graph]].

In a [[Deep Neural Network]] with parameters $\theta$, the forward pass is $x_{out} = f(x_{in}, \theta)$. The backward pass is the part for calculating and updating gradients. 

Backward pass for a [[Linear Function]] is the same as the forward pass for a linear layer, but with the weights transposed. Backward pass itself can be viewed as a reversed neural network of the forward pass.
Forward network is a [[Hypernetwork]] that parameterizes the backward network.
The backward pass can always be represented solely by linear layers since the chain rule is just a product of [[Jacobian Matrix]].

The [[Gradient]] for each parameter is calculated using [[Chain Rule]] and these gradients are used to update the parameters.[^1]

For efficiency purposes, during the forward pass, some of the calculations/information can be stored and reused in the backward pass since there is a lot of repeated calculations that must be done. Thus, by using [[Dynamic Programming]], the results are stored and reused when needed. It will take additional memory, but it will bring about speed improvements.

![[Pasted image 20250923175817.png]]

For computing the gradients over a batch, use the following identity: $\frac{\partial \frac{1}{N} \sum_{i=1}^N J_i(\theta)}{\partial \theta} = \frac{1}{N} \sum_{i=1}^N \frac{\partial J_i(\theta)}{\partial \theta}$.

[^1]: https://visionbook.mit.edu/backpropagation.html