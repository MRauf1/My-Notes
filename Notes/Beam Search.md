---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Beam Search[^1]
> A [[Decoding (Language Model)|decoding]] algorithm that maintains a fixed number $B$ (the **beam width**) of partial hypotheses in parallel. At each step every hypothesis is extended by every token, and the $B$ extensions with the highest total log probability $\sum_n \log Pr(t_n \mid t_{<n})$ are kept; the most likely complete sequence is returned at the end.

# Properties
- Approximates the most likely overall sequence, which greedy decoding (the case $B = 1$) need not find, without the infeasible cost of searching all sequences.[^1]
- Tends to produce many similar hypotheses; variants encourage more diverse sequences (Vijayakumar et al., 2016; Kulikov et al., 2018).[^2]

[^1]: [Prince, p. 224](zotero://open-pdf/library/items/BWT7FYX5?page=238&annotation=S7KR3ZZ5); [Prince, p. 235](zotero://open-pdf/library/items/BWT7FYX5?page=249&annotation=PHFK6UEN)
[^2]: [Prince, p. 235](zotero://open-pdf/library/items/BWT7FYX5?page=249&annotation=PHFK6UEN)
