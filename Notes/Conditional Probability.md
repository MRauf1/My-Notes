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

> [!info] Definition 2 (Conditional Probability using [[Probability Function]])
> Giving [[Random Variable]] $X_1, X_2$ with [[Joint Probability Distribution]] $f(x_1, x_2)$, the conditional probability is
> $$
> \begin{align}
> f_{X_1 | X_2}(x_1 | X_2 = x_2) = \frac{f(x_1, x_2)}{f_{X_2}(x_2)}
> \end{align}
> $$

# Properties

## Primary Properties
- [[Conditional Probability Primary Properties]]

## Multiplication Rule
- [[Conditional Probability Multiplication Rule]]

## Bayes' Theorem
- [[Bayes' Theorem|Bayes' Theorem]]

## Other Properties
- [[Conditional Probability Other Properties]]

#TODO 
- Are the other properties true?
- For the first other property, is the $P(B) > 0$ necessary?
- Double check the last property from my notes

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=30)