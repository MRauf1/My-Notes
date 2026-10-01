---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Focal Loss[^1]
> A modification of the [[Cross-Entropy Loss]] for class-imbalanced classification (Lin et al., 2017) that adds a single extra parameter $\gamma \geq 0$ to down-weight well-classified examples:
> $$
> \begin{align}
> \mathrm{FL}(p_t) = -(1 - p_t)^{\gamma} \log[p_t]
> \end{align}
> $$
> where $p_t$ is the predicted probability of the true class.[^2]

# Properties
- Motivation: with heavy class imbalance, the standard maximum likelihood loss lets the model concentrate on becoming more confident about well-classified examples from the dominant classes, classifying less-represented classes poorly.
- $\gamma = 0$ recovers the cross-entropy; larger $\gamma$ suppresses the gradients of easy (high-$p_t$) examples.
- An example of deliberately departing from the pure likelihood loss to address a failure mode ([[Maximum Likelihood Loss Optimality and Failure Modes]]).

[^1]: [Prince, Ch. 5](zotero://select/library/items/T3V9WVXD)
[^2]: Supplementary notes provided by the creator.
