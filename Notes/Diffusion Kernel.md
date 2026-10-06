---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Diffusion Kernel[^1][^2]
> The closed-form distribution of the latent $\mathbf{z}_t$ of the [[Diffusion Forward Process|diffusion forward process]] given the starting data point $\mathbf{x}$:
> $$
> \begin{align}
> \mathbf{z}_t &= \sqrt{\alpha_t}\cdot\mathbf{x} + \sqrt{1-\alpha_t}\cdot\boldsymbol{\epsilon}, \qquad \boldsymbol{\epsilon} \sim \mathrm{Norm}[\mathbf{0}, \mathbf{I}] \\
> q(\mathbf{z}_t|\mathbf{x}) &= \mathrm{Norm}_{\mathbf{z}_t}\left[\sqrt{\alpha_t}\cdot\mathbf{x}, (1-\alpha_t)\mathbf{I}\right], \qquad \alpha_t = \prod_{s=1}^t (1-\beta_s)
> \end{align}
> $$
> *Derivation.* Substituting $\mathbf{z}_1$ into $\mathbf{z}_2$ gives $\mathbf{z}_2 = \sqrt{(1-\beta_2)(1-\beta_1)}\,\mathbf{x} + \sqrt{1-\beta_2}\sqrt{\beta_1}\,\boldsymbol{\epsilon}_1 + \sqrt{\beta_2}\,\boldsymbol{\epsilon}_2$. The two noise terms are independent normals, so their sum is normal with variance $(1-\beta_2)\beta_1 + \beta_2 = 1 - (1-\beta_1)(1-\beta_2)$ ([[Normal Distribution Linear Combination]]). Induction on $t$ gives the result.

(Prince writes $\alpha_t$ for what Ho et al. (2020) call $\bar{\alpha}_t$.)

# Properties
- Allows drawing $\mathbf{z}_t$ for any $t$ directly from $\mathbf{x}$, without simulating $\mathbf{z}_1, \dots, \mathbf{z}_{t-1}$; this makes training efficient since many $(t, \mathbf{z}_t)$ pairs are needed per example ([[Diffusion Model Loss Function]]).[^1]
- $\alpha_t$ decreases monotonically from $\approx 1$ to $\approx 0$, so the signal-to-noise ratio $\alpha_t / (1-\alpha_t)$ decreases with $t$ and $q(\mathbf{z}_T|\mathbf{x}) \to \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$ regardless of $\mathbf{x}$.
- **Diffused marginal**: marginalizing the joint $q(\mathbf{z}_{1\dots t}, \mathbf{x})$ over everything except $\mathbf{z}_t$ reduces, via the kernel, to[^3]
$$
\begin{align}
q(\mathbf{z}_t) = \iint q(\mathbf{z}_{1\dots t}|\mathbf{x})Pr(\mathbf{x})\,d\mathbf{z}_{1\dots t-1}\,d\mathbf{x} = \int q(\mathbf{z}_t|\mathbf{x})Pr(\mathbf{x})\,d\mathbf{x}
\end{align}
$$
  i.e. the data distribution, shrunk by $\sqrt{\alpha_t}$, convolved with an isotropic Gaussian: a continuous [[Mixture of Gaussians|mixture of Gaussians]]. It has no closed form because $Pr(\mathbf{x})$ is unknown.
- Since $q(\mathbf{z}_{t-1}|\mathbf{x})$ is normal, the reverse step becomes tractable once $\mathbf{x}$ is known ([[Conditional Diffusion Distribution]]).
- **Score of the kernel**: $\nabla_{\mathbf{z}_t}\log q(\mathbf{z}_t|\mathbf{x}) = -\boldsymbol{\epsilon}/\sqrt{1-\alpha_t}$, so predicting the noise is (up to scale) estimating the score of $q(\mathbf{z}_t)$ (Vincent, 2011).
- The loss of [[Diffusion Model Loss Function|noise prediction]] depends on the forward process only through this kernel, so any forward process with the same kernel is trained identically ([[Denoising Diffusion Implicit Model]]).[^4]

[^1]: [Prince, p. 353](zotero://open-pdf/library/items/BWT7FYX5?page=367&annotation=UB988TDA)
[^2]: [Prince, p. 353](zotero://open-pdf/library/items/BWT7FYX5?page=367&annotation=XUX4VPAW)
[^3]: [Prince, p. 353](zotero://open-pdf/library/items/BWT7FYX5?page=367&annotation=HNV3N93I); [Prince, p. 354](zotero://open-pdf/library/items/BWT7FYX5?page=368&annotation=MF65FGPE)
[^4]: [Prince, p. 364](zotero://open-pdf/library/items/BWT7FYX5?page=378&annotation=TIIGX58K)
