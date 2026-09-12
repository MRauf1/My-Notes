---
tags:
  - computer_science
  - artificial_intelligence
---

# Definition
> [!info] Observability[^1]
> A dimension of a [[Task Environment|task environment]] describing how much of the environment's state an agent's sensors give it access to at each point in time.

# Types
- Fully Observable - the agent's sensors detect the complete state of the environment (or at least all aspects relevant to the choice of action) at each point in time.
- Partially Observable - the environment's state is only incompletely revealed to the agent's sensors, e.g. due to noisy sensors or missing state information.
- Unobservable - the agent has no sensors at all; its goals may still sometimes be achievable, even with certainty.

# Properties
- Fully observable environments are convenient because the agent need not maintain any internal state to keep track of the world.
- Distinct from whether the environment is [[Known vs Unknown Environment|known or unknown]]: a known environment can be partially observable, and an unknown environment can be fully observable.

[^1]: [Russell and Norvig, 2022, p. 61](zotero://open-pdf/library/items/JZXT5DZQ?page=61&annotation=WTWGLG24)
