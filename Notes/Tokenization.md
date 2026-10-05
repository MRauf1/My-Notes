---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Tokenization[^1]
> The first stage of a text-processing pipeline: a **tokenizer** splits text into smaller units (**tokens**) drawn from a fixed **vocabulary** $\mathcal{V}$ of possible tokens.

# Types
- **Word-level**: one token per word. Problems: some words (e.g. names) will be missing from the vocabulary; it is unclear how to handle punctuation, which carries meaning (e.g. a question mark); and variants of a word (walk, walks, walked, walking) need separate tokens with no indication that they are related.[^1]
- **Character-level**: letters and punctuation marks as the vocabulary. It splits text into very small parts, so the network must re-learn the relations between them.[^1]
- **Sub-word** (used in practice): a compromise whose vocabulary contains common words plus word fragments from which rarer words can be composed. Computed by e.g. **byte pair encoding**, which starts from characters and greedily merges the most frequently occurring adjacent pair of sub-strings into a new token until the vocabulary reaches the desired size.[^1]

# Properties
- Each token is then mapped to a learned [[Word Embedding|embedding]] before entering the [[Transformer]].
- A typical vocabulary size is $|\mathcal{V}| \approx 30{,}000$.[^2]

[^1]: [Prince, p. 218](zotero://open-pdf/library/items/BWT7FYX5?page=232&annotation=KFBSZTRG)
[^2]: [Prince, p. 218](zotero://open-pdf/library/items/BWT7FYX5?page=232&annotation=IKJSGRTP)
