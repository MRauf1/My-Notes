---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Domain Transformation[^1]
> A technique for removing floors, ceilings, and lower-order terms from a [[Divide and Conquer]] recurrence $T$ by passing to a shifted function $S(n) = T(n + \alpha)$, with the constant $\alpha$ chosen so that $S$ satisfies a clean recurrence.
>
> For an upper bound, first overestimate $T$ to remove the ceiling (and unequal subproblem sizes), then shift:[^2]
> $$\begin{align}
> T(n) &\leq 2T(\lceil n/2 \rceil) + n \leq 2T(n/2 + 1) + n, \\
> S(n) = T(n+\alpha) &\leq 2T(n/2 + \alpha/2 + 1) + n + \alpha = 2S(n/2 - \alpha/2 + 1) + n + \alpha.
> \end{align}$$
> Choosing $\alpha = 2$ gives $S(n) \leq 2S(n/2) + n + 2$, so by the [[Recursion Tree]] method $S(n) = O(n\log n)$, and hence $T(n) = S(n-2) = O(n \log n)$.[^3]

Since similar transformations work for any divide-and-conquer recurrence, floors, ceilings, and lower-order terms may be silently ignored from then on.[^4]

# Properties
- Preserves [[Big O|asymptotic]] bounds, since $\alpha$ is a constant shift.
- Used together with the [[Recursion Tree]] method.

[^1]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=52&annotation=UTAI5CL6)
[^2]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=53&annotation=59FZLGQT)
[^3]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=53&annotation=KHQYKZQU)
[^4]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=53&annotation=SM5NN689)
