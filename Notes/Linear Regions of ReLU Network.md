---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Linear Regions of ReLU Network[^1]
> A neural network with [[ReLU Function|ReLU]] activations computes a continuous piecewise linear function that partitions the input space $\mathbb{R}^{D_i}$ into convex polytopes, the linear regions, bounded by the hyperplanes where hidden units switch between **active** (not clipped) and **inactive** (clipped). Each region corresponds to a distinct **activation pattern** of the hidden units and contains a different linear function; the polytopes are shared by all outputs, but the linear functions within them can differ per output.

# Properties
- **Shallow network**, $D$ hidden units: at most $D + 1$ regions for $D_i = 1$.[^2] In $D_i$ dimensions, the $D$ hyperplanes create at most $\sum_{j=0}^{D_i} \binom{D}{j}$ regions.[^3] With $D = D_i$ hyperplanes aligned to the coordinate axes, the space divides into $2^{D_i}$ orthants; since shallow networks usually have $D > D_i$, they typically create more than $2^{D_i}$ regions, so the count grows rapidly with input dimension.[^4]
- **Deep network**, $D_i = D_o = 1$, $K$ layers of $D > 2$ units: up to $(D + 1)^K$ regions using $3D + 1 + (K - 1)D(D + 1)$ parameters, versus $D + 1$ regions from $3D + 1$ parameters for a [[Shallow Neural Network]].[^5]
- **Deep network, general bounds** (Montúfar et al., 2014): with $D$ hidden units in total, at most $2^D$ regions. With $K$ layers of $D \geq D_i$ units each, the number of regions is
$$
\begin{align}
O\left(\left(\frac{D}{D_i}\right)^{(K-1)D_i} D^{D_i}\right)
\end{align}
$$
Tighter bounds allowing different widths per layer exist (Montúfar, 2017; Arora et al., 2016; Serra et al., 2018), and Serra et al. (2018) give an algorithm that counts regions exactly, practical only for very small networks.[^3]
- **Exact maximum**: if all $K$ layers have $D$ units and $D$ is an integer multiple of $D_i$, the maximum number of regions is
$$
\begin{align}
N_r = \left(\frac{D}{D_i} + 1\right)^{D_i(K-1)} \cdot \sum_{j=0}^{D_i} \binom{D}{j}
\end{align}
$$
The first factor comes from the first $K - 1$ layers repeatedly folding the input space ([[Neural Network Folding]]), devoting $D / D_i$ units per input dimension; the second is the number of regions the last layer can create as a shallow network.[^6]
- The large region counts of deep networks carry complex dependencies and symmetries, and flexibility is still limited by the number of parameters. It is unclear that more regions help unless the target function has similar symmetries or is truly a composition of simpler functions.[^7]
- Its ease of characterization in terms of regions is the main reason ReLU is the default [[Activation Layer|activation]] in theoretical treatments.[^8]

[^1]: [Prince, p. 27](zotero://open-pdf/library/items/BWT7FYX5?page=41&annotation=XVPMFM4H); [Prince, p. 35](zotero://open-pdf/library/items/BWT7FYX5?page=49&annotation=W2XKTGZD)
[^2]: [Prince, p. 29](zotero://open-pdf/library/items/BWT7FYX5?page=43&annotation=IRUAYRI5)
[^3]: [Prince, p. 52](zotero://open-pdf/library/items/BWT7FYX5?page=66&annotation=8XDLGRWV); [Prince, p. 53](zotero://open-pdf/library/items/BWT7FYX5?page=67&annotation=UWK5W5FE)
[^4]: [Prince, p. 33](zotero://open-pdf/library/items/BWT7FYX5?page=47&annotation=89DX8UFZ)
[^5]: [Prince, p. 50](zotero://open-pdf/library/items/BWT7FYX5?page=64&annotation=C9SH66XE)
[^6]: [Prince, p. 52](zotero://open-pdf/library/items/BWT7FYX5?page=66&annotation=6QL52Q46); [Prince, p. 53](zotero://open-pdf/library/items/BWT7FYX5?page=67&annotation=AVKP8YFJ); [Prince, p. 53](zotero://open-pdf/library/items/BWT7FYX5?page=67&annotation=UWK5W5FE)
[^7]: [Prince, p. 50](zotero://open-pdf/library/items/BWT7FYX5?page=64&annotation=ANIWQU9S)
[^8]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
