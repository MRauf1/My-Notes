---
tags:
  - review
---

# Review[^1]

Potential Problems (see [[Accident (Machine Learning)]]):
1) Wrong [[Objective Function]]
	1) [[Negative Side Effects (Machine Learning)|Negative side effects]]
		- Some aspects are ignored by the objective function, but which can have negative effects.
	2) [[Reward Hacking]]
		- Model finds a sort of a "shortcut" that bypass the designer's intent resulting in incorrect generalization.
2) Valid [[Objective Function]] present, but too expensive, so the designer relies on approximations and on the model's capability to extrapolate on limited samples, which can be dangerous ([[Scalable Oversight]]).
3) Good [[Objective Function]], but either insufficient/poor training data or lack of model expressability
	1) [[Safe Exploration|Safe exploration]]
	2) [[Robustness to Distributional Shift|Robustness to distributional shift]]

[^1]: [Concrete Problems in AI Safety](zotero://open-pdf/library/items/JKJMXPTZ?page=1)
