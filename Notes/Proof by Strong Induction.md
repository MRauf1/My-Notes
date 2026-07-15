---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 ([[Proof by Induction|Proof by Strong Induction]])[^1]
> To prove a goal of form $\forall n \in \mathbb{N}, P(n)$
> 1) Base Case: Prove $P(0)$
> 2) Induction Step: Prove $\forall n \in \mathbb{N}, (\forall k < n, P(k)) \implies P(n + 1)$
> Assuming $\forall k < n, P(k)$ is true is called the Inductive Hypothesis
> Technically, a base case is not needed for strong induction

A natural number has the property based on the assumption that all the previous natural numbers have the property.

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=303)