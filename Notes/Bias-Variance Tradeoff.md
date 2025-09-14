---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 ([[Bias]]-[[Variance]] Tradeoff)[^1]
> Test [[Mean Squared Error]] can be decomposed into
> $$
> \begin{align}
> E[y_0 - \hat{f}(x_0)]^2 = Var[\hat{f}(x_0)] + (Bias[\hat{f}(x_0)])^2 + Var[\epsilon]
> \end{align}
> $$
> To minimize the error, need to simultaneously achieve low [[Variance]] and low [[Bias]].
> [[Variance]] refers to how much $\hat{f}$ would change if we estimated it using a different training data set. [[Bias]] refers to the error introduced by approximating a real-life problem by a much simpler model.

In general, more flexible models have high [[Variance]] and low [[Bias]].

#TODO 
Is this decomposition for MSE only or does it work in general for any loss function?

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=42)