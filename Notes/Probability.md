---
tags:
  - statistics
  - introduction_to_statistics
---

# Definition

For [[Event|event]] $A$, the probability is the [[Real Number|real]]-valued [[Set Function|set function]] that outputs the chance of the event occurring and is denoted by $P(A)$.[^1] 

By definition, probability has the following properties:
- $P(A) \geq 0$
- $P(S) = 1$ for [[Universe of Discourse|outcome space]] $S$
- if $A_1, A_2, \dots, A_n$ are [[Mutually Exclusive Events|mutually exclusive events]], then $P(A_1 \cup A_2 \cup \dots \cup A_n) = P(A_1) + P(A_2) + \dots + P(A_n)$. This can be extended to an [[Infinity|infinite]], but [[Countable Set|countable]] number of events.

> [!info] Definition 2 (Probability Set Function)[^2]
> Let $\mathcal{C}$ be a [[Sample Space]] and $\mathcal{B}$ its [[Sigma-Field]] of events. A real-valued function $P$ on $\mathcal{B}$ is a probability set function if
> 1. $P(A) \geq 0$ for all $A \in \mathcal{B}$,
> 2. $P(\mathcal{C}) = 1$,
> 3. if $\{A_n\}$ is a sequence of events in $\mathcal{B}$ with $A_m \cap A_n = \emptyset$ for all $m \neq n$, then
> $$
> \begin{align}
> P\left(\bigcup_{n=1}^\infty A_n\right) = \sum_{n=1}^\infty P(A_n)
> \end{align}
> $$

The axioms abstract the properties of [[Relative Frequency]]; a probability set function describes how probability is distributed over the events $\mathcal{B}$.

# Types
- [[Conditional Probability]]
- [[Independent Events]]

# Properties
- [[Probability of Complement]]
- [[Probability of Empty Set]]
- [[Probability of Subset]]
- [[Probability Maximum Value]]
- [[Probability of Set Union]]
- [[Probability of Equally Likely Outcomes]]
- [[Continuity Theorem of Probability]]
- [[Boole's Inequality]]
- [[Bonferroni's Inequality]]

# Frameworks
- [[Probability Frequentist Framework]]
- [[Probability Bayesian Framework]]

## Interpretations
- [[Probability Objective Interpretation]]
- [[Probability Subjective Interpretation]]

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=13)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=28)