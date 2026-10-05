---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Nucleus (Top-p) Sampling[^1]
> A [[Decoding (Language Model)|decoding]] strategy that samples the next token from the smallest set $\mathcal{V}^{(p)}$ of most likely tokens whose total probability mass reaches a fixed proportion $p$, after renormalizing (Holtzman et al., 2020):
> $$
> \begin{align}
> \sum_{t \in \mathcal{V}^{(p)}} Pr(t \mid t_1, \dots, t_{n-1}) \ge p
> \end{align}
> $$

# Properties
- Unlike [[Top-K Sampling]], the candidate set adapts to the distribution: it is small when a few tokens dominate and large when the distribution is flat.[^1]

[^1]: [Prince, p. 235](zotero://open-pdf/library/items/BWT7FYX5?page=249&annotation=PHFK6UEN)
