---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Inductive Bias)[^1]
> The set of assumptions built into a learning algorithm's [[Hypothesis Space]] or optimization procedure that lead it to prefer some solutions over others, beyond what is strictly implied by the training data alone.

# Properties
- In Prince's terms: the tendency of a model to prioritize one solution over another *between data points*. Once a model fits the training data almost perfectly, extra capacity can only change its behaviour between the training points, so the inductive bias determines generalization in the over-parameterized regime ([[Double Descent]]).[^2]
- One of the reasons [[Deep Neural Network|deep nets]] work well: their architectures (e.g. convolutional weight-sharing, or attention) reflect real structure in the world, which biases the search toward learned solutions that capture true structure and so generalize, rather than toward arbitrary functions that merely fit the training data.
- [[The Bitter Lesson (Sutton)|Sutton's Bitter Lesson]] argues that hand-designed, human inductive biases tend to be outperformed over time by more general architectures paired with more data and compute, though inductive biases that reflect general mathematical structure of the world, such as invariances, may remain useful even as compute scales; see [[Priors in Light of the Bitter Lesson]].

- Example: on translated-template data, a [[Convolutional Neural Network|CNN]] generalizes better than a fully connected network because it is forced to process every position in the same way; the convolutional structure can be viewed as a [[Regularization|regularizer]] placing an infinite penalty on most solutions a fully connected network can describe ([[Convolutional Layer]]).[^3]
- Example: the [[Vision Transformer]] lacks the convolutional inductive bias and underperforms CNNs on modest data, but surpasses them when pre-trained on extremely large datasets.[^4]
- Example: a [[Graph Convolutional Network]] has a **relational inductive bias**, i.e. a bias toward prioritizing information from a node's neighbours.[^5]

[^1]: [MIT Vision Book - Neural Networks](https://visionbook.mit.edu/neural_nets.html)
[^2]: [Prince, p. 129](zotero://open-pdf/library/items/BWT7FYX5?page=143&annotation=XN6MRP3D)
[^3]: [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=ZKKHF27M); [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=EE2MMBYY)
[^4]: [Prince, p. 230](zotero://open-pdf/library/items/BWT7FYX5?page=244&annotation=8CLW5ECL); [Prince, p. 238](zotero://open-pdf/library/items/BWT7FYX5?page=252&annotation=AEG4IWZR)
[^5]: [Prince, p. 248](zotero://open-pdf/library/items/BWT7FYX5?page=262&annotation=V6VVW959)
