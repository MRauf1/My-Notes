---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Manifold Precision and Recall[^1]
> Metrics separating realism from diversity of a [[Generative Model|generative model]] via the overlap of the *data manifold* $\mathcal{M}_r$ (where real examples lie) and the *model manifold* $\mathcal{M}_g$ (where generated samples lie). For real examples $\{\mathbf{x}_i\}$ and generated samples $\{\mathbf{x}_j^*\}$,
> $$
> \begin{align}
> \text{precision} &= \frac{1}{|\{\mathbf{x}_j^*\}|}\sum_j \mathbb{1}\left[\mathbf{x}_j^* \in \mathcal{M}_r\right], \\
> \text{recall} &= \frac{1}{|\{\mathbf{x}_i\}|}\sum_i \mathbb{1}\left[\mathbf{x}_i \in \mathcal{M}_g\right].
> \end{align}
> $$

# Properties
- **Precision** is the fraction of generated samples that are realistic; **recall** is the fraction of real data the model can generate (coverage).[^1]
- **Manifold estimate**: place a hypersphere around each example with radius equal to the distance to its $k$-th nearest neighbor ([[K Nearest Neighbor Classifier]]); the union of the hyperspheres approximates the manifold, and membership of a new point is easy to test:
$$
\begin{align}
\mathcal{M} \approx \bigcup_{i} B\left(\mathbf{x}_i, \|\mathbf{x}_i - \mathrm{NN}_k(\mathbf{x}_i)\|\right)
\end{align}
$$
- Typically computed in the feature space of a classifier, inheriting the advantages and disadvantages of the [[Fréchet Inception Distance]].
- Motivated by FID conflating realism and diversity into one number.
- Analogous to classification precision/recall: generated samples play the role of predictions and the data manifold the role of ground truth.

[^1]: [Prince, p. 274](zotero://open-pdf/library/items/BWT7FYX5?page=288&annotation=BIPZK5JQ)
