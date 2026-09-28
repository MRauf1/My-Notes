---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Redundant Encoding[^1]
> The phenomenon whereby a protected attribute (e.g. race or gender) is encoded implicitly in other features correlated with it, so that removing the attribute from a model's inputs does little to prevent the model from effectively using it.

# Properties
- Consequently "fairness through blindness" does not work, described as the most established and robust fact in algorithmic fairness research.[^2]
- Blindness can even make matters worse: without the protected attribute one cannot measure how strongly other variables correlate with it, and hence cannot detect or correct the bias.[^1]
- A mechanism of [[Algorithmic Bias]].

[^1]: [Christian, 2021, p. 69](zotero://open-pdf/library/items/P27SWKW4?page=69&annotation=R9BMNT9U); [Christian, 2021, p. 69](zotero://open-pdf/library/items/P27SWKW4?page=69&annotation=CSD3QFGK); [Christian, 2021, p. 69](zotero://open-pdf/library/items/P27SWKW4?page=69&annotation=7LTYJADM)
[^2]: [Christian, 2021, p. 70](zotero://open-pdf/library/items/P27SWKW4?page=70&annotation=JXQ5GSVY)
