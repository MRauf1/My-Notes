---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

[[Set]] containing [[Set]]. Also called a family of sets.[^1]

> [!info] Definition 1 (Intersection and Union of a Family)[^2]
> For a family of sets $\mathcal F$,
> $$
> \begin{align}
> \bigcap \mathcal F &= \{x \mid \forall A \in \mathcal F\,(x \in A)\} = \{x \mid \forall A\,(A \in \mathcal F \to x \in A)\} \\
> \bigcup \mathcal F &= \{x \mid \exists A \in \mathcal F\,(x \in A)\} = \{x \mid \exists A\,(A \in \mathcal F \land x \in A)\}
> \end{align}
> $$

# Types
- [[Indexed Family of Sets]]: $\mathcal F = \{A_i \mid i \in I\}$, with $\bigcup_{i \in I} A_i = \bigcup \mathcal F$ and $\bigcap_{i \in I} A_i = \bigcap \mathcal F$.
- [[Power Set]]: $\mathcal P(A)$ is a family of sets.

# Properties
- For $\mathcal F = \{A, B\}$: $\bigcap \mathcal F = A \cap B$ and $\bigcup \mathcal F = A \cup B$ ([[Set Intersection]], [[Set Union]]).
- $\bigcap$ and $\bigcup$ correspond to the [[Universal Quantifier]] and [[Existential Quantifier]], so the [[Quantifier Negation Laws]] give the generalized [[DeMorgan's Laws]]: $A \setminus \bigcup \mathcal F = \bigcap\{A \setminus B \mid B \in \mathcal F\}$.
- $\bigcap \varnothing$ would be every object, so $\bigcap \mathcal F$ is only used for $\mathcal F \neq \varnothing$ (or inside a fixed universe); $\bigcup \varnothing = \varnothing$.
- Identities such as $(\bigcap \mathcal F) \cap (\bigcap \mathcal G) = \bigcap(\mathcal F \cup \mathcal G)$ follow from the [[Quantifier Distributive Laws]].

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=89)
[^2]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=91)
