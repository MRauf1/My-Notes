---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Safe Exploration[^1]
> The problem of ensuring that exploratory actions taken by a [[Reinforcement Learning|reinforcement learning]] agent do not lead to negative or irrecoverable consequences that outweigh the long-term value of exploration.

# Properties
- A type of [[Accident (Machine Learning)|accident]] where the objective is correct but harm arises during learning.
- Unlike in simulation, the real world is unforgiving: badly chosen actions may destroy the agent or trap it in states it cannot escape. Yet it should often be possible to predict which actions are dangerous and explore while avoiding them, even with little information about the environment.[^2]
- In practice real-world RL often hard-codes avoidance of catastrophic behaviours; this works when there are few failure modes all known in advance, but becomes infeasible as agents grow more autonomous and act in more complex domains.[^3]
- Approaches:[^4]
	- *Risk-sensitive performance criteria*: optimise worst-case or risk-adjusted performance rather than expected return, e.g. under a [[Markov Decision Process|MDP]] with uncertainty or constraints.
	- *Use demonstrations*: use expert demonstrations (imitation/inverse RL) to learn a baseline policy, reducing the need for exploration.
	- *Simulated exploration*: do as much exploration as possible in simulation, where catastrophe is harmless.
	- *Bounded exploration*: restrict exploration to a portion of state space known to be safe or recoverable.
	- *Trusted policy oversight*: given a trusted policy and a model of the environment, only explore actions from which the trusted policy can recover.
	- *Human oversight*: have a human check potentially unsafe actions, which runs into the problem of [[Scalable Oversight]].
- Refines the exploration side of the exploration-exploitation tradeoff in [[Reinforcement Learning]].

[^1]: [Amodei et al., 2016, p. 3](zotero://open-pdf/library/items/JKJMXPTZ?page=3&annotation=W97US924); [Amodei et al., 2016, p. 3](zotero://open-pdf/library/items/JKJMXPTZ?page=3&annotation=DIK55Z2X)
[^2]: [Amodei et al., 2016, p. 14](zotero://open-pdf/library/items/JKJMXPTZ?page=14&annotation=2FLNGZYY); [Amodei et al., 2016, p. 14](zotero://open-pdf/library/items/JKJMXPTZ?page=14&annotation=5B3AW2UJ)
[^3]: [Amodei et al., 2016, p. 14](zotero://open-pdf/library/items/JKJMXPTZ?page=14&annotation=SBMAUXJ9); [Amodei et al., 2016, p. 14](zotero://open-pdf/library/items/JKJMXPTZ?page=14&annotation=MI35MJNR)
[^4]: [Amodei et al., 2016, p. 14](zotero://open-pdf/library/items/JKJMXPTZ?page=14&annotation=NUX8CS4M); [Amodei et al., 2016, p. 14](zotero://open-pdf/library/items/JKJMXPTZ?page=14&annotation=7BAVANS6); [Amodei et al., 2016, p. 15](zotero://open-pdf/library/items/JKJMXPTZ?page=15&annotation=VG6EY2EA); [Amodei et al., 2016, p. 15](zotero://open-pdf/library/items/JKJMXPTZ?page=15&annotation=UXFPIBW6); [Amodei et al., 2016, p. 15](zotero://open-pdf/library/items/JKJMXPTZ?page=15&annotation=YWS8KLJI); [Amodei et al., 2016, p. 15](zotero://open-pdf/library/items/JKJMXPTZ?page=15&annotation=CQSFANHL)
