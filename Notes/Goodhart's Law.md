---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Goodhart's Law[^1]
> When a metric is used as a target, it ceases to be a good metric.

# Properties
- Originates in the economics literature (Charles Goodhart).
- In machine learning, a proxy objective that correlates with the designer's intent under normal conditions loses that correlation once it is strongly optimised, making it one of the causes of [[Reward Hacking]].
- Implies that any [[Objective Function|objective function]] that is only a proxy for true intent becomes less trustworthy the harder it is optimised.

[^1]: [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=PRHN6WSQ); [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=UZFNLYTW)
