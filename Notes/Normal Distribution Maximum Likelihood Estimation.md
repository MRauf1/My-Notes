---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!abstract] Maximum Likelihood for the Univariate Gaussian[^1][^2]
> For [[Independent and Identically Distributed|i.i.d.]] observations $\mathbf{x} = (x_1, \dots, x_N)^T$ from $\mathcal{N}(x | \mu, \sigma^2)$, the [[Log-Likelihood Function|log likelihood]] is
> $$
> \begin{align}
> \ln p(\mathbf{x} | \mu, \sigma^2) = -\frac{1}{2\sigma^2}\sum_{n=1}^N (x_n - \mu)^2 - \frac{N}{2}\ln \sigma^2 - \frac{N}{2}\ln(2\pi)
> \end{align}
> $$
> and its joint maximizers are the sample mean and the sample variance about the sample mean:
> $$
> \begin{align}
> \mu_{\mathrm{ML}} = \frac{1}{N}\sum_{n=1}^N x_n, \qquad \sigma^2_{\mathrm{ML}} = \frac{1}{N}\sum_{n=1}^N (x_n - \mu_{\mathrm{ML}})^2
> \end{align}
> $$

> [!abstract] Bias of the Maximum Likelihood Variance[^3][^4]
> Taking expectations over data sets drawn from $\mathcal{N}(\mu, \sigma^2)$,
> $$
> \begin{align}
> \mathbb{E}[\mu_{\mathrm{ML}}] = \mu, \qquad \mathbb{E}[\sigma^2_{\mathrm{ML}}] = \left(\frac{N-1}{N}\right)\sigma^2
> \end{align}
> $$
> so maximum likelihood systematically underestimates the variance, and the [[Unbiased Estimator|unbiased]] estimate is
> $$
> \begin{align}
> \tilde{\sigma}^2 = \frac{N}{N-1}\sigma^2_{\mathrm{ML}} = \frac{1}{N-1}\sum_{n=1}^N (x_n - \mu_{\mathrm{ML}})^2
> \end{align}
> $$

# Types
- **Multivariate Gaussian** (general case): for $\mathcal{N}(\mathbf{x} | \boldsymbol{\mu}, \boldsymbol{\Sigma})$, $\boldsymbol{\mu}_{\mathrm{ML}} = \frac{1}{N}\sum_n \mathbf{x}_n$ and $\boldsymbol{\Sigma}_{\mathrm{ML}} = \frac{1}{N}\sum_n (\mathbf{x}_n - \boldsymbol{\mu}_{\mathrm{ML}})(\mathbf{x}_n - \boldsymbol{\mu}_{\mathrm{ML}})^T$, with the same bias $\mathbb{E}[\boldsymbol{\Sigma}_{\mathrm{ML}}] = \frac{N-1}{N}\boldsymbol{\Sigma}$ ([[Multivariate Normal Distribution]], [[Covariance Matrix]]).

# Properties
- Although the maximization is joint, the solution for $\mu$ decouples from that for $\sigma^2$: evaluate $\mu_{\mathrm{ML}}$ first ([[Sample Mean]]), then use it in $\sigma^2_{\mathrm{ML}}$.[^2]
- The bias arises because the variance is measured about $\mu_{\mathrm{ML}}$, which was fitted to the same data, rather than about the true $\mu$; see [[Sample Variance]] for the frequentist derivation of the $N - 1$ correction.
- The bias vanishes as $N \to \infty$ and is negligible for anything but small $N$; for complex models with many parameters, the analogous bias of maximum likelihood is far more severe and lies at the root of [[Overfitting|over-fitting]].[^4]
- Maximizing the log rather than the likelihood is equivalent since $\ln$ is monotonically increasing, simplifies the algebra, and avoids numerical underflow of a product of many small probabilities.[^5]

[^1]: [Bishop, 2006, p. 27](zotero://open-pdf/library/items/5G99AZ8U?page=47&annotation=TUHT7IY9)
[^2]: [Bishop, 2006, p. 27](zotero://open-pdf/library/items/5G99AZ8U?page=47&annotation=C4G96HFT)
[^3]: [Bishop, 2006, p. 27](zotero://open-pdf/library/items/5G99AZ8U?page=47&annotation=WMA8AAYH)
[^4]: [Bishop, 2006, p. 28](zotero://open-pdf/library/items/5G99AZ8U?page=48&annotation=4SIQ5ISY)
[^5]: [Bishop, 2006, p. 26](zotero://open-pdf/library/items/5G99AZ8U?page=46&annotation=8E3NKN4J)
