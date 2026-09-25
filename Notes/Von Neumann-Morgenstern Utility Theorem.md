---
tags:
  - philosophy
  - epistemology
---

# Definition
> [!info] Von Neumann-Morgenstern Utility Theorem (1944)[^1]
> If an agent's preferences $\succeq$ over gambles (lotteries) satisfy the following four constraints, then they can be represented by a [[Utility Function|utility function]] $ such that the agent prefers one gamble to another exactly when it has higher [[Expected Utility|expected utility]]; $ is unique up to a positive affine transformation.
> 1. **Completeness**: for any , b$, the agent prefers $ to $, prefers $ to $, or is indifferent ( \succeq b$ or  \succeq a$).
> 2. **Transitivity**: if  \succ b$ and  \succ c$, then  \succ c$.
> 3. **Continuity**: if  \succ b \succ c$, then there is some gamble between $ and $ with which the agent is indifferent to $, i.e., $\exists p \in (0, 1)$ with  + (1-p)c \sim b$.
> 4. **Independence**: the choice between two options should not be affected by an outcome that is independent of the choice, i.e.,  \succeq b \iff pa + (1-p)c \succeq pb + (1-p)c$ for all $ and  \in (0, 1]$.

# Properties
- Used in the [[Representation Theorem Argument]] for [[Probabilism]].
- Takes the probabilities of the gambles as given and derives only utilities; representation theorems that derive both subjective probabilities (degrees of belief) and utilities from preferences, as the [[Representation Theorem Argument]] requires, are due to Ramsey (1926) and Savage (1954).
- Independence is the most controversial constraint, since the [[Allais Paradox]] shows that actual agents violate it.
- Grounds the [[Utility-Based Agent|utility-based]] view that any [[Rational Agent|rational agent]] behaves as if maximizing expected utility, central to [[Decision Theory]].

[^1]: [A Critical Introduction to Formal Epistemology](zotero://open-pdf/library/items/9XYCZDPF?page=49)
