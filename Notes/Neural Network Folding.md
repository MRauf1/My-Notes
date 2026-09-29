---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Neural Network Folding[^1]
> An interpretation of composing networks $\mathbf{y}' = \mathbf{f}_2[\mathbf{f}_1[\mathbf{x}]]$: the first network "folds" the input space back onto itself so that multiple inputs map to the same output, and the second network applies a function that is then replicated at every set of points folded on top of one another.

# Properties
- With [[ReLU Function|ReLU]] activations the composition is still piecewise linear, but can have more linear regions than a [[Shallow Neural Network]] with the same total number of hidden units: if the first network maps three ranges of $x$ onto the same output range, the second network's function is duplicated three times, turning two 3-unit networks into a function with $9$ regions ([[Linear Regions of ReLU Network]]).[^2]
- Alternative view: each layer creates new functions that are clipped (creating new regions) and recombined. Folding emphasizes the dependencies in the output function but not how clipping creates new joints; the clipping view has the opposite emphasis. Both give only partial insight, and the network remains merely an equation relating $\mathbf{x}$ to $\mathbf{y}'$.[^3]
- Explains the symmetries among the many regions of a [[Deep Neural Network]], which are only an advantage if the target function has similar symmetries or compositional structure.[^4]

[^1]: [Prince, p. 41](zotero://open-pdf/library/items/BWT7FYX5?page=55&annotation=4S6RC2IY); [Prince, p. 43](zotero://open-pdf/library/items/BWT7FYX5?page=57&annotation=BM6SXACS)
[^2]: [Prince, p. 43](zotero://open-pdf/library/items/BWT7FYX5?page=57&annotation=V9EVV57V)
[^3]: [Prince, p. 46](zotero://open-pdf/library/items/BWT7FYX5?page=60&annotation=B5AT9DM2)
[^4]: [Prince, p. 50](zotero://open-pdf/library/items/BWT7FYX5?page=64&annotation=ANIWQU9S)
