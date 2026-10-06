---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Spectral Graph Convolution[^1]
> A convolution on a [[Graph]] performed in the graph Fourier domain, whose basis vectors are the [[Eigenvector|eigenvectors]] of the [[Graph Laplacian Matrix]] $\mathbf{L} = \mathbf{D} - \mathbf{A}$. With the [[Eigendecomposition|eigendecomposition]] $\mathbf{L} = \mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^T$, a signal $\mathbf{x} \in \mathbb{R}^N$ on the nodes is filtered by
> $$
> \begin{align}
> g_{\boldsymbol{\theta}} \star \mathbf{x} = \mathbf{U}\, g_{\boldsymbol{\theta}}(\boldsymbol{\Lambda})\, \mathbf{U}^T\mathbf{x},
> \end{align}
> $$
> where $\mathbf{U}^T\mathbf{x}$ is the graph Fourier transform and $g_{\boldsymbol{\theta}}(\boldsymbol{\Lambda})$ is a learned diagonal filter on the eigenvalues (graph frequencies).

The formula is the graph analogue of the convolution theorem: convolution becomes pointwise multiplication in the eigenbasis of the Laplacian, just as the complex exponentials diagonalize the [[Laplacian Operator]] on $\mathbb{R}^n$.[^2]

# Types
- **Spectral networks** (Bruna et al., 2013): free filter coefficients $g_{\boldsymbol{\theta}}(\boldsymbol{\Lambda}) = \mathrm{diag}(\boldsymbol{\theta})$.[^1]
- **Smooth spectral filters** (Henaff et al., 2015): forcing the Fourier representation to be smooth makes the filters localized in the spatial domain.[^1]
- **ChebNet** (Defferrard et al., 2016): approximates the filter by a degree-$K$ polynomial in Chebyshev polynomials $T_j$ evaluated at the rescaled Laplacian $\tilde{\mathbf{L}} = 2\mathbf{L}/\lambda_{\max} - \mathbf{I}$, computed with the recurrence $T_j(x) = 2xT_{j-1}(x) - T_{j-2}(x)$:[^3]
$$
\begin{align}
g_{\boldsymbol{\theta}} \star \mathbf{x} \approx \sum_{j=0}^{K} \theta_j T_j(\tilde{\mathbf{L}})\,\mathbf{x}.
\end{align}
$$
  This needs no eigendecomposition and is exactly $K$-hop localized, since $\tilde{\mathbf{L}}^j$ has non-zero entries only between nodes within distance $j$.
- **Kipf & Welling (2017) GCN**: the case $K = 1$ with the normalized Laplacian, $\lambda_{\max} \approx 2$, and a single parameter $\theta$, giving $\theta(\mathbf{I} + \mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2})\mathbf{x}$. This 1-hop filter is the [[Graph Convolutional Network|spatial GCN]] with Kipf [[Neighborhood Aggregation (Graph Neural Network)|normalization]], bridging spectral and spatial methods.[^3]

# Properties
- **Disadvantages of the plain spectral approach**: the filters are not spatially localized, and the eigendecomposition ($O(N^3)$) is prohibitively expensive for large graphs.[^1]
- **Graph-specific**: the filters are defined relative to one graph's Laplacian eigenbasis, so if the graph changes the model must be retrained; spatial methods avoid this.[^4]
- Low eigenvalues of $\mathbf{L}$ correspond to smooth signals (small $\mathbf{x}^T\mathbf{L}\mathbf{x}$), high eigenvalues to oscillating ones, so filters can be read as low-pass or high-pass; the Kipf GCN is a low-pass filter, which links to [[Oversmoothing]].[^2]

[^1]: [Prince, p. 262](zotero://open-pdf/library/items/BWT7FYX5?page=276&annotation=8WUSBTKD); filter formula added from general knowledge.
[^2]: Added from general knowledge.
[^3]: [Prince, p. 262](zotero://open-pdf/library/items/BWT7FYX5?page=276&annotation=8WUSBTKD); formulas added from general knowledge.
[^4]: [Prince, p. 262](zotero://open-pdf/library/items/BWT7FYX5?page=276&annotation=NF4XCUQI)
