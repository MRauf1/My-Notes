---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Probability]] of [[Set Union]])[^1]
> For [[Event|events]] $A, B$, the probability of their union is
> $$
> \begin{align}
> P(A \cup B) = P(A) + P(B) - P(A \cap B)
> \end{align}
> $$

Proof: $A \cup B = A \cup (A^c \cap B)$ and $B = (A \cap B) \cup (A^c \cap B)$ are [[Disjoint Set Union|disjoint unions]] (see [[Venn Diagram]]), so additivity gives both $P(A \cup B) = P(A) + P(A^c \cap B)$ and $P(B) = P(A \cap B) + P(A^c \cap B)$.

> [!abstract] Theorem 1 (Inclusion-Exclusion Formula)[^1]
> For events $C_1, \dots, C_k$,
> $$
> \begin{align}
> P(C_1 \cup C_2 \cup \dots \cup C_k) = p_1 - p_2 + p_3 - \dots + (-1)^{k+1} p_k
> \end{align}
> $$
> where $p_i$ is the sum of the probabilities of all possible intersections of $i$ of the sets:
> $$
> \begin{align}
> p_1 = \sum_i P(C_i), \quad p_2 = \sum_{i<j} P(C_i \cap C_j), \quad p_3 = \sum_{i<j<l} P(C_i \cap C_j \cap C_l), \quad \dots, \quad p_k = P\left(\bigcap_{i=1}^k C_i\right)
> \end{align}
> $$

> [!abstract] Theorem 2 (Bonferroni Bounds)[^1]
> Truncating the inclusion-exclusion formula alternately over- and under-estimates the union:
> $$
> \begin{align}
> p_1 &\geq P(C_1 \cup \dots \cup C_k) \geq p_1 - p_2 \\
> p_1 - p_2 + p_3 &\geq P(C_1 \cup \dots \cup C_k) \geq p_1 - p_2 + p_3 - p_4
> \end{align}
> $$
> and in general a partial sum ending in a $+p_j$ term is an upper bound, one ending in a $-p_j$ term is a lower bound.

Hogg et al. also remark that $p_1 \geq p_2 \geq \dots \geq p_k$; this holds for $k = 3$ (where $p_1 \geq p_2 \geq p_3$) but is false in general: for four events each equal to $\mathcal{C}$, $p_1 = 4 < p_2 = \binom{4}{2} = 6$. The Bonferroni bounds above are the statements that hold for all $k$.

# Properties
- The first upper bound $P\left(\bigcup_i C_i\right) \leq p_1$ is [[Boole's Inequality]].
- For two events the first lower bound is equivalent to [[Bonferroni's Inequality]] $P(C_1 \cap C_2) \geq P(C_1) + P(C_2) - 1$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=29)
