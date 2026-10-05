---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Decoding (Language Model)[^1]
> The process of choosing output tokens from the next-token distributions $Pr(t_n \mid t_1, \dots, t_{n-1})$ returned by a [[Transformer Decoder|decoder]]: each chosen token is appended to the preceding text and the model is run again.

# Types
- **Greedy decoding**: pick the most likely token at each step. Results tend to be very generic, and the greedy sequence is not necessarily the most likely overall sequence.[^1]
- **Pure (ancestral) sampling**: sample from the full distribution. The long tail of unlikely tokens collectively has significant probability, which can lead to degraded output (Holtzman et al., 2020).[^1]
- [[Beam Search]]
- [[Top-K Sampling]]
- [[Nucleus Sampling]]

# Properties
- The naive methods fail partly because during training the model only sees ground-truth prefixes ([[Teacher Forcing]]) but at deployment it sees its own outputs.[^1]
- Searching over every combination of tokens is computationally infeasible, since the number of sequences grows as $|\mathcal{V}|^N$.[^2]

[^1]: [Prince, p. 235](zotero://open-pdf/library/items/BWT7FYX5?page=249&annotation=XMQF7NH8); [Prince, p. 224](zotero://open-pdf/library/items/BWT7FYX5?page=238&annotation=S7KR3ZZ5)
[^2]: [Prince, p. 235](zotero://open-pdf/library/items/BWT7FYX5?page=249&annotation=PHFK6UEN)
