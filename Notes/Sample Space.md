---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Sample Space[^1]
> For a [[Random Experiment]], the sample space (or experimental space) $\mathcal{C}$ is the [[Set]] of every possible outcome of the experiment. Its elements (outcomes) are usually denoted by lowercase letters $c \in \mathcal{C}$.

The sample space plays the role of the [[Universe of Discourse]] for the experiment: [[Event|events]] are [[Subset|subsets]] of $\mathcal{C}$, and the [[Set Complement|complement]] of an event is taken relative to $\mathcal{C}$.

# Properties
- The collection of events on $\mathcal{C}$ is a [[Sigma-Field]]; together with a [[Probability|probability set function]] it forms a [[Probability Space]].
- A [[Random Variable]] $X: \mathcal{C} \to \mathbb{R}$ induces a new sample space, its range $\mathcal{D} = \{X(c) : c \in \mathcal{C}\}$.
- $\mathcal{C}^c = \emptyset$ and $\emptyset^c = \mathcal{C}$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=17)
