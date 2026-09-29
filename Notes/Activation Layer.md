---
tags:
  - computer_science
  - computer_vision
---

# Definition

Layers in [[Deep Neural Network|DNNs]] that apply a [[Nonlinear Function|nonlinearity]] after a [[Linear Layer]]. Usually are [[Pointwise Function|pointwise functions]] and contain little to no parameters.[^1]

# Types

- [[Sigmoid Function|Sigmoid Function]]
- [[ReLU Function|ReLU Function]]
- [[Leaky ReLU]], [[Parametric ReLU]], [[Concatenated ReLU]]
- [[Softplus Function]], [[Gaussian Error Linear Unit]], [[Swish Function]], [[HardSwish Function]], [[Exponential Linear Unit]], [[Scaled Exponential Linear Unit]]

# Properties
- Necessary for a network to compute nonlinear functions at all: the composition of any number of [[Linear Layer|linear layers]] is itself just a linear function, so without activation layers a deep net could only represent linear input-output mappings.
- There is no definitive answer as to which activation is empirically superior; leaky, parametric, and many smooth variants give minor gains over the [[ReLU Function|ReLU]] in particular situations.[^2]

[^1]: https://visionbook.mit.edu/neural_nets.html
[^2]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
