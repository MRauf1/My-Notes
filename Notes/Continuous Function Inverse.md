---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 ([[Continuous Function]] [[Inverse Function]])[^1]
> Inverse of a continuous function is also a continuous function.

> [!abstract] Theorem 2 (Inverse of Continuous Bijection on [[Compact Metric Space]])[^2]
> Suppose $f$ is a continuous [[Injective Function|one-to-one]] mapping of a [[Compact Metric Space]] $X$ onto a [[Metric Space]] $Y$. Then the [[Inverse Function]] $f^{-1}$, defined on $Y$ by $f^{-1}(f(x)) = x$ ($x \in X$), is a continuous mapping of $Y$ onto $X$.

Definition 1 is not true in general: it holds for a continuous one-to-one function on an interval of $\mathbb{R}$ ([[Continuous Function Strictly Increasing Inverse Theorem]]), but for general domains some hypothesis such as compactness is required; Rudin's Example 4.21 shows that compactness of $X$ cannot be dropped in Theorem 2.[^3]

# Properties
- Proof via [[Continuous Function on Metric Space Theorem|Corollary 2]] (closed sets) and [[Continuous Function Compact Metric Space Theorem]].
- A continuous bijection has a continuous inverse if and only if it is an [[Open Map]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=152)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=99)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=100)
