---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition

> [!abstract] Theorem 1 ([[Conditional Probability]] [[Multiplication]] Rule)[^1][^2]
> $$
> \begin{align}
> P(A \cap B) = P(A) P(B | A) = P(B) P(A | B)
> \end{align}
> $$
> where $P(A) > 0$ in the first case and $P(B) > 0$ in the second case

> [!abstract] Theorem 2 (Multiplication Rule for Three Events)[^2]
> For [[Event|events]] $A, B, C$ with $P(A \cap B) > 0$,
> $$
> \begin{align}
> P(A \cap B \cap C) = P(A) P(B | A) P(C | A \cap B)
> \end{align}
> $$

> [!abstract] Theorem 3 (Generalized Multiplication Rule for $k$ Events)[^2]
> For events $A_1, \dots, A_k$ with $P(A_1 \cap \dots \cap A_{k-1}) > 0$,
> $$
> \begin{align}
> P\left(\bigcap_{i=1}^k A_i\right) = P(A_1) P(A_2 | A_1) P(A_3 | A_1 \cap A_2) \cdots P(A_k | A_1 \cap \dots \cap A_{k-1}) = \prod_{i=1}^k P\left(A_i \,\middle|\, \bigcap_{j=1}^{i-1} A_j\right)
> \end{align}
> $$
> where the $i = 1$ factor is $P(A_1)$.

Proof by induction on $k$: the case $k = 2$ is Theorem 1; for the step, apply Theorem 1 to $B = A_1 \cap \dots \cap A_{k-1}$ and $A_k$, giving $P(B \cap A_k) = P(B) P(A_k | B)$, then expand $P(B)$ by the induction hypothesis. The positivity condition on $A_1 \cap \dots \cap A_{k-1}$ implies every earlier intersection has positive probability, so every conditional probability is defined.

# Properties
- For [[Mutually Independent Events]], every conditional factor reduces to $P(A_i)$ and the rule becomes $P\left(\bigcap_i A_i\right) = \prod_i P(A_i)$.
- It is the event form of the chain rule for [[Joint Probability Distribution|joint distributions]] $p(x_1, \dots, x_k) = \prod_i p(x_i | x_1, \dots, x_{i-1})$.

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=30)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=41)
