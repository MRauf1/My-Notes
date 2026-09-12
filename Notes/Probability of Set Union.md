---
tags:
  - statistics
  - introduction_to_statistics
---

# Definition

> [!info] Definition 1 ([[Probability]] of [[Set Union]])
> For [[Set|sets]] $A, B$, the probability of their union is
> $$
> \begin{align}
> P(A \cup B) = P(A) + P(B) - P(A \cap B)
> \end{align}
> $$

This generalizes to $n$ sets $A_1, \dots, A_n$ via the inclusion-exclusion principle:
$$
\begin{align}
P\left(\bigcup_{i=1}^n A_i\right) = \sum_i P(A_i) - \sum_{i<j} P(A_i \cap A_j) + \sum_{i<j<k} P(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n+1} P\left(\bigcap_{i=1}^n A_i\right)
\end{align}
$$