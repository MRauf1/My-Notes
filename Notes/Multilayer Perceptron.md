---
tags:
  - computer_science
  - computer_vision
---

# Definition

A [[Perceptron|perceptron]] with multiple (linear + activation) layers stacked together.[^1]

The composition of [[Nonlinear Function|nonlinear functions]] means that the MLP can approximate nonlinear [[Function|functions]] in addition to linear ones.

An input **layer** of data $\mathbf{x}$ is mapped to a layer of outputs $\mathbf{y}$, via one or more **hidden units** in between (the **hidden layer**), each computed as $h = g(z)$ for a hidden unit's pre-activation $z$ and [[Activation Layer|activation function]] $g$. Since each neuron in the network acts as a perceptron, and this network has multiple layers of neurons, it is called a multilayer perceptron. For a single hidden layer:
$$
\begin{align}
\mathbf{z} &= \mathbf{W}_1\mathbf{x} + \mathbf{b}_1 \\
\mathbf{h} &= g(\mathbf{z}) \\
\mathbf{y} &= \mathbf{W}_2\mathbf{h} + \mathbf{b}_2
\end{align}
$$
In general, MLPs can be constructed with any number of layers following this pattern: linear layer, activation function, linear layer, activation function, and so on; this linear-nonlinear motif recurs throughout almost all neural networks, including [[Deep Neural Network|deep nets]].

[^1]: https://visionbook.mit.edu/neural_nets.html