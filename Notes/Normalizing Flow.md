---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Normalizing Flow[^1]
> A [[Probabilistic Generative Model|probabilistic generative model]] that transforms a simple, tractable base density $Pr(\mathbf{z})$ over [[Latent Variables|latent variables]] $\mathbf{z} \in \mathbb{R}^D$ into a complex density over data $\mathbf{x} \in \mathbb{R}^D$ through an **invertible** deep network $\mathbf{x} = \mathbf{f}[\mathbf{z}, \boldsymbol{\phi}]$. By the [[Random Vector Transformation|change-of-variables formula]], the likelihood of a data point is
> $$
> \begin{align}
> Pr(\mathbf{x} | \boldsymbol{\phi}) = \left|\frac{\partial \mathbf{f}[\mathbf{z}, \boldsymbol{\phi}]}{\partial \mathbf{z}}\right|^{-1} \cdot Pr(\mathbf{z}), \qquad \mathbf{z} = \mathbf{f}^{-1}[\mathbf{x}, \boldsymbol{\phi}]
> \end{align}
> $$
> where $|\partial \mathbf{f} / \partial \mathbf{z}|$ is the absolute [[Determinant]] of the $D \times D$ [[Jacobian Matrix]]. In 1D this is the absolute derivative $|\partial f / \partial z|$.
> - **Generative (forward) direction** $\mathbf{x} = \mathbf{f}[\mathbf{z}, \boldsymbol{\phi}]$: sampling, by drawing $\mathbf{z}^* \sim Pr(\mathbf{z})$ and computing $\mathbf{x}^* = \mathbf{f}[\mathbf{z}^*, \boldsymbol{\phi}]$.
> - **Normalizing (inverse) direction** $\mathbf{z} = \mathbf{f}^{-1}[\mathbf{x}, \boldsymbol{\phi}]$: likelihood evaluation. The base density is usually a standard [[Multivariate Normal Distribution|multivariate normal]] $\mathrm{Norm}_{\mathbf{z}}[\mathbf{0}, \mathbf{I}]$, so this direction turns the data distribution into a normal one.

**Intuition.** Probability mass is conserved, so the density decreases where $\mathbf{f}$ stretches space and increases where it compresses it. The absolute Jacobian determinant measures this local change in volume ([[Determinant Volume Scaling Theorem]]): if it is greater than one the density drops, if smaller it rises.[^2]

# Types
- [[Linear Flow]] and [[Elementwise Flow]]: easy to invert, with cheap Jacobians, but not expressive enough alone; used as building blocks.[^5]
- [[Coupling Flow]]
- [[Autoregressive Flow]] (masked and inverse)
- [[Residual Flow]] (reversible and contractive/invertible residual networks)
- [[Multi-Scale Flow]]
- [[Glow]]: an image model combining these ideas.

# Properties
- **Layered composition**: the network is a composition of invertible layers $\mathbf{f}_k[\bullet, \boldsymbol{\phi}_k]$, and the inverse applies the layer inverses in reverse order:[^3]
$$
\begin{align}
\mathbf{x} &= \mathbf{f}_K\left[\mathbf{f}_{K-1}\left[\dots \mathbf{f}_2\left[\mathbf{f}_1[\mathbf{z}, \boldsymbol{\phi}_1], \boldsymbol{\phi}_2\right], \dots \boldsymbol{\phi}_{K-1}\right], \boldsymbol{\phi}_K\right] \\
\mathbf{z} &= \mathbf{f}_1^{-1}\left[\mathbf{f}_2^{-1}\left[\dots \mathbf{f}_{K-1}^{-1}\left[\mathbf{f}_K^{-1}[\mathbf{x}, \boldsymbol{\phi}_K], \boldsymbol{\phi}_{K-1}\right], \dots \boldsymbol{\phi}_2\right], \boldsymbol{\phi}_1\right]
\end{align}
$$
  Each inverse layer gradually moves, or "flows", the data density toward the normal distribution, hence the name.
- **Jacobian of the composition**: by the [[Derivative Chain Rule|chain rule]] the Jacobian is a product of layer Jacobians (writing $\mathbf{f}_k$ for the output of layer $k$), so by [[Determinant Matrix Multiplication]] the absolute determinant factorizes:[^3]
$$
\begin{align}
\left|\frac{\partial \mathbf{f}[\mathbf{z}, \boldsymbol{\phi}]}{\partial \mathbf{z}}\right| = \left|\frac{\partial \mathbf{f}_1[\mathbf{z}, \boldsymbol{\phi}_1]}{\partial \mathbf{z}}\right| \cdot \left|\frac{\partial \mathbf{f}_2[\mathbf{f}_1, \boldsymbol{\phi}_2]}{\partial \mathbf{f}_1}\right| \cdots \left|\frac{\partial \mathbf{f}_K[\mathbf{f}_{K-1}, \boldsymbol{\phi}_K]}{\partial \mathbf{f}_{K-1}}\right|
\end{align}
$$
  The absolute Jacobian determinant of the inverse mapping is the reciprocal of that of the forward mapping.
- **Training**: [[Maximum Likelihood Learning|maximum likelihood]] on i.i.d. data $\{\mathbf{x}_i\}_{i=1}^I$, i.e. minimizing the negative log-likelihood:[^4]
$$
\begin{align}
\hat{\boldsymbol{\phi}} = \underset{\boldsymbol{\phi}}{\operatorname{argmax}}\left[\prod_{i=1}^I Pr(\mathbf{z}_i) \cdot \left|\frac{\partial \mathbf{f}[\mathbf{z}_i, \boldsymbol{\phi}]}{\partial \mathbf{z}_i}\right|^{-1}\right] = \underset{\boldsymbol{\phi}}{\operatorname{argmin}}\left[\sum_{i=1}^I \log\left[\left|\frac{\partial \mathbf{f}[\mathbf{z}_i, \boldsymbol{\phi}]}{\partial \mathbf{z}_i}\right|\right] - \log\left[Pr(\mathbf{z}_i)\right]\right], \qquad \mathbf{z}_i = \mathbf{f}^{-1}[\mathbf{x}_i, \boldsymbol{\phi}]
\end{align}
$$
  This is minimizing the forward [[Kullback-Leibler Divergence]] from the empirical data distribution to the model.
- **Layer requirements**: for the theory to be practical, the layers $\mathbf{f}_k$ must[^4]
	1. collectively be expressive enough to map a multivariate standard normal to an arbitrary density;
	2. be invertible, i.e. each a [[Bijective Function|bijection]] (otherwise the inverse is ambiguous);
	3. have an efficiently computable inverse (closed form or a fast algorithm), since it is evaluated every time the likelihood is computed during training;
	4. have an efficiently computable Jacobian determinant, in either the forward or the inverse direction.
- **Same dimension**: invertibility forces the latent space to have the same size as the data space, even though natural data can often be described by fewer underlying variables ([[Multi-Scale Flow]] mitigates the cost).[^6]
- **Exact likelihood**: of [[Generative Adversarial Network|GANs]], [[Variational Autoencoder|VAEs]], normalizing flows, and [[Diffusion Model|diffusion models]], only normalizing flows compute the exact log-likelihood of a new sample; GANs are not probabilistic, and VAEs and diffusion models return only a lower bound ([[Test Likelihood]], [[Generative Model Desiderata]]).[^7]
- **Sample quality**: samples are not as good as those from GANs or diffusion models. It is unknown whether this is a fundamental restriction of invertible layers or merely the result of less research effort.[^8]
- **Discrete data**: images are quantized, so the training likelihood can increase without bound unless noise is added ([[Dequantization]]).[^7]
- **Approximating another density**: a flow can also be fit, as a student, to a target density that is easy to evaluate but hard to sample from ([[Probability Density Distillation]]); this is used to model the posterior in [[Variational Autoencoder|VAEs]].[^9]

[^1]: [Prince, p. 304](zotero://open-pdf/library/items/BWT7FYX5?page=318&annotation=LQQ53SU5); [Prince, p. 304](zotero://open-pdf/library/items/BWT7FYX5?page=318&annotation=7XDC5YVX); [Prince, p. 306](zotero://open-pdf/library/items/BWT7FYX5?page=320&annotation=GACXEG7R); [Prince, p. 307](zotero://open-pdf/library/items/BWT7FYX5?page=321&annotation=ZNN4BIF2)
[^2]: [Prince, p. 304](zotero://open-pdf/library/items/BWT7FYX5?page=318&annotation=4JQE5LV3); [Prince, p. 306](zotero://open-pdf/library/items/BWT7FYX5?page=320&annotation=G82RBVIN)
[^3]: [Prince, p. 308](zotero://open-pdf/library/items/BWT7FYX5?page=322&annotation=YSAE6X42); [Prince, p. 309](zotero://open-pdf/library/items/BWT7FYX5?page=323&annotation=QVNXSGGB)
[^4]: [Prince, p. 307](zotero://open-pdf/library/items/BWT7FYX5?page=321&annotation=4FD2FZUC); [Prince, p. 309](zotero://open-pdf/library/items/BWT7FYX5?page=323&annotation=QVNXSGGB); [Prince, p. 309](zotero://open-pdf/library/items/BWT7FYX5?page=323&annotation=4WRIS5M4)
[^5]: [Prince, p. 309](zotero://open-pdf/library/items/BWT7FYX5?page=323&annotation=JDF9KBXS)
[^6]: [Prince, p. 317](zotero://open-pdf/library/items/BWT7FYX5?page=331&annotation=M7D3HJB3)
[^7]: [Prince, p. 318](zotero://open-pdf/library/items/BWT7FYX5?page=332&annotation=SDJ3QHGK); [Prince, p. 319](zotero://open-pdf/library/items/BWT7FYX5?page=333&annotation=VGV3I2GI); [Prince, p. 319](zotero://open-pdf/library/items/BWT7FYX5?page=333&annotation=TSQ29N5R)
[^8]: [Prince, p. 321](zotero://open-pdf/library/items/BWT7FYX5?page=335&annotation=T72FYWG2)
[^9]: [Prince, p. 321](zotero://open-pdf/library/items/BWT7FYX5?page=335&annotation=JFADEZRS); [Prince, p. 321](zotero://open-pdf/library/items/BWT7FYX5?page=335&annotation=69BRXLVQ)
