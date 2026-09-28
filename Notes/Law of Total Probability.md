---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Law of Total Probability)
> For [[Event|event]] $A$, and [[Mutually Exclusive Events|mutually exclusive]] and [[Exhaustive Events|exhaustive]] events $B_1, B_2, \dots, B_n$ (a [[Partition]] of the [[Sample Space]]) with $P(B_i) > 0$[^1][^2]
> $$
> \begin{align}
> A &= (B_1 \cap A) \cup (B_2 \cap A) \cup \dots \cup (B_n \cap A) \\
> P(A) &= \sum_{i=1}^{n} P(A | B_i) P(B_i)
> \end{align}
> $$

The first line is a [[Disjoint Set Union|disjoint union]], so the second follows from additivity and the [[Conditional Probability Multiplication Rule]]. The partition events need not be equally likely.

# Properties
- Holds for a countable partition $B_1, B_2, \dots$ by countable additivity.
- Supplies the denominator of [[Bayes' Theorem]].
- Its expectation analogue is the [[Law of Total Expectation]]; for random variables, $p_2(x_2) = \sum_{x_1} p_{2|1}(x_2 | x_1) p_1(x_1)$ with the [[Conditional Distribution]].

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=45)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=42)
