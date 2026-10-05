---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Data Augmentation[^1]
> Expanding the training set by transforming each input example in a way that leaves its label unchanged, teaching the model to be indifferent to these irrelevant transformations.

# Properties
- One of three ways of exploiting extra data: [[Transfer Learning]] uses a different dataset, [[Multitask Learning]] uses additional labels, and augmentation expands the dataset itself.
- Builds the desired invariances ([[Invariant Function]]) into the model through data rather than architecture ([[Inductive Bias]]), whereas a [[Convolutional Neural Network|CNN]] builds translation equivariance into the architecture.

[^1]: [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=RUSDFTRR); [Prince, p. 154](zotero://open-pdf/library/items/BWT7FYX5?page=168&annotation=387ZX5NI)
