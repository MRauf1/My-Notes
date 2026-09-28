---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Imitation Learning[^1]
> Learning a behaviour by observing and reproducing the demonstrations of an expert, rather than from explicit reward or rules.

# Properties
- Advantages:[^1]
	- *Efficiency* - the fruits of another's trial and error are handed over, including the knowledge that the task is possible at all.
	- *Safety* - avoids learning through countless failures where failure is costly (surgeons, pilots).
	- *Conveying the hard-to-describe* - "five minutes' demonstration is worth more than five hours' talking"; true both of actions and of goals that cannot be fully articulated.
- **Cascading errors**: a learner trained only on expert trajectories never sees how to recover from its own mistakes (e.g. ALVINN never saw off-centre driving), so small errors compound. Demonstrating swerves is time-consuming and dangerous; ALVINN instead used synthetically skewed images labelled with corrective steering, a hack that breaks down with modern high-resolution sensors.[^2]
- **Interaction (DAgger)**: the fix is for the learner to return to the expert with its own mistakes: the expert labels the states the learner actually visits (or expert and learner randomly share control, with the learner's share increasing). Dataset Aggregation worked orders of magnitude better than static demonstrations, which failed to improve even with a million frames.[^3]
- Further limitations: one may be unable to do what the expert does, making imitation a start one cannot finish; and pure imitation makes surpassing the teacher hard, unless (as in AlphaGo Zero) the system imitates *itself*.[^4]
- Values are hard to state outright ("It seems completely impossible to write down a list of everything we care about"), so "watch and learn" may extend to living well; but both RL and imitation require humans as ultimate authorities, and imitators surpass teachers only if errors cancel out or experts can at least recognise what they want ([[Inverse Reinforcement Learning]]).[^5]
- Human imitation is a sophisticated foundation of development ([[Overimitation]]).

[^1]: [Christian, 2021, p. 220](zotero://open-pdf/library/items/P27SWKW4?page=220&annotation=DMPVCJE3); [Christian, 2021, p. 221](zotero://open-pdf/library/items/P27SWKW4?page=221&annotation=TZXJ7UHN); [Christian, 2021, p. 222](zotero://open-pdf/library/items/P27SWKW4?page=222&annotation=R9MXBJTW); [Christian, 2021, p. 222](zotero://open-pdf/library/items/P27SWKW4?page=222&annotation=KZ3U74ZD)
[^2]: [Christian, 2021, p. 228](zotero://open-pdf/library/items/P27SWKW4?page=228&annotation=IDIUE5FR); [Christian, 2021, p. 229](zotero://open-pdf/library/items/P27SWKW4?page=229&annotation=9AG6P4B5); [Christian, 2021, p. 229](zotero://open-pdf/library/items/P27SWKW4?page=229&annotation=K2Z9QDUM); [Christian, 2021, p. 229](zotero://open-pdf/library/items/P27SWKW4?page=229&annotation=FAR7YS5T); [Christian, 2021, p. 229](zotero://open-pdf/library/items/P27SWKW4?page=229&annotation=YD27K6EC)
[^3]: [Christian, 2021, p. 230](zotero://open-pdf/library/items/P27SWKW4?page=230&annotation=CVAZK3NS); [Christian, 2021, p. 230](zotero://open-pdf/library/items/P27SWKW4?page=230&annotation=HEUHUNA4); [Christian, 2021, p. 231](zotero://open-pdf/library/items/P27SWKW4?page=231&annotation=32L8NB2E); [Christian, 2021, p. 231](zotero://open-pdf/library/items/P27SWKW4?page=231&annotation=NQ73DSBH)
[^4]: [Christian, 2021, p. 234](zotero://open-pdf/library/items/P27SWKW4?page=234&annotation=D7W9T6NR); [Christian, 2021, p. 239](zotero://open-pdf/library/items/P27SWKW4?page=239&annotation=VJLU9DTK); [Christian, 2021, p. 243](zotero://open-pdf/library/items/P27SWKW4?page=243&annotation=BC94VWPK)
[^5]: [Christian, 2021, p. 245](zotero://open-pdf/library/items/P27SWKW4?page=245&annotation=27HWTDMF); [Christian, 2021, p. 246](zotero://open-pdf/library/items/P27SWKW4?page=246&annotation=MGXFX9YB); [Christian, 2021, p. 246](zotero://open-pdf/library/items/P27SWKW4?page=246&annotation=2MUQK2CQ)
