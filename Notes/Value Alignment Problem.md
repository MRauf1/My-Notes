---
tags:
  - computer_science
  - artificial_intelligence
---

# Definition
> [!info] Value Alignment Problem[^1]
> The problem of achieving agreement between humans' true preferences and the objective given to a machine: the values or objectives built into a machine must be aligned with those of the humans it serves.

# Properties
- Christian frames it as ensuring that models capture our norms and values, understand what we mean or intend, and do what we want; its first succinct expression is Wiener's warning that a machine we cannot interfere with must be given "the purpose which we really desire and not merely a colorful imitation of it" ([[Corrigibility]]).[^2]
- Machine-learning approaches include [[Reward Shaping]], [[Imitation Learning]], [[Inverse Reinforcement Learning]], [[Cooperative Inverse Reinforcement Learning]], and [[Inverse Reward Design]].
- Arises directly from the [[Standard Model of Artificial Intelligence|standard model]]'s assumption that a fully specified objective can be transferred perfectly to a machine.
- If the objective cannot be transferred perfectly, the machine should instead pursue human objectives while remaining uncertain as to what they precisely are; such a machine has an incentive to act cautiously, ask permission, learn preferences through observation, and defer to human control.
- The ultimate goal is agents that are provably beneficial to humans.
- For superintelligent systems, studied as the [[AI Control Problem]] and [[Value-Loading Problem]]; see also the [[Orthogonality Thesis]] and [[Instrumental Convergence Thesis]].
- Concrete machine-learning failures of alignment are studied as [[Accident (Machine Learning)|accidents]], e.g. [[Reward Hacking|reward hacking]] and [[Negative Side Effects (Machine Learning)|negative side effects]].
- Directly relevant to the [[Ethical Concerns of Artificial Intelligence|ethical concerns]] of AI, particularly existential risk.

[^1]: [Russell and Norvig, 2022, p. 23](zotero://open-pdf/library/items/JZXT5DZQ?page=23&annotation=LGNZNUBP)
[^2]: [Christian, 2021, p. 20](zotero://open-pdf/library/items/P27SWKW4?page=20&annotation=RXWREEQ5); [Christian, 2021, p. 293](zotero://open-pdf/library/items/P27SWKW4?page=293&annotation=WQJH8G5T)
