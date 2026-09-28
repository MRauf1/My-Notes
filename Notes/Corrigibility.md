---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Corrigibility[^1]
> The property of an AI system that allows humans to intervene in, correct, or shut it down: the flip side of Wiener's warning that if we use "a mechanical agency with whose operation we cannot efficiently interfere once we have started it", we had better be sure its purpose is the one we really desire. If we cannot be sure our objectives are perfectly specified, we must be sure we can intervene.

# Properties
- Much harder than it seems, since a goal-directed agent typically has incentives to resist interruption ([[Instrumental Convergence Thesis]]).[^1]
- Uncertainty rather than incentives may be the answer: a system should "reason as if it is incomplete and potentially flawed in dangerous ways"; Russell argues the machine must be initially uncertain about what humans want ([[Cooperative Inverse Reinforcement Learning]]).[^2]
- Two problems with uncertainty-based corrigibility (the off-switch game):[^3]
	- Each intervention reduces the system's uncertainty; if it reaches zero, the system loses any incentive to defer. Hence one should think hard before giving a robot a deterministic reward function or letting it become fully convinced of its objective.
	- The system must assume the human is always right; if it believes humans err, it will eventually conclude it knows better and ignore protests.
- Sometimes humans truly are wrong about what they want, so even the human might want the system to be "disobedient". Models of human values should err toward complexity: overparameterised value models learn the truth more slowly, whereas underparameterised ones quickly become confidently disobedient.[^4]
- Staying uncertain even under an explicit reward function motivates [[Inverse Reward Design]].
- A central component of the [[AI Control Problem]] and [[Value Alignment Problem]].

[^1]: [Christian, 2021, p. 293](zotero://open-pdf/library/items/P27SWKW4?page=293&annotation=WQJH8G5T); [Christian, 2021, p. 293](zotero://open-pdf/library/items/P27SWKW4?page=293&annotation=CC4U6G39)
[^2]: [Christian, 2021, p. 294](zotero://open-pdf/library/items/P27SWKW4?page=294&annotation=VVTAXRZD); [Christian, 2021, p. 295](zotero://open-pdf/library/items/P27SWKW4?page=295&annotation=HQMEI3ZL); [Christian, 2021, p. 295](zotero://open-pdf/library/items/P27SWKW4?page=295&annotation=W6CCSRNU)
[^3]: [Christian, 2021, p. 295](zotero://open-pdf/library/items/P27SWKW4?page=295&annotation=DG5CDDM7); [Christian, 2021, p. 295](zotero://open-pdf/library/items/P27SWKW4?page=295&annotation=I8PVW6AU); [Christian, 2021, p. 296](zotero://open-pdf/library/items/P27SWKW4?page=296&annotation=VZS68YNR)
[^4]: [Christian, 2021, p. 296](zotero://open-pdf/library/items/P27SWKW4?page=296&annotation=7E2QZAP6); [Christian, 2021, p. 297](zotero://open-pdf/library/items/P27SWKW4?page=297&annotation=XKLNKRCY)
