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
- In deterministic form, a model $\mathbf{x} = \mathbf{g}[\mathbf{y}, \boldsymbol{\phi}]$ that computes the real-world measurements $\mathbf{x}$ as a function of the output $\mathbf{y}$. It does not predict $\mathbf{y}$ directly: [[Inference (Machine Learning)|inference]] requires inverting $\mathbf{y} = \mathbf{g}^{-1}[\mathbf{x}, \boldsymbol{\phi}]$, which may be difficult; in exchange, prior knowledge about how the data were created can be built into the model.[^3]
- Most demanding of data, but provides the marginal $p(\mathbf{x})$ for [[Novelty Detection|novelty detection]]; contrasts with a [[Discriminative Model]].
- An [[Autoregressive Language Model]] is a generative model of text: it defines $Pr(t_1, \dots, t_N)$ and generates by sampling one token at a time.[^4]

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=21)
[^2]: [Bishop, 2006, p. 43](zotero://open-pdf/library/items/5G99AZ8U?page=63&annotation=I9CU6JKG)
[^3]: [Prince, p. 23](zotero://open-pdf/library/items/BWT7FYX5?page=37&annotation=KM6TDWK5); [Prince, p. 23](zotero://open-pdf/library/items/BWT7FYX5?page=37&annotation=36X3XLPQ)
[^4]: [Prince, p. 223](zotero://open-pdf/library/items/BWT7FYX5?page=237&annotation=5BVXXUTC)
