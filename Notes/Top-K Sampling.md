---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Top-K Sampling[^1]
> A [[Decoding (Language Model)|decoding]] strategy that samples the next token only from the $K$ most likely tokens, after renormalizing their probabilities (Fan et al., 2018).

# Properties
- Prevents choosing from the long tail of low-probability tokens, which can lead to an unnecessary linguistic dead end.[^1]
- With a fixed $K$, it can still allow unreasonable choices when only a few tokens have high probability; [[Nucleus Sampling]] addresses this.[^2]

[^1]: [Prince, p. 224](zotero://open-pdf/library/items/BWT7FYX5?page=238&annotation=S7KR3ZZ5); [Prince, p. 235](zotero://open-pdf/library/items/BWT7FYX5?page=249&annotation=PHFK6UEN)
[^2]: [Prince, p. 235](zotero://open-pdf/library/items/BWT7FYX5?page=249&annotation=PHFK6UEN)
