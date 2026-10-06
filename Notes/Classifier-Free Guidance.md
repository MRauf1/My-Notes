---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Classifier-Free Guidance[^1][^2]
> Conditional generation in a [[Diffusion Model|diffusion model]] without a separate classifier: the class $c$ is fed into the noise predictor $\mathbf{g}_t[\mathbf{z}_t, \boldsymbol{\phi}_t, c]$ (as an embedding added to the [[U-Net]] layers, like the time step), and the conditioning is randomly dropped (replaced by a null token $\varnothing$) during training, so one network learns both the conditional and the unconditional model (Ho & Salimans, 2022). At sampling time the two are combined with a guidance weight $w$:
> $$
> \begin{align}
> \tilde{\mathbf{g}}_t[\mathbf{z}_t, c] = (1+w)\,\mathbf{g}_t[\mathbf{z}_t, \boldsymbol{\phi}_t, c] - w\,\mathbf{g}_t[\mathbf{z}_t, \boldsymbol{\phi}_t, \varnothing]
> \end{align}
> $$

# Properties
- **Implicit classifier**: since $\mathbf{g} \propto -\nabla\log q$, the difference $\mathbf{g}[\mathbf{z}_t, c] - \mathbf{g}[\mathbf{z}_t, \varnothing] \propto -\nabla\log Pr(c|\mathbf{z}_t)$ by [[Bayes' Theorem]], so the combination mimics [[Classifier Guidance]] with scale $1 + w$.
- Can generate unconditionally ($w = -1$), conditionally ($w = 0$), or any weighted combination.[^1]
- **Quality–diversity trade-off**: over-weighting the conditional component ($w > 0$) gives very high-quality, more typical but slightly stereotypical samples, analogous to the [[Truncation Trick|truncation trick]] in GANs.[^1][^2]
- The condition dropping during training is akin to [[Dropout]].[^2]
- Standard in text-to-image models, where $c$ is a text embedding.

[^1]: [Prince, p. 366](zotero://open-pdf/library/items/BWT7FYX5?page=380&annotation=3N4ZYVFJ); [Prince, p. 367](zotero://open-pdf/library/items/BWT7FYX5?page=381&annotation=ZYEMHQNA)
[^2]: [Prince, p. 371](zotero://open-pdf/library/items/BWT7FYX5?page=385&annotation=MA6WXVUW)
