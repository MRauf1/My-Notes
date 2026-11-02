---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 ([[Proof]] by Induction)[^1]
> To prove a goal of form $\forall n \in \mathbb{N}, P(n)$
> 1) Base Case: Prove $P(0)$
> 2) Induction Step: Prove $\forall n \in \mathbb{N}, P(n) \implies P(n + 1)$
> Assuming $P(n)$ is true is called the Inductive Hypothesis

A natural number has the property based on the assumption that the previous natural number has the property.

> [!info] Scope of Induction[^2]
> Induction proves the countable family of statements
> $$\begin{align}
> P(0),\; P(1),\; P(2),\; \dots
> \end{align}$$
> each of which concerns a finite $n \in \mathbb{N}$. There is no statement $P(\infty)$ in this family, so induction never proves a property of an object built by infinitely many steps (an infinite product, union, intersection, limit, etc.).

"Induction works on [[Countable Set|countable sets]]" and "induction does not reach countably infinite operations" are consistent because "countable" counts different things:
- In the first, it counts the **statements** being proved (one per $n$; the domain of quantification is $\mathbb{N}$, or any set in bijection with it).
- In the second, it counts the **steps inside a single object** (e.g. the factors of $\prod_{i=1}^\infty A_i$), which is not equal to the $n$-th stage for any $n$.

Induction proves infinitely many finite facts, never an infinite fact. Passing from "true at every finite stage" to "true at the infinite stage" is a separate limit step, which is made explicit in [[Principle of Transfinite Induction|transfinite induction]].

# Types
- [[Proof by Strong Induction]]
- [[Principle of Transfinite Induction]] (generalization to [[Well-Ordered Set|well-ordered sets]] and ordinals)

# Properties
- The limit step can fail: $\{0,1\}^n$ is finite for every $n$, but $\{0,1\}^{\mathbb{N}}$ is uncountable ([[Set of Binary Sequences Uncountability Theorem]]). So induction shows that finite products of countable sets are countable, but says nothing about countable products.
- The limit step can hold, but even then it needs its own proof: induction only shows that finite unions of countable sets are countable. That a countable union of [[Countable Set|countable sets]] is countable needs a direct enumeration argument (using the [[Axiom of Choice|axiom of countable choice]]).
- Knowing that every finite truncation (projection onto the first $n$ coordinates) of a set has some property does not imply that the whole set has it.

# Questions
> [!question]- Finite products of countable sets are countable by induction. Why doesn't induction show that a countable product of countable sets is countable?
> Induction proves $P(n)$: "$A_1 \times \cdots \times A_n$ is countable" for each finite $n$, but $\prod_{i=1}^\infty A_i$ is not $A_1 \times \cdots \times A_n$ for any $n$, so it is not covered. Reaching it would need a limit step, which fails here: $\{0,1\}^{\mathbb{N}}$ is uncountable.

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=274)
[^2]: [Mathematical Induction (Wikipedia)](https://en.wikipedia.org/wiki/Mathematical_induction)
