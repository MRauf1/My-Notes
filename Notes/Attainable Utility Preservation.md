---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Attainable Utility Preservation[^1]
> (Turner et al.) An impact-regularisation approach in which an agent, while maximising its task reward, is penalised for changing its ability to achieve a set of auxiliary goals, so that it preserves its future capacity to pursue them. With auxiliary action-value functions $Q_1, \dots, Q_N$ and a no-op action $\varnothing$:
> $$\begin{align}
> R_{\text{AUP}}(s,a) = R(s,a) - \frac{\lambda}{N} \sum_{i=1}^{N} \left| Q_i(s,a) - Q_i(s,\varnothing) \right|
> \end{align}$$

# Properties
- Fosters good behaviour in DeepMind's AI safety gridworlds even when the auxiliary goals are generated at random, e.g. the agent pushes a block to a reversible position before heading to the goal.[^2]
- An approach to [[Negative Side Effects (Machine Learning)|negative side effects]] and to preserving reversibility, cf. [[Safe Exploration]].

[^1]: [Christian, 2021, p. 292](zotero://open-pdf/library/items/P27SWKW4?page=292&annotation=K37VH6GD)
[^2]: [Christian, 2021, p. 292](zotero://open-pdf/library/items/P27SWKW4?page=292&annotation=K37VH6GD); [Christian, 2021, p. 292](zotero://open-pdf/library/items/P27SWKW4?page=292&annotation=X7GHAALQ)
