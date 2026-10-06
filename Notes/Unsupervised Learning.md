---
tags:
  - computer_science
  - deep_learning
---

# Definition

[[Subset|Subset]] of [[Machine Learning|machine learning]] that learns without labeled data. The goal is to describe/understand structure within the data.[^1]

# Properties
- Rather than matching observed input-output examples as in [[Supervised Learning]], learns by optimizing for desirable properties of the input-output mapping.[^2]
- Given input data $\{\mathbf{x}^{(i)}\}_{i=1}^N$ without target outputs, the learner comes up with a model or representation of the input data with useful properties, as measured by an [[Objective Function]]; for example, the objective may reward compressing the data into a lower-dimensional format that still preserves all information about the inputs.
- Defining characteristic: learned from observed data $\{\mathbf{x}_i\}$ alone, in the absence of labels; in contrast, [[Supervised Learning]] maps $\mathbf{x}$ to outputs $\mathbf{y}$ using a loss on pairs $\{\mathbf{x}_i, \mathbf{y}_i\}$.[^4]
- A common strategy is a mapping between data $\mathbf{x}$ and lower-dimensional [[Latent Variables|latent variables]] $\mathbf{z}$, in either direction: data to latent (e.g. k-means maps $\mathbf{x}$ to a cluster assignment $z \in \{1, \dots, K\}$) or latent to data ([[Generative Model|generative models]]).[^5]

![[Unsupervised Learning Model Taxonomy.png]]

# Types
- [[Clustering]]: discovering groups of similar examples within the data.[^3]
- [[Density Estimation]]: determining the distribution of the data within the input space.
- Visualization: projecting data from a high-dimensional space down to two or three dimensions.
- [[Generative Model|Generative models]], including [[Probabilistic Generative Model|probabilistic generative models]]; these overlap with, but are distinct from, latent variable models.[^5]

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=21)
[^2]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)
[^3]: [Bishop, 2006, p. 3](zotero://open-pdf/library/items/5G99AZ8U?page=23&annotation=FBYN8VEI)
[^4]: [Prince, p. 269](zotero://open-pdf/library/items/BWT7FYX5?page=283&annotation=UYK298VE); [Prince, p. 269](zotero://open-pdf/library/items/BWT7FYX5?page=283&annotation=8GPQJ9EJ)
[^5]: [Prince, p. 269](zotero://open-pdf/library/items/BWT7FYX5?page=283&annotation=H9U8U3RJ); [Prince, p. 270](zotero://open-pdf/library/items/BWT7FYX5?page=284&annotation=BRF8BGVS)
