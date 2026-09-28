---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Word Embedding[^1]
> A *distributed representation* of words in which each word is mapped ("embedded") to a vector of numbers, its coordinates in an abstract space where related words lie nearer one another; this vector is the word's [[Representation (Machine Learning)|representation]].

# Properties
- Learned by self-supervision: initialise word vectors randomly; repeatedly hide a word in a phrase from a corpus and ask the model to predict it from context; on errors, nudge the correct word's vector toward the context words and incorrect guesses away.[^2]
- Because they capture the statistics of human language, embeddings absorb societal stereotypes (e.g. gender associations of professions), a prominent case of [[Algorithmic Bias]].[^3]
- Conversely, they can serve as a quantitative mirror of society for social science.

[^1]: [Christian, 2021, p. 41](zotero://open-pdf/library/items/P27SWKW4?page=41&annotation=UUYVA5WY); [Christian, 2021, p. 41](zotero://open-pdf/library/items/P27SWKW4?page=41&annotation=T8FCNC3H)
[^2]: [Christian, 2021, p. 42](zotero://open-pdf/library/items/P27SWKW4?page=42&annotation=EQJDFCX8); [Christian, 2021, p. 42](zotero://open-pdf/library/items/P27SWKW4?page=42&annotation=7KXZ3TYV)
[^3]: [Christian, 2021, p. 44](zotero://open-pdf/library/items/P27SWKW4?page=44&annotation=K7HW6MKD)
