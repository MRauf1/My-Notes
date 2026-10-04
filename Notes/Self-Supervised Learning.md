---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Self-Supervised Learning[^1]
> Creating large amounts of "free" labelled data from unlabelled data by defining a secondary task whose labels come from the data itself, typically used to pre-train a network for [[Transfer Learning]].

# Types
- **Generative**: mask part of each data example and predict the missing part.
- **Contrastive**: compare pairs of examples with commonalities against unrelated pairs, e.g. whether two images are transformed versions of one another, or whether two sentences followed one another in a document; sometimes the precise relationship within a connected pair must be identified (e.g. the relative position of two patches of an image).

# Properties
- Sits between [[Supervised Learning]] and [[Unsupervised Learning]]: no human labels, but trained with supervised-style losses ([[Loss Function Taxonomy]] lists contrastive losses).

[^1]: [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=LNWFRNLX); [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=MBT9GCER); [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=REGDEM4V)
