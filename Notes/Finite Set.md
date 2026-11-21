---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Finite Set)[^1][^2]
> For $n \in \mathbb{N}$ let $I_n = \{i \in \mathbb{Z}^+ : i \leq n\} = \{1, \dots, n\}$, with $I_0 = \varnothing$. A [[Set|set]] $A$ is finite if there is an $n \in \mathbb{N}$ such that $I_n \sim A$, i.e. there is a [[Bijective Function|bijection]] $I_n \to A$. Otherwise $A$ is an [[Infinite Set|infinite set]].

Counting the elements of $A$ is exactly building a bijection between $\{1, 2, \dots, n\}$ and $A$; the sets $I_n$ are the reference sets against which the sizes of finite sets are measured.[^1]

# Properties

> [!abstract] Theorem 1 (Finite Sets Are Not Equinumerous With a Proper Subset)[^3]
> If $A$ is finite and $B \subsetneq A$ is a [[Proper Subset|proper subset]], then $A \not\sim B$.

- The $n$ with $I_n \sim A$ is unique, so the number of elements $|A| = n$ is well defined ([[Set Cardinality]]).[^1]
- Theorem 1 is the pigeonhole principle: for finite $A$, an [[Injective Function|injective]] map $A \to A$ is automatically [[Surjective Function|surjective]]. Infinite sets are exactly the ones where this fails ([[Infinite Set]], Theorem 1).
- A [[Countable Set]] is one that is finite or in bijection with $\mathbb{Z}^+$.

# Questions

> [!question]- How is Theorem 1 proved, and which finite fact does the proof use?
> By [[Proof by Induction|induction]] on $n = |A|$: show that every injection $f : I_n \to I_n$ is onto. For $n = 0$ it is trivial. For the step, compose $f : I_{n+1} \to I_{n+1}$ with the transposition swapping $f(n+1)$ and $n+1$. The result fixes $n+1$, so it restricts to an injection $I_n \to I_n$, which is onto by the hypothesis. The proof uses that $I_{n+1}$ has a *last element* $n+1$ to peel off. An infinite set has no last stage, and indeed $n \mapsto n+1$ is an injection $\mathbb{Z}^+ \to \mathbb{Z}^+$ that is not onto.

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=320)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=34)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=35)
