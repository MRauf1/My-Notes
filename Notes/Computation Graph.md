---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Computation Graph)[^1]
> A representation of computation as a graph of modular layers chained together, where each layer takes in some inputs and transforms them into some outputs (its **forward** pass), acting in isolation from the rest of the graph. If a layer has parameters, they are treated as an additional input to an otherwise parameter-free transformation.

# Properties
- [[Backpropagation]] computes the gradient of the loss with respect to every parameter, and symmetrically every data input, in a computation graph by defining, for each layer, a **backward** operation alongside its forward one.
- Backpropagation treats parameters and data identically, as generic inputs to parameterless modules, which is why techniques that optimize data inputs, such as [[Activation Maximization]], can reuse the same machinery used to optimize parameters.

[^1]: [MIT Vision Book - Backpropagation](https://visionbook.mit.edu/backpropagation.html)
