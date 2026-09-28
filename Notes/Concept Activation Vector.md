---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Concept Activation Vector[^1]
> In *testing with concept activation vectors* (TCAV, Been Kim et al.), a direction in a network layer's activation space representing a human concept, obtained by training a linear classifier to separate that layer's activations on examples of the concept (e.g. images of men) from activations on random examples; one then measures how much this direction contributes to a given prediction (e.g. "doctor").

# Properties
- Motivated by the view that humans think and communicate in concepts, not numbers, so pixel-level [[Saliency Map|saliency]] does not go far enough.[^2]
- Explanations "speak the users' language": users can test their own hypotheses in their own terms without learning ML.[^3]
- A technique of [[Interpretability (Machine Learning)]], useful for probing [[Algorithmic Bias]].

[^1]: [Christian, 2021, p. 119](zotero://open-pdf/library/items/P27SWKW4?page=119&annotation=LEH42VXK); [Christian, 2021, p. 120](zotero://open-pdf/library/items/P27SWKW4?page=120&annotation=RVBP2EN9)
[^2]: [Christian, 2021, p. 119](zotero://open-pdf/library/items/P27SWKW4?page=119&annotation=XHYKIKQ8)
[^3]: [Christian, 2021, p. 120](zotero://open-pdf/library/items/P27SWKW4?page=120&annotation=4JCKQNML)
