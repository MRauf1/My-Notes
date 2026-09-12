---
tags:
  - mathematics
  - abstract_algebra
---

# Definition

> [!info] Definition 1 ([[Cycle]] [[Group Conjugate|Conjugation]])
> For $\sigma, \tau \in S_n$, where $\tau = (a_1 \dots a_k)$
> $$
> \begin{align}
> \sigma (a_1 \dots a_k) \sigma^{-1} &= (\sigma(a_1) \dots \sigma(a_k))
> \end{align}
> $$

# Properties
- $\forall \sigma, \tau \in S_n$, $\tau$ and $\sigma \tau \sigma^{-1}$ have the same [[Cycle Type]]
- If $\tau, \tau' \in S_n$ have the same cycle type, then $\tau' = \sigma \tau \sigma^{-1}$ for some $\sigma \in S_n$
- Together, these two properties give: two permutations in $S_n$ are conjugate iff they have the same cycle type.