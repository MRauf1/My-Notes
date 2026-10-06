---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Inception Score (IS)[^1][^2]
> An image-[[Generative Model|generative model]] metric computed with a pretrained classifier (usually the Inception network) giving $Pr(y | \mathbf{x})$ over the 1000 ImageNet classes $y$. For generated images $\mathbf{x}_1^*, \dots, \mathbf{x}_I^*$,
> $$
> \begin{align}
> \text{IS} &= \exp\left[\frac{1}{I}\sum_{i=1}^{I} D_{\mathrm{KL}}\left[Pr(y | \mathbf{x}_i^*) \,\|\, Pr(y)\right]\right], \\
> Pr(y) &= \frac{1}{I}\sum_{i=1}^{I} Pr(y | \mathbf{x}_i^*).
> \end{align}
> $$

# Properties
- Encodes two criteria:[^1]
	- Each generated image should look like one and only one class, so $Pr(y | \mathbf{x}_i^*)$ is sharply peaked.
	- The generated set should cover all classes equally, so the marginal $Pr(y)$ is flat.
- The [[Kullback-Leibler Divergence]] between a peaked and a flat distribution is large, so high IS means realistic and class-diverse samples.[^2]
- Equivalently, $\log \text{IS}$ is the [[Mutual Information|mutual information]] between the generated image and its predicted label.
- Only sensible for models of ImageNet-like data, and sensitive to the particular classifier: retraining it can change the numbers substantially.[^2]
- Does not reward within-class diversity: generating one realistic example per class already scores highly. [[Fréchet Inception Distance]] addresses this.

[^1]: [Prince, p. 272](zotero://open-pdf/library/items/BWT7FYX5?page=286&annotation=AW56LXAY)
[^2]: [Prince, p. 273](zotero://open-pdf/library/items/BWT7FYX5?page=287&annotation=YETI5JWV)
