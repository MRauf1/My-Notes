---
tags: statistics
---

# Definition

> [!info] Definition 1 (Conditional Probability)
> For [[Event|events]] $A, B$, the conditional [[Probability|probability]] of event $A$ occurring given event $B$ occurred is[^1]
> $$
> \begin{align}
> P(A | B) = \frac{P(A \cap B)}{P(B)}
> \end{align}
> $$
> given $P(B) > 0$

With conditional probability, our sample space changes from the [[Universe of Discourse|universe of discourse]] to the space of event $B \subseteq U$.

# Properties

## Primary Properties

- $P(A | B) \geq 0$
- $P(B | B) = 1$
- if $A_1, A_2, \dots, A_n$ are [[Mutually Exclusive Events|mutually exclusive events]], then $P(A_1 \cup A_2 \cup \dots \cup A_n | B) = P(A_1 | B) + P(A_2 | B) + \dots + P(A_n | B)$. This can be extended to an [[Infinity|infinite]], but [[Countably Infinite|countable]] number of events.

## Multiplication Rule

- $P(A \cap B) = P(A) P(B | A) = P(B) P(A | B)$, where $P(A) > 0$ in the first case and $P(B) > 0$ in the second case

## Bayes' Theorem

- [[Bayes' Theorem|Bayes' Theorem]]

## Other Properties

- $P(A | B) = 1 - P(A^c | B)$, given $P(B) > 0$
- $P(\emptyset | B) = 0$
- $A_1 \subseteq A_2 \implies P(A_1 | B) \leq P(A_2 | B)$
- $P(A | B) \leq 1$
- $P(A_1 \cup A_2 | B) = P(A_1 | B) + P(A_2 | B) - P(A_1 \cap A_2 | B)$

#TODO 
- Are the other properties true?
- For the first other property, is the $P(B) > 0$ necessary?

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=30)