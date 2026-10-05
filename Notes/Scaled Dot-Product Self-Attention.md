---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Scaled Dot-Product Self-Attention[^1]
> [[Self-Attention]] in which the dot products are divided by the square root of the query/key dimension $D_q$ (the number of rows of $\boldsymbol{\Omega}_q$ and $\boldsymbol{\Omega}_k$) before the softmax:
> $$
> \begin{align}
> \mathbf{Sa}[\mathbf{X}] = \mathbf{V} \cdot \mathbf{Softmax}\left[\frac{\mathbf{K}^T \mathbf{Q}}{\sqrt{D_q}}\right]
> \end{align}
> $$

# Properties
- **Why scale**: unscaled dot products can have large magnitude, pushing the [[Softmax Function|softmax]] into a region where the largest argument completely dominates; small input changes then barely affect the output, so gradients are tiny ([[Vanishing Gradients]]) and the model is hard to train.[^1]
- If the entries of $\mathbf{q}$ and $\mathbf{k}$ are independent with zero mean and unit variance, $\mathbf{k}^T\mathbf{q} = \sum_{d=1}^{D_q} k_d q_d$ has variance $D_q$; dividing by $\sqrt{D_q}$ restores unit variance regardless of dimension.[^2]
- The standard attention used in each head of [[Multi-Head Self-Attention]].

[^1]: [Prince, p. 214](zotero://open-pdf/library/items/BWT7FYX5?page=228&annotation=677ZFUPL)
[^2]: Added from general knowledge (Vaswani et al., 2017).
