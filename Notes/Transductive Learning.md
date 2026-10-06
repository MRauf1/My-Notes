---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Transductive Learning[^1]
> A learning setting in which the model considers the labelled and the unlabelled data at the same time and produces a labelling of the specific unlabelled examples, rather than a general rule. It contrasts with **inductive learning**, which learns a rule mapping inputs to outputs from a labelled training set and then applies it to new test data.

# Properties
- Sometimes termed [[Semi-Supervised Learning]].[^2]
- **Advantage**: it can exploit patterns in the unlabelled data to make its decisions.[^2]
- **Disadvantage**: the model must be retrained when extra unlabelled data are added.[^2]
- **On graphs**: in the inductive setting, a [[Graph Neural Network]] is trained on a set of labelled graphs and must label every node of a new test graph. In the transductive setting, there is one large graph in which some nodes are labelled; the model is trained to predict the known labels and then read off at the unknown nodes, whose features and connections were present during training.[^3]
- Vapnik's motivation: when only specific test points matter, solve that problem directly rather than the harder general problem of learning a function.[^4]

[^1]: [Prince, p. 252](zotero://open-pdf/library/items/BWT7FYX5?page=266&annotation=WF66MNLC); [Prince, p. 253](zotero://open-pdf/library/items/BWT7FYX5?page=267&annotation=8TECXLA4)
[^2]: [Prince, p. 253](zotero://open-pdf/library/items/BWT7FYX5?page=267&annotation=8TECXLA4)
[^3]: [Prince, p. 252](zotero://open-pdf/library/items/BWT7FYX5?page=266&annotation=JCBIF9WW)
[^4]: Added from general knowledge.
