---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Policy Network[^1]
> A [[Deep Neural Network|deep network]] that represents a [[Policy]] in [[Reinforcement Learning]], mapping the observed world state to an action.

# Properties
- Trained so that the agent chooses actions that lead to high rewards on average, subject to the [[Temporal Credit Assignment Problem]] and the [[Exploration-Exploitation Tradeoff]].
- Its output may be a single action ([[Deterministic Policy]]) or a distribution over actions ([[Stochastic Policy]]).

[^1]: [Prince, p. 12](zotero://open-pdf/library/items/BWT7FYX5?page=26&annotation=WV6IEQS9)
