---
tags:
  - statistics
  - introduction_to_statistics
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

The ratio form is forced by two requirements:[^2] relative to the new [[Sample Space]] $B$, only $A \cap B$ matters and $B$ is certain, so $P(A | B) = P(A \cap B | B)$ and $P(B | B) = 1$; and the ratio of the probabilities of $A \cap B$ and $B$ should be the same relative to $B$ as relative to $\mathcal{C}$, i.e. $\frac{P(A \cap B | B)}{P(B | B)} = \frac{P(A \cap B)}{P(B)}$. At this level the conditional probability is defined only when $P(B) > 0$.

> [!info] Definition 2 (Conditional Probability using [[Probability Function]])
> Giving [[Random Variable]] $X_1, X_2$ with [[Joint Probability Distribution]] $f(x_1, x_2)$, the conditional probability is
> $$
> \begin{align}
> f_{X_1 | X_2}(x_1 | X_2 = x_2) = \frac{f(x_1, x_2)}{f_{X_2}(x_2)}
> \end{align}
> $$

# Properties
- [[Conditional Probability Primary Properties]]
- [[Conditional Probability Multiplication Rule]]
- [[Law of Total Probability]]
- [[Bayes' Theorem|Bayes' Theorem]]
- [[Conditional Probability Other Properties]]

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=30)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=39)