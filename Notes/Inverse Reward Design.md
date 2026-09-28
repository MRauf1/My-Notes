---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Inverse Reward Design[^1]
> (Hadfield-Menell et al.) An approach in which an agent treats the designer's explicit reward function not as the true objective but as (mere) evidence about what the designer wants, given that the designer made a best-faith but imperfect attempt. Whereas [[Inverse Reinforcement Learning|IRL]] asks "what do you want, based on what you do?", IRD asks "what do you want, based on what you told me to do?"

# Properties
- "Even the score is not the score": autonomous agents optimise the reward they are given, but do not know how hard it is to design one that captures what we want.[^2]
- Keeps the agent uncertain even when given a deterministic reward function, supporting [[Corrigibility]].[^3]
- Guards against [[Reward Hacking]] and [[Negative Side Effects (Machine Learning)|negative side effects]] in situations the designer did not anticipate.

[^1]: [Christian, 2021, p. 299](zotero://open-pdf/library/items/P27SWKW4?page=299&annotation=8TVSAE6H)
[^2]: [Christian, 2021, p. 298](zotero://open-pdf/library/items/P27SWKW4?page=298&annotation=EKITDCZN); [Christian, 2021, p. 299](zotero://open-pdf/library/items/P27SWKW4?page=299&annotation=B8H9ECWD)
[^3]: [Christian, 2021, p. 298](zotero://open-pdf/library/items/P27SWKW4?page=298&annotation=Q8NSCM9W)
