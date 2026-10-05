---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Network Dissection[^1]
> An [[Interpretability (Machine Learning)|interpretability]] method that passes images with known pixel labels (color, texture, object type, etc.) through a network and measures the correlation of each hidden unit with each labelled property.

# Properties
- Uses only the forward pass and requires no optimization, unlike [[Feature Visualization]] or [[Activation Maximization]].[^1]
- Showed that in [[Convolutional Neural Network|CNNs]] earlier layers correlate more with texture and color and later layers with object type.[^1]
- Introduced by Bau et al. (2017).

[^1]: [Prince, p. 184](zotero://open-pdf/library/items/BWT7FYX5?page=198&annotation=7WATMM6L)
