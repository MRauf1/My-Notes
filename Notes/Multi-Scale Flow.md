---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Multi-Scale Flow[^1]
> A [[Normalizing Flow|normalizing flow]] architecture that partitions the latent vector $\mathbf{z} = [\mathbf{z}_1, \mathbf{z}_2, \dots, \mathbf{z}_N]$ and introduces the partitions gradually:
> - **Generative direction**: $\mathbf{z}_1$ is processed by invertible layers of its own dimension until $\mathbf{z}_2$ is appended and combined with it, and so on, until the representation has the full size of the data $\mathbf{x}$.
> - **Normalizing direction**: the network starts at the full dimension of $\mathbf{x}$; at the point where $\mathbf{z}_n$ was added, that part is split off, skips the remaining processing, and is assessed against the base distribution.

![[Multi-Scale Flow.png]]

# Properties
- **Motivation**: flows require $\dim \mathbf{z} = \dim \mathbf{x}$, but natural data can often be described by fewer underlying variables. All variables must be introduced at some point, but passing them all through the entire network is inefficient.[^1]
- Makes both density estimation and sampling faster.[^1]
- The log-likelihood is the sum of the base log-densities of all the factored-out $\mathbf{z}_n$ plus the log Jacobian determinants of the layers.
- Used in RealNVP and [[Glow]], where partitions are factored out after spatial squeezing at successive resolutions.

[^1]: [Prince, p. 317](zotero://open-pdf/library/items/BWT7FYX5?page=331&annotation=M7D3HJB3); [Prince, p. 318](zotero://open-pdf/library/items/BWT7FYX5?page=332&annotation=NHP69A4E)
