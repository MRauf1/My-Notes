---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition
> [!info] Relative Frequency[^1][^2]
> If a [[Random Experiment]] is performed $N$ times and [[Event]] $A$ occurs $f = \#\{A\}$ times (the frequency), the relative frequency of $A$ is
> $$
> \begin{align}
> f_A = \frac{\#\{A\}}{N}
> \end{align}
> $$

Relative frequency is erratic for small $N$, but as $N$ grows it tends to stabilize around a number $p$. Identifying $P(A)$ with this number is the relative frequency approach to [[Probability]] ([[Probability Frequentist Framework]]): we cannot predict a single outcome, but for large $N$ we can predict approximately how often the outcome lands in $A$. It presupposes the experiment can be repeated under essentially identical conditions.

# Properties
- $f_A \geq 0$ and $f_{\mathcal{C}} = 1$.
- If $A_1, A_2$ are [[Mutually Exclusive Events|disjoint]], $f_{A_1 \cup A_2} = f_{A_1} + f_{A_2}$.
- These three properties motivate the axioms of [[Probability]]; the axiomatic version strengthens the last to countable unions.
- The stabilization is made precise by the [[Strong Law of Large Numbers]]: $f_A \to P(A)$ almost surely.

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=13)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=18)
