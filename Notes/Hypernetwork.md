---
tags:
  - computer_science
  - computer_vision
---

# Definition

Hypernetwork is a [[Deep Neural Network]] that outputs values that parameterize another neural network.[^1]

# Properties
- [[Self-Attention]] is an example: the attention weights that linearly combine the values are computed by another branch (queries, keys, dot products, softmax) from the same input, which makes the overall computation nonlinear.[^2]

[^1]: https://visionbook.mit.edu/backpropagation.html
[^2]: [Prince, p. 209](zotero://open-pdf/library/items/BWT7FYX5?page=223&annotation=BCCM9EHH)
