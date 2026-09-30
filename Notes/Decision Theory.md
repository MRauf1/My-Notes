---
tags:
  - computer_science
  - artificial_intelligence
---

# Definition
> [!info] Decision Theory[^1]
> The framework that combines probability theory with utility theory to provide a formal and complete account of individual decisions, economic or otherwise, made under uncertainty.

# Types
- [[Markov Decision Process]] - Richard Bellman's formalization of sequential decision problems under uncertainty, foundational to reinforcement learning.

# Properties
- In [[Pattern Recognition|pattern recognition]], determining the joint distribution $p(\mathbf{x}, \mathbf{t})$ from training data is **inference**; decision theory then tells how to make optimal predictions or actions given these probabilities, a stage that is generally simple, even trivial, once inference is solved ([[Three Approaches to Decision Problems]]).[^2]
- Classification decisions: [[Minimum Misclassification Rate Decision Rule]], [[Minimum Expected Loss Decision Rule]], [[Reject Option]]; regression decisions: [[Regression Function]], [[Minkowski Loss]].
- In statistical estimation, a decision rule $\delta(y)$ is judged by its [[Risk Function (Statistics)|risk function]] $R(\theta, \delta) = E\{L[\theta, \delta(Y)]\}$, ordered by the [[Minimax Decision Rule|minimax]] principle or a prior average ([[Bayes Estimator]]).
- Combines a [[Utility Function|utility function]] with probability to define [[Expected Utility|expected utility]], the quantity a rational decision-maker maximizes under uncertainty.

[^1]: [Russell and Norvig, 2022, p. 28](zotero://open-pdf/library/items/JZXT5DZQ?page=28&annotation=QV35B94D)
[^2]: [Bishop, 2006, p. 38](zotero://open-pdf/library/items/5G99AZ8U?page=58&annotation=QMIMQI9U)
