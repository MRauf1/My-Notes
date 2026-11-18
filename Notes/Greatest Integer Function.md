---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Greatest Integer Function)[^1]
> For $x \in \mathbb{R}$, $[\![x]\!] = \lfloor x \rfloor$ is the largest [[Integer]] that is less than or equal to $x$. It is also called the floor function.

# Properties
- $[\![x]\!] = n$ on $[n, n+1)$ for every integer $n$, so its graph is a staircase of half-open steps.
- At each integer $n$: $\lim_{x \to n^-} [\![x]\!] = n - 1 \neq n = \lim_{x \to n^+} [\![x]\!]$, so $\lim_{x \to n} [\![x]\!]$ does not exist ([[Limit of Function and One-Sided Limit of Function Theorem]]). Each integer is a [[Jump Discontinuity]]; the function is right-continuous there.
- Differentiable exactly on $\mathbb{R} \setminus \mathbb{Z}$, with derivative $0$ there ([[Differentiable Implies Continuous]] rules out the integers).

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=133)
