---
tags:
  - computer_science
  - deep_learning
---

# Definition

Models that generate new data examples that are [[Statistics|statistically]] indistinguishable from the training examples. Some models learn the probability distribution of the data and sample from it, while others learn a mechanism for generation without describing the distribution.[^1]

These models rely on the statistics of the training data, and as such, do not truly understand the significance of their answers.

# Properties
- In classification, a generative approach models the class-conditional densities $p(\mathbf{x} | \mathcal{C}_k)$ and priors $p(\mathcal{C}_k)$ (or the joint $p(\mathbf{x}, \mathcal{C}_k)$) and obtains posteriors via [[Bayes' Theorem]]; it is called generative because sampling from it generates synthetic inputs ([[Three Approaches to Decision Problems]]).[^2]
- Most demanding of data, but provides the marginal $p(\mathbf{x})$ for [[Novelty Detection|novelty detection]]; contrasts with a [[Discriminative Model]].

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=21)
[^2]: [Bishop, 2006, p. 43](zotero://open-pdf/library/items/5G99AZ8U?page=63&annotation=I9CU6JKG)