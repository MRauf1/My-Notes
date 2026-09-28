---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition
> [!info] Probability on a Countable Sample Space[^2]
> Let $\mathcal{C} = \{x_1, x_2, \dots\}$ be a [[Countable Set|countable]] [[Sample Space]] and $p_i \geq 0$ with $\sum_i p_i = 1$. Then
> $$
> \begin{align}
> P(A) = \sum_{x_i \in A} p_i, \quad A \subseteq \mathcal{C}
> \end{align}
> $$
> is a [[Probability]] on $\mathcal{C}$.

> [!info] Equilikely Case[^1][^2]
> Let $\mathcal{C} = \{x_1, \dots, x_m\}$ be finite and $p_i = 1/m$ for all $i$. Then for every $A \subseteq \mathcal{C}$,
> $$
> \begin{align}
> P(A) = \sum_{x_i \in A} \frac{1}{m} = \frac{\#(A)}{m}
> \end{align}
> $$
> where $\#(A)$ is the number of elements of $A$. In particular, each single outcome has probability $1/m$.

In the equilikely case, computing probabilities reduces to counting, via the [[Cartesian Product Set Cardinality|mn-rule]], [[Permutation (Combinatorics)|permutations]], and [[Combination|combinations]].

# Properties
- Special case of [[Probability]] under the [[Probability Frequentist Framework|frequentist framework]], applied when all $m$ possible outcomes are equally likely.
- The outcomes need not be equally likely for a general countable model; the equilikely assumption is a modeling choice (e.g. a fair die), not a consequence of the axioms.
- No equilikely model exists on a countably infinite sample space, since $\sum_i p = 1$ is impossible for constant $p$.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 6: Probability](https://www.feynmanlectures.caltech.edu/I_06.html)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=31)
