---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Instance Normalization (InstanceNorm)[^1]
> A [[Normalization Layer|normalization layer]] that standardizes each channel of each data example separately, using the [[Mean|mean]] and standard deviation computed across the spatial positions alone (Ulyanov et al., 2016), followed by a learned per-channel scale $\gamma$ and offset $\delta$.

![[Normalization Schemes.png]]

# Properties
- The extreme case of [[Group Normalization]] in which the number of groups equals the number of channels.[^1]
- Uses no batch statistics, unlike [[Batch Normalization]].

[^1]: [Prince, p. 203](zotero://open-pdf/library/items/BWT7FYX5?page=217&annotation=E94CD4T3); [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=IWF2TIB4); [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=WQAIWEGA)
