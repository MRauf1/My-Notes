---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Autoregressive Language Model[^1]
> A model that predicts the conditional distribution $Pr(t_n \mid t_1, \dots, t_{n-1})$ of each token given all prior tokens, and thereby indirectly defines the joint probability of all $N$ tokens via the chain rule ([[Conditional Probability Multiplication Rule]]):
> $$
> \begin{align}
> Pr(t_1, t_2, \dots, t_N) = Pr(t_1) \prod_{n=2}^{N} Pr(t_n \mid t_1, \dots, t_{n-1})
> \end{align}
> $$

# Properties
- Shows that maximizing the [[Joint Probability|joint probability]] of the tokens is equivalent to the next-token prediction task: training maximizes $\sum_n \log Pr(t_n \mid t_{<n})$ ([[Log-Likelihood Function]]).[^2]
- A [[Generative Model]]: since it defines a probability model over text, new plausible text can be sampled one token at a time, feeding each chosen token back in ([[Decoding (Language Model)]]).[^3]
- Implemented by a [[Transformer Decoder]] (e.g. GPT3).
- Enormous language models are argued to be **few-shot learners**, able to perform novel tasks from just a few examples in the prompt; in practice performance is erratic, and how far they extrapolate rather than interpolate or copy verbatim is unclear.[^4]

[^1]: [Prince, p. 222](zotero://open-pdf/library/items/BWT7FYX5?page=236&annotation=Q3PRHHBM); [Prince, p. 223](zotero://open-pdf/library/items/BWT7FYX5?page=237&annotation=79LDJ5II)
[^2]: [Prince, p. 223](zotero://open-pdf/library/items/BWT7FYX5?page=237&annotation=79LDJ5II); [Prince, p. 223](zotero://open-pdf/library/items/BWT7FYX5?page=237&annotation=FWWCN2W4)
[^3]: [Prince, p. 223](zotero://open-pdf/library/items/BWT7FYX5?page=237&annotation=5BVXXUTC)
[^4]: [Prince, p. 225](zotero://open-pdf/library/items/BWT7FYX5?page=239&annotation=6UDGSAYB)
