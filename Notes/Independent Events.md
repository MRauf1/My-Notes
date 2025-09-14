---
tags: statistics
---

# Definition

> [!info] Definition 1 (Marginally Independent Events)
> Events $A, B$ are marginally independent $\iff$
> $$
> \begin{align}
> P(A \cap B) = P(A)P(B)
> \end{align}
> $$
> Otherwise, they are called dependent events.

When the occurrence of one [[Event|event]] does not change the [[Probability|probability]] of the occurrence of the other event.[^1]

> [!info] Definition 2 (Conditionally Independent Events)
> Events $A, B$ are conditionally independent given $C$ if
> $$
> \begin{align}
> P(A \cap B | C) = P(A | C) P(B | C)
> \end{align}
> $$

In general, this does not imply that $A, B$ are marginally independent.

# Properties

- $P(A | B) = P(A)$, $P(B | A) = P(B)$ ([[Conditional Probability]] = [[Marginal Probability]])
- $A, B$ are independent events $\implies$ 
	1) $A, B^c$ are independent
	2) $A^c, B$ are independent
	3) $A^c, B^c$ are independent

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=38)