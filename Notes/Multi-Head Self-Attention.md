---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Multi-Head Self-Attention[^1]
> $H$ [[Scaled Dot-Product Self-Attention|scaled dot-product self-attention]] mechanisms (**heads**) applied in parallel, each with its own parameters $\{\boldsymbol{\beta}_{vh}, \boldsymbol{\Omega}_{vh}\}, \{\boldsymbol{\beta}_{qh}, \boldsymbol{\Omega}_{qh}\}, \{\boldsymbol{\beta}_{kh}, \boldsymbol{\Omega}_{kh}\}$:
> $$
> \begin{align}
> \mathbf{V}_h &= \boldsymbol{\beta}_{vh}\mathbf{1}^T + \boldsymbol{\Omega}_{vh}\mathbf{X}, \quad
> \mathbf{Q}_h = \boldsymbol{\beta}_{qh}\mathbf{1}^T + \boldsymbol{\Omega}_{qh}\mathbf{X}, \quad
> \mathbf{K}_h = \boldsymbol{\beta}_{kh}\mathbf{1}^T + \boldsymbol{\Omega}_{kh}\mathbf{X} \\
> \mathbf{Sa}_h[\mathbf{X}] &= \mathbf{V}_h \cdot \mathbf{Softmax}\left[\frac{\mathbf{K}_h^T \mathbf{Q}_h}{\sqrt{D_q}}\right]
> \end{align}
> $$
> The head outputs are vertically concatenated and recombined by a further linear transform $\boldsymbol{\Omega}_c$:
> $$
> \begin{align}
> \mathbf{MhSa}[\mathbf{X}] = \boldsymbol{\Omega}_c \left[\mathbf{Sa}_1[\mathbf{X}]^T, \mathbf{Sa}_2[\mathbf{X}]^T, \dots, \mathbf{Sa}_H[\mathbf{X}]^T\right]^T
> \end{align}
> $$

![[Multi-Head Self-Attention.png]]

# Properties
- Typically, with input dimension $D$, the values, queries, and keys of each head have dimension $D/H$, so the concatenation is $D \times N$ again and the cost is similar to a single full-width head; this allows an efficient implementation.[^1]
- Multiple heads seem necessary for [[Self-Attention|self-attention]] to work well; it has been speculated that they make the network more robust to bad initializations.[^2]
- First sub-block of the [[Transformer Layer]].

[^1]: [Prince, p. 214](zotero://open-pdf/library/items/BWT7FYX5?page=228&annotation=TX3HFFNS); [Prince, p. 215](zotero://open-pdf/library/items/BWT7FYX5?page=229&annotation=FIFSISJL)
[^2]: [Prince, p. 215](zotero://open-pdf/library/items/BWT7FYX5?page=229&annotation=N76NMSI3)
