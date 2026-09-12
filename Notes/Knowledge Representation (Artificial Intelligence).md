---
tags:
  - computer_science
  - artificial_intelligence
---

# Definition
> [!info] Representation Schemes[^1]
> A hierarchy of ways to represent the state of the world within an agent, ordered along an axis of increasing expressiveness.

# Types
- Atomic Representation - each state of the world is indivisible, a "black box" whose only discernible property is being identical to or different from another such state; used by search, game-playing, hidden Markov models, and Markov decision processes.
- Factored Representation - each state is split into a fixed set of variables or attributes, each of which can have a value; underlies constraint satisfaction, [[Propositional Logic|propositional logic]], planning, and Bayesian networks.
- Structured Representation - objects and their varying relationships are described explicitly, rather than only variables and values; underlies relational databases, first-order logic, first-order probability models, and natural language understanding.

# Properties
- A more expressive representation can capture, at least as concisely, everything a less expressive one can, plus more — often far more concisely — but reasoning and learning become more complex as expressive power increases.

[^1]: [Russell and Norvig, 2022, p. 77](zotero://open-pdf/library/items/JZXT5DZQ?page=77&annotation=IV6AWR3V)
