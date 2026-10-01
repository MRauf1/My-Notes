---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Countable Set[^1]
> A [[Set]] $C$ is countable if $C$ is finite or has as many elements as there are positive integers, i.e. there is a [[Bijective Function|bijection]] $C \to \mathbb{N}$. In the latter case $C$ is called countably infinite. A set that is not countable is uncountable.

# Properties
- $\mathbb{N}$, $\mathbb{Z}$, and $\mathbb{Q}$ are countably infinite; $\mathbb{R}$ and every [[Non-degenerate Interval]] are uncountable. The [[Set of Binary Sequences Uncountability Theorem|set of all binary (0/1) sequences]] is likewise uncountable.
- A countable union of countable sets is countable. More generally, if $A$ is at most countable and $B_\alpha$ is at most countable for every $\alpha \in A$, then $\bigcup_{\alpha \in A} B_\alpha$ is at most countable.[^2]
- If $A$ is a countable set, then the set of all $n$-tuples $(a_1, \dots, a_n)$ with each $a_k \in A$ (not necessarily distinct) is countable.[^2] This is how one shows $\mathbb{Q}$ is countable, by viewing a rational number as a pair of integers.
- Every infinite subset of a countable set is countable; equivalently, no uncountable set can be a subset of a countable set, so countably infinite sets are the "smallest" kind of infinite set.[^3]
- A set is infinite if and only if it is equivalent (in bijection) to one of its own proper subsets; a finite set can never be put in bijection with a proper subset of itself.[^4]
- Countability is the dividing line in the axioms of [[Probability]]: additivity is required over countable [[Mutually Exclusive Events|disjoint]] unions, and a [[Sigma-Field]] is closed under countable unions.
- A [[Discrete Random Variable]] is one whose space is countable.

Rudin's *Principles of Mathematical Analysis* uses a stricter convention: there, "countable" means countably infinite specifically (in bijection with $\mathbb{N}$), while "at most countable" means finite or countably infinite. The definition above (countable = finite or countably infinite) follows the convention of this note's primary source instead, which matches what is elsewhere called "at most countable."

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=19)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=38)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=35)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=35)
