---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Algorithmic Bias[^1]
> Systematic, unfair behaviour of a machine-learning system toward some group, arising most often directly from the data on which it was trained: a system that can learn almost anything from examples is at the mercy of those examples, so types of data underrepresented in training but present in the world lead to unreliable behaviour.

# Properties
- Every machine-learning system has a "Shirley card" at its heart (after the Kodak colour-calibration cards that encoded bias inside the camera itself): its training data. The more we take such artefacts for granted, the more they govern our lives.[^1]
- Computer systems are cheap to disseminate, so a biased system that becomes a standard makes its bias pervasive (Friedman and Nissenbaum). It is thus crucial to know who is represented in a dataset, and to what degree, before training systems that affect real people.[^2]
- Machine-learning systems are designed precisely to infer hidden correlations, so they not only exhibit bias but may silently perpetuate and amplify it, e.g. gender stereotypes in [[Word Embedding|word embeddings]].[^3]
- Debiasing is hard: removing explicit links (e.g. "nurse"-"she") while leaving implicit ones (e.g. "nurse"-"receptionist") may be only "lipstick on a pig", arguably worse because it removes the most visible, measurable associations. Still, ML should at least not amplify societal bias.[^4]
- Because the model's biases are our own, embeddings act as a diagnostic mirror of society, a new instrument for social science that can quantify, and track over time, cultural associations; ML artefacts themselves become objects of sociological study.[^5]
- Removing a protected attribute does not remove bias, due to [[Redundant Encoding|redundant encodings]]; and common fairness criteria cannot all be satisfied at once ([[Fairness Impossibility Theorem]]).
- Errors are not equally costly: some misclassifications are thousands or millions of times worse than others, which uniform loss functions ignore.[^6]
- Deployed models also change the world they model ([[Feedback Loop (Machine Learning)]]).
- A central concern of [[Ethical Concerns of Artificial Intelligence]] and of the broader [[Value Alignment Problem]].

[^1]: [Christian, 2021, p. 32](zotero://open-pdf/library/items/P27SWKW4?page=32&annotation=6V85Q3KD); [Christian, 2021, p. 32](zotero://open-pdf/library/items/P27SWKW4?page=32&annotation=U7C2DTPW); [Christian, 2021, p. 33](zotero://open-pdf/library/items/P27SWKW4?page=33&annotation=QMSU3TQI); [Christian, 2021, p. 35](zotero://open-pdf/library/items/P27SWKW4?page=35&annotation=M9GWB7MG)
[^2]: [Christian, 2021, p. 36](zotero://open-pdf/library/items/P27SWKW4?page=36&annotation=MU8N53MC); [Christian, 2021, p. 39](zotero://open-pdf/library/items/P27SWKW4?page=39&annotation=SHTC9EAK)
[^3]: [Christian, 2021, p. 44](zotero://open-pdf/library/items/P27SWKW4?page=44&annotation=K7HW6MKD); [Christian, 2021, p. 44](zotero://open-pdf/library/items/P27SWKW4?page=44&annotation=2QZFZ7L2); [Christian, 2021, p. 45](zotero://open-pdf/library/items/P27SWKW4?page=45&annotation=SKGHXK8K)
[^4]: [Christian, 2021, p. 49](zotero://open-pdf/library/items/P27SWKW4?page=49&annotation=4S2TBJT2); [Christian, 2021, p. 49](zotero://open-pdf/library/items/P27SWKW4?page=49&annotation=BSVMNUC3)
[^5]: [Christian, 2021, p. 51](zotero://open-pdf/library/items/P27SWKW4?page=51&annotation=PUXD59J9); [Christian, 2021, p. 51](zotero://open-pdf/library/items/P27SWKW4?page=51&annotation=JMPQNMHT); [Christian, 2021, p. 52](zotero://open-pdf/library/items/P27SWKW4?page=52&annotation=CGPWEK84); [Christian, 2021, p. 53](zotero://open-pdf/library/items/P27SWKW4?page=53&annotation=LGWR4662)
[^6]: [Christian, 2021, p. 314](zotero://open-pdf/library/items/P27SWKW4?page=314&annotation=CX8AJ6PN)
