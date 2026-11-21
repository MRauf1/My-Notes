---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Infinite Set)[^1][^2]
> A [[Set|set]] $A$ is infinite if it is not a [[Finite Set|finite set]], i.e. there is no $n \in \mathbb{N}$ with a [[Bijective Function|bijection]] $\{1, \dots, n\} \to A$.

> [!info] Definition 2 (Dedekind-Infinite Set)[^3]
> A set $A$ is Dedekind-infinite if $A \sim B$ for some [[Proper Subset|proper subset]] $B \subsetneq A$.

Infinity is defined *negatively*, as the failure of finiteness. So an infinite set has only the properties that can be proved from "not finite", and every finite fact whose proof needs a last element can fail.

# Types
- Countably infinite (denumerable): $A \sim \mathbb{Z}^+$ ([[Countable Set]]).
- Uncountable: infinite and not countably infinite, e.g. $\mathbb{R}$ ([[Cardinality of the Continuum]]) and $\mathcal{P}(\mathbb{Z}^+)$ ([[Cantor's Theorem]]).

# Properties

> [!abstract] Theorem 1 (Dedekind Characterization)[^2][^3]
> 1. Every Dedekind-infinite set is infinite (provable in ZF).
> 2. Assuming the axiom of countable choice (a weak form of the [[Axiom of Choice]]), every infinite set is Dedekind-infinite.
>
> So, under countable choice, $A$ is infinite $\iff$ $A$ is in bijection with a proper subset of itself.

- A set is Dedekind-infinite if and only if it has a countably infinite subset, i.e. there is an [[Injective Function|injection]] $\mathbb{N} \to A$.[^3]
- Part 1 is the contrapositive of [[Finite Set]] Theorem 1 (finite sets are not equinumerous with a proper subset).
- Every infinite subset of a [[Countable Set|countable set]] is countable, so countably infinite sets are the smallest infinite sets.
- The existence of an infinite set is not provable from the other axioms of set theory. It is postulated by the [[Axiom of Infinity]].

# Questions

> [!question]- Why does "infinite ⇒ Dedekind-infinite" need choice, and what is the proof once you have it?
> From "$A$ is not finite" alone you can pick distinct $a_1, a_2, \dots$ one at a time, since after finitely many picks $A$ is not exhausted. But turning infinitely many picks into a single function $n \mapsto a_n$ needs countable choice, and without any choice there are models of ZF with infinite sets that are not Dedekind-infinite. Given an injection $n \mapsto a_n$, define $f(a_n) = a_{n+1}$ and $f(x) = x$ otherwise. Then $f$ is a bijection from $A$ onto $A \setminus \{a_1\} \subsetneq A$, which is Hilbert's hotel.

> [!question]- Why is the definition of an infinite set negative, and what does that imply for intuition?
> "Infinite" is defined as "not in bijection with any $\{1, \dots, n\}$". No positive description of an infinite set is given, so every property must be *proved*. Intuitions such as "a proper subset is smaller", "a self-injection is onto", or "there is a largest element" are theorems about finite sets whose proofs peel off a last element by induction. They have no reason to survive, and for infinite sets they fail.

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=320)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=35)
[^3]: [Dedekind-infinite set (Wikipedia)](https://en.wikipedia.org/wiki/Dedekind-infinite_set)
