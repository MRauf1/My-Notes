---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Group Normalization (GroupNorm)[^1]
> A [[Normalization Layer|normalization layer]] that, for each data example separately, divides the channels into groups and standardizes each group using the [[Mean|mean]] and standard deviation computed across the within-group channels and the spatial positions (Wu & He, 2018). As in the other schemes, a separate learned scale $\gamma$ and offset $\delta$ is applied per channel.

![[Normalization Schemes.png]]

# Properties
- Like [[Layer Normalization]], it avoids batch statistics, so it is independent of the batch size and other batch members.
- Interpolates between [[Layer Normalization]] (one group containing all channels) and [[Instance Normalization]] (one group per channel).

[^1]: [Prince, p. 203](zotero://open-pdf/library/items/BWT7FYX5?page=217&annotation=E94CD4T3); [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=WQAIWEGA)
