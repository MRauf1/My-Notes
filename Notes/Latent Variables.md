---
tags: computer_science, deep_learning
---

# Definition

One approach to represent high-dimensional variables is through a lower-dimensional, smaller representation (latent variables). The idea behind this is that the real-world data is often generated due to some structure (like images being formed through physical processes), and this structure adds constraints to the problem, which makes the representation lower-dimensional (latent variables).[^1]

Latent variables typically have a simpler probability distribution, and in generative tasks, can produce the desired output with the help of [[Decoder|decoders]].

Latent variables, while used primarily in [[Unsupervised Learning|unsupervised learning]], can also be used with [[Supervised Learning|supervised learning]] models. This results in multiple benefits:

1) Since latent variables are lower-dimensional, one will likely need less training samples.
2) Since latent variables correspond to plausible data, one can better enforce the model to produce more plausible examples through using latent variables
3) By adding randomness to the mapping between either the latent variables or the latent variable with the corresponding output, one can generate multiple images with the supervised constraint (like images following a certain caption).

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=23)