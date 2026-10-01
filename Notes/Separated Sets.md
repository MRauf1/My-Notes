---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Separated Sets)[^1]
> Let $(X, d)$ be a [[Metric Space]] and $A, B \subseteq X$. $A$ and $B$ are separated if both $A \cap \overline{B} = \emptyset$ and $\overline{A} \cap B = \emptyset$, where $\overline{A}, \overline{B}$ denote [[Closure Set|closure]]. Equivalently, no [[Point]] of $A$ lies in the closure of $B$, and no point of $B$ lies in the closure of $A$.

Separated sets are necessarily [[Disjoint Sets|disjoint]], since a point common to both $A$ and $B$ would lie in both closures. The converse fails: disjoint sets need not be separated.[^2]

> [!example]- Disjoint but not Separated, versus Separated
> In $\mathbb{R}$, the [[Interval|interval]] $[0, 1]$ and the segment $(1, 2)$ are disjoint but not separated, since $1$ is a [[Limit Point]] of $(1, 2)$ and so lies in $\overline{(1,2)} \cap [0,1]$. However, the segments $(0, 1)$ and $(1, 2)$ are separated.

# Properties
- A [[Subset]] $E$ of $(X,d)$ is [[Connected Metric Space|connected]] if and only if $E$ is not the union of two nonempty separated sets.[^1]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=51)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=51)
