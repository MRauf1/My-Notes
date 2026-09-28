---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Negative Side Effects[^1]
> An [[Accident (Machine Learning)|accident]] in which the designer specifies an [[Objective Function|objective function]] focused on accomplishing a specific task in the environment, but which ignores other aspects of the (potentially very large) environment, thereby implicitly expressing indifference over environmental variables that may actually be harmful to change.

# Properties
- An agent optimising such an objective may engage in major disruptions of the broader environment if doing so gives even a tiny advantage on the task at hand.[^2]
- It is generally infeasible to identify and explicitly penalise every possible disruption.[^2]
- Side effects are conceptually similar across very diverse tasks (e.g. knocking over furniture is bad for most tasks), so the problem is worth attacking in generality; a successful approach might transfer across tasks and counteract one general mechanism that produces wrong objective functions.[^3]
- Approaches:[^3]
	- *Define an impact regulariser*: add a [[Regularization|regularisation]] penalty on "change to the environment", e.g. distance between the resulting state and that under some null/baseline policy.
	- *Learn an impact regulariser*: learn a generalisable side-effect penalty across many tasks via transfer learning, separately from the task reward.
	- *Penalise influence*: discourage the agent from getting into positions where it *could* cause side effects, e.g. by penalising empowerment (the mutual information between the agent's actions and future states).
	- *Multi-agent approaches*: make the agent understand and avoid affecting other agents' (including humans') interests, e.g. via cooperative inverse reinforcement learning or reward autoencoders.
	- *Reward uncertainty*: have the agent be uncertain about its [[Reward Function|reward function]], with a prior that makes random changes to the environment more likely to be bad than good.
- The ideal outcome is to prevent, or at least bound, the incidental harm an agent can do; such approaches are not a replacement for extensive testing and careful per-system design, but may counteract a general tendency for harmful side effects to proliferate in complex environments.[^4]

[^1]: [Amodei et al., 2016, p. 2](zotero://open-pdf/library/items/JKJMXPTZ?page=2&annotation=YVHFFCBY)
[^2]: [Amodei et al., 2016, p. 4](zotero://open-pdf/library/items/JKJMXPTZ?page=4&annotation=M35IJY2A); [Amodei et al., 2016, p. 4](zotero://open-pdf/library/items/JKJMXPTZ?page=4&annotation=2LSJCA6W); [Amodei et al., 2016, p. 4](zotero://open-pdf/library/items/JKJMXPTZ?page=4&annotation=PXBP2GVR)
[^3]: [Amodei et al., 2016, p. 5](zotero://open-pdf/library/items/JKJMXPTZ?page=5&annotation=T3WRUKYD); [Amodei et al., 2016, p. 5](zotero://open-pdf/library/items/JKJMXPTZ?page=5&annotation=7ZKF2JCF); [Amodei et al., 2016, p. 5](zotero://open-pdf/library/items/JKJMXPTZ?page=5&annotation=YDLHVTF5); [Amodei et al., 2016, p. 5](zotero://open-pdf/library/items/JKJMXPTZ?page=5&annotation=FP8AR7HP); [Amodei et al., 2016, p. 6](zotero://open-pdf/library/items/JKJMXPTZ?page=6&annotation=4M6NNSDW); [Amodei et al., 2016, p. 6](zotero://open-pdf/library/items/JKJMXPTZ?page=6&annotation=7LBZ63TI)
[^4]: [Amodei et al., 2016, p. 7](zotero://open-pdf/library/items/JKJMXPTZ?page=7&annotation=RM9ITS5J)
