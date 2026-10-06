---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Diffusion Model Loss Function[^1][^2][^3]
> For a [[Diffusion Model|diffusion model]] with fixed encoder $q(\mathbf{z}_{1\dots T}|\mathbf{x})$, the [[Evidence Lower Bound]] simplifies to
> $$
> \begin{align}
> \mathrm{ELBO}[\boldsymbol{\phi}_{1\dots T}] &= \int q(\mathbf{z}_{1\dots T}|\mathbf{x})\log\left[\frac{Pr(\mathbf{x}, \mathbf{z}_{1\dots T}|\boldsymbol{\phi}_{1\dots T})}{q(\mathbf{z}_{1\dots T}|\mathbf{x})}\right]d\mathbf{z}_{1\dots T} \\
> &\approx \mathbb{E}_{q(\mathbf{z}_1|\mathbf{x})}\left[\log Pr(\mathbf{x}|\mathbf{z}_1, \boldsymbol{\phi}_1)\right] - \sum_{t=2}^T \mathbb{E}_{q(\mathbf{z}_t|\mathbf{x})}\left[D_{KL}\left[q(\mathbf{z}_{t-1}|\mathbf{z}_t, \mathbf{x}) \,\|\, Pr(\mathbf{z}_{t-1}|\mathbf{z}_t, \boldsymbol{\phi}_t)\right]\right]
> \end{align}
> $$
> a reconstruction term (as in the [[Variational Autoencoder|VAE]]) plus [[Kullback-Leibler Divergence|KL divergences]] between the [[Conditional Diffusion Distribution|conditional diffusion distribution]] and the decoder steps. Both are normal, so each KL is $\frac{1}{2\sigma_t^2}\|\boldsymbol{\mu}_q - \mathbf{f}_t[\mathbf{z}_t, \boldsymbol{\phi}_t]\|^2 + C$. Negating and using one [[Monte Carlo Estimator|Monte Carlo]] sample $\mathbf{z}_{it}$ per example gives
> $$
> \begin{align}
> L[\boldsymbol{\phi}_{1\dots T}] = \sum_{i=1}^I \Bigg(\underbrace{-\log\mathrm{Norm}_{\mathbf{x}_i}\left[\mathbf{f}_1[\mathbf{z}_{i1}, \boldsymbol{\phi}_1], \sigma_1^2\mathbf{I}\right]}_{\text{reconstruction}} + \sum_{t=2}^T \frac{1}{2\sigma_t^2}\Big\|\underbrace{\frac{1-\alpha_{t-1}}{1-\alpha_t}\sqrt{1-\beta_t}\,\mathbf{z}_{it} + \frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x}_i}_{\text{target: mean of } q(\mathbf{z}_{t-1}|\mathbf{z}_t, \mathbf{x})} - \underbrace{\mathbf{f}_t[\mathbf{z}_{it}, \boldsymbol{\phi}_t]}_{\text{predicted } \mathbf{z}_{t-1}}\Big\|^2\Bigg)
> \end{align}
> $$
> Each network is trained to predict the most likely previous latent given the ground-truth clean data.

> [!abstract] Noise-Prediction Parameterization[^4][^5]
> Substituting $\mathbf{x} = (\mathbf{z}_t - \sqrt{1-\alpha_t}\,\boldsymbol{\epsilon})/\sqrt{\alpha_t}$ from the [[Diffusion Kernel|diffusion kernel]], the target mean becomes $\frac{1}{\sqrt{1-\beta_t}}\mathbf{z}_t - \frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\boldsymbol{\epsilon}$. Replacing the model $\hat{\mathbf{z}}_{t-1} = \mathbf{f}_t$ with a network $\hat{\boldsymbol{\epsilon}} = \mathbf{g}_t[\mathbf{z}_t, \boldsymbol{\phi}_t]$ that predicts the mixed-in noise,
> $$
> \begin{align}
> \mathbf{f}_t[\mathbf{z}_t, \boldsymbol{\phi}_t] = \frac{1}{\sqrt{1-\beta_t}}\mathbf{z}_t - \frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{g}_t[\mathbf{z}_t, \boldsymbol{\phi}_t]
> \end{align}
> $$
> the loss (with the reconstruction term treated likewise and constants dropped) becomes
> $$
> \begin{align}
> L[\boldsymbol{\phi}_{1\dots T}] = \sum_{i=1}^I\sum_{t=1}^T \frac{\beta_t^2}{(1-\alpha_t)(1-\beta_t)2\sigma_t^2}\left\|\mathbf{g}_t[\mathbf{z}_{it}, \boldsymbol{\phi}_t] - \boldsymbol{\epsilon}_{it}\right\|^2
> \end{align}
> $$
> In practice the per-step weights are dropped, giving the simple loss
> $$
> \begin{align}
> L[\boldsymbol{\phi}_{1\dots T}] = \sum_{i=1}^I\sum_{t=1}^T \left\|\mathbf{g}_t\left[\sqrt{\alpha_t}\,\mathbf{x}_i + \sqrt{1-\alpha_t}\,\boldsymbol{\epsilon}_{it}, \boldsymbol{\phi}_t\right] - \boldsymbol{\epsilon}_{it}\right\|^2
> \end{align}
> $$

# Properties
- **Training** (algorithm 18.1, see [[Diffusion Model]]): for each example draw $t \sim \mathrm{Uniform}[1, \dots, T]$ and $\boldsymbol{\epsilon} \sim \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$, form $\mathbf{z}_t$ in one shot with the diffusion kernel, and regress $\boldsymbol{\epsilon}$; no simulation of the chain is needed.[^5]
- **Sampling** (algorithm 18.2): from $\mathbf{z}_T \sim \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$, set $\hat{\mathbf{z}}_{t-1} = \mathbf{f}_t[\mathbf{z}_t, \boldsymbol{\phi}_t]$ using $\mathbf{g}_t$ and add noise, $\mathbf{z}_{t-1} = \hat{\mathbf{z}}_{t-1} + \sigma_t\boldsymbol{\epsilon}$, for $t = T, \dots, 2$; the final step to $\mathbf{x}$ adds no noise.
- The noise parameterization works better in practice than predicting $\mathbf{z}_{t-1}$ directly; dropping the weights reweights the ELBO toward the harder, noisier steps, trading likelihood for sample quality (Ho et al., 2020).[^4]
- **Denoising score matching**: since $\nabla_{\mathbf{z}_t}\log q(\mathbf{z}_t|\mathbf{x}) = -\boldsymbol{\epsilon}/\sqrt{1-\alpha_t}$, the minimizer satisfies $\mathbf{g}_t[\mathbf{z}_t] = -\sqrt{1-\alpha_t}\,\nabla\log q(\mathbf{z}_t)$, so the network learns the score of the noisy marginal (Vincent, 2011; Song et al., 2021). The sampling mean is then $\frac{1}{\sqrt{1-\beta_t}}\left(\mathbf{z}_t + \beta_t\nabla\log q(\mathbf{z}_t)\right)$, a small gradient-ascent step on the log-density, as in [[Metropolis-Adjusted Langevin Algorithm|Langevin dynamics]].
- **Tweedie's formula**: equivalently $\mathbb{E}[\mathbf{x}|\mathbf{z}_t] = (\mathbf{z}_t - \sqrt{1-\alpha_t}\,\mathbb{E}[\boldsymbol{\epsilon}|\mathbf{z}_t])/\sqrt{\alpha_t}$, so a noise predictor is also a minimum-MSE denoiser.
- **Shared network**: in practice one network $\mathbf{g}[\mathbf{z}_t, t, \boldsymbol{\phi}]$ (a [[U-Net]] with a time embedding) serves all steps.
- Depends on the forward process only through the diffusion kernel, so it trains a whole family of compatible processes, including [[Denoising Diffusion Implicit Model|DDIM]].[^6]

[^1]: [Prince, p. 358](zotero://open-pdf/library/items/BWT7FYX5?page=372&annotation=K5EW6YDN); [Prince, p. 359](zotero://open-pdf/library/items/BWT7FYX5?page=373&annotation=EUFGM3FV); [Prince, p. 359](zotero://open-pdf/library/items/BWT7FYX5?page=373&annotation=HQT5378B)
[^2]: [Prince, p. 359](zotero://open-pdf/library/items/BWT7FYX5?page=373&annotation=SR9J632F)
[^3]: [Prince, p. 360](zotero://open-pdf/library/items/BWT7FYX5?page=374&annotation=UTMXEDZ3); [Prince, p. 361](zotero://open-pdf/library/items/BWT7FYX5?page=375&annotation=4BVZZL2M)
[^4]: [Prince, p. 361](zotero://open-pdf/library/items/BWT7FYX5?page=375&annotation=WJIS2WXR); [Prince, p. 362](zotero://open-pdf/library/items/BWT7FYX5?page=376&annotation=Q7HTFQZU); [Prince, p. 362](zotero://open-pdf/library/items/BWT7FYX5?page=376&annotation=EXVKM8MC)
[^5]: [Prince, p. 363](zotero://open-pdf/library/items/BWT7FYX5?page=377&annotation=KX3PKUPD); [Prince, p. 364](zotero://open-pdf/library/items/BWT7FYX5?page=378&annotation=G9QGMTCE)
[^6]: [Prince, p. 364](zotero://open-pdf/library/items/BWT7FYX5?page=378&annotation=TIIGX58K); [Prince, p. 365](zotero://open-pdf/library/items/BWT7FYX5?page=379&annotation=D7TIBGCS)
