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

# Properties
- Necessary for a network to compute nonlinear functions at all: the composition of any number of [[Linear Layer|linear layers]] is itself just a linear function, so without activation layers a deep net could only represent linear input-output mappings.

[^1]: https://visionbook.mit.edu/neural_nets.html