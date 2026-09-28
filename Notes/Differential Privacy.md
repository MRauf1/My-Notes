---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Differential Privacy[^1]
> A principle, developed by Cynthia Dwork and colleagues, enabling the collection and analysis of data about a population while preserving the privacy of individuals. Formally, a randomised mechanism $\mathcal{M}$ is $\varepsilon$-differentially private if for all datasets $D, D'$ differing in one individual and all measurable sets of outputs $S$:
> $$\begin{align}
> \Pr[\mathcal{M}(D) \in S] \le e^{\varepsilon} \Pr[\mathcal{M}(D') \in S]
> \end{align}$$

# Properties
- Smaller $\varepsilon$ gives stronger privacy: the output distribution barely depends on any single individual's data.
- Dwork's hunch was that demands for privacy are often really worries about data being *used* harmfully; over time the public discussion shifted from privacy to fairness, and many privacy problems came to look like fairness problems ([[Algorithmic Bias]]).[^2]

[^1]: [Christian, 2021, p. 66](zotero://open-pdf/library/items/P27SWKW4?page=66&annotation=VTKPYIPG); [Christian, 2021, p. 67](zotero://open-pdf/library/items/P27SWKW4?page=67&annotation=CCQYRAME)
[^2]: [Christian, 2021, p. 68](zotero://open-pdf/library/items/P27SWKW4?page=68&annotation=2QQJ4ILN)
