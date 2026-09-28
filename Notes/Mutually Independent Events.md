---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Mutually Independent Events for $n$ Cases)[^2]
> [[Event|Events]] $A_1, A_2, \dots, A_n$ are mutually independent $\iff$ for every $k$ with $2 \leq k \leq n$ and every choice of $k$ distinct indices $d_1 < d_2 < \dots < d_k$ from $\{1, \dots, n\}$,
> $$
> \begin{align}
> P(A_{d_1} \cap A_{d_2} \cap \dots \cap A_{d_k}) = P(A_{d_1}) P(A_{d_2}) \cdots P(A_{d_k})
> \end{align}
> $$
> i.e. every sub-collection ([[Combination]]) of the events satisfies the product rule.

> [!info] Definition 2 (Mutually Independent Events for $3$ Cases)[^1]
> For [[Event|events]] $A, B, C$, they are mutually independent $\iff$
> 1) $A, B, C$ are pairwise [[Independent Events|independent]]: $P(A \cap B) = P(A)P(B)$, $P(A \cap C) = P(A)P(C)$, $P(B \cap C) = P(B)P(C)$
> 2) $P(A \cap B \cap C) = P(A) P(B) P(C)$

**Permutations vs. combinations.** Hogg et al. phrase Definition 1 as "for every permutation $d_1, \dots, d_k$", but [[Set Intersection]] and multiplication are both commutative, so reordering the chosen indices yields the same equation. Checking all [[Permutation (Combinatorics)|$k$-permutations]] ($P^n_k = \binom{n}{k} k!$ of them) repeats each condition $k!$ times; only the $\binom{n}{k}$ [[Combination|combinations]] give distinct conditions. What matters is which events are chosen, not their order. The total number of distinct conditions is
$$
\begin{align}
\sum_{k=2}^n \binom{n}{k} = 2^n - n - 1
\end{align}
$$

# Properties
- Pairwise independence does not imply mutual independence: the $\binom{n}{2}$ pairwise conditions do not constrain the higher-order intersections.
- Mutually independent $\implies P(A_1 \cap \dots \cap A_n) = P(A_1) \cdots P(A_n)$; the converse fails, as the single $k = n$ condition does not imply the lower-order ones.
- Replacing any sub-collection of the $A_i$ by their [[Set Complement|complements]] preserves mutual independence; more generally, events built from disjoint groups of the $A_i$ are independent. For $A, B, C$ mutually independent:
	1) $A, (B \cap C)$ are independent
	2) $A, (B \cup C)$ are independent
	3) $A^c, (B \cap C^c)$ are independent
	4) $A^c, B^c, C^c$ are mutually independent
- Outcomes of independent experiments: a sequence of [[Random Experiment|random experiments]] performed so that events associated with different experiments are mutually independent.[^3]

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=40)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=45)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=46)
