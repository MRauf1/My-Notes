---
tags:
  - computer_science
  - computer_vision
---

# Definition

Layer in [[Deep Neural Network|DNNs]] that compute a [[Linear Function|linear transformation]] on the input. They contain most of the DNNs parameters.[^1]

# Properties
- Mathematically, the function computed, $\mathbf{x}_{out} = \mathbf{W}\mathbf{x}_{in} + \mathbf{b}$, is [[Affine Transformation|affine]] rather than strictly linear, because of the added bias $\mathbf{b}$; it is called a linear layer only by convention, and can equivalently be viewed as a genuinely linear function of the augmented input $\begin{bmatrix}\mathbf{x}_{in} \\ 1\end{bmatrix}$.

[^1]: https://visionbook.mit.edu/neural_nets.html