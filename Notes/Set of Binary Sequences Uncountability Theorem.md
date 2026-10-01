---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Uncountability of the Set of Binary Sequences)[^1]
> Let $A$ be the [[Set]] of all [[Sequence|sequences]] whose terms are the digits $0$ and $1$ (i.e. $A$ is the set of all functions $f: \mathbb{N} \to \{0, 1\}$). Then $A$ is [[Countable Set|uncountable]].

This is proved by a diagonal argument: given any sequence of elements of $A$, one constructs an element of $A$ that differs from the $n$th listed element in its $n$th digit, so no sequence of elements of $A$ can enumerate all of $A$.

# Properties
- Since $A \sim \mathcal{P}(\mathbb{N})$ (each binary sequence is the indicator sequence of a subset of $\mathbb{N}$), this is equivalent to [[Power Set|the power set]] of a countable set being uncountable.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=39)
