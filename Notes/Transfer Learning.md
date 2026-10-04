---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Transfer Learning[^1]
> Pre-training a network on a related secondary task for which data are plentiful, then adapting it to the original task, typically by removing the last layer and adding one or more layers producing a suitable output. Either the main model is fixed and only the new layers are trained, or the entire model is **fine-tuned**.

# Properties
- The network builds a good internal [[Representation (Machine Learning)|representation]] on the secondary task that can be exploited for the original task.
- Equivalently, it initializes most parameters in a sensible part of parameter space likely to yield a good solution.
- Improves performance by exploiting a different dataset, whereas [[Multitask Learning]] uses additional labels and [[Data Augmentation]] expands the dataset.[^2]
- When no large labelled secondary dataset exists, [[Self-Supervised Learning]] can create one.

[^1]: [Prince, p. 151](zotero://open-pdf/library/items/BWT7FYX5?page=165&annotation=Q5DCIPM5); [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=LPMKZIBB); [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=I3N83LDE)
[^2]: [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=RUSDFTRR)
