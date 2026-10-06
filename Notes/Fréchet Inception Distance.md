---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Fréchet Inception Distance (FID)[^1][^2]
> A symmetric distance between the distributions of real and generated images. Each distribution is approximated by a [[Multivariate Normal Distribution|multivariate Gaussian]] fitted to the deepest-layer activations of the Inception classification network, with means $\boldsymbol{\mu}_r, \boldsymbol{\mu}_g$ and covariances $\boldsymbol{\Sigma}_r, \boldsymbol{\Sigma}_g$, and the distance between them is the Fréchet distance:
> $$
> \begin{align}
> \text{FID} = \|\boldsymbol{\mu}_r - \boldsymbol{\mu}_g\|_2^2 + \operatorname{Tr}\left[\boldsymbol{\Sigma}_r + \boldsymbol{\Sigma}_g - 2\left(\boldsymbol{\Sigma}_r \boldsymbol{\Sigma}_g\right)^{1/2}\right]
> \end{align}
> $$

# Properties
- **General case**: the Fréchet distance between distributions $p, q$ is the 2-Wasserstein distance $W_2(p, q)^2 = \inf_{\gamma \in \Gamma(p, q)} \mathbb{E}_{(\mathbf{a}, \mathbf{b}) \sim \gamma}\|\mathbf{a} - \mathbf{b}\|^2$ over couplings $\gamma$; for Gaussians it has the closed form above ([[Trace]], [[Matrix Square Root]]).
- The Gaussian approximation is unavoidable since characterizing either distribution exactly is precisely the job of the [[Generative Model|generative model]].[^1]
- The comparison is made in a feature space of units most associated with object classes, so it operates at a semantic level and ignores fine-grained image detail.[^2]
- Unlike the [[Inception Score]], it accounts for within-class diversity.
- Relies on what the Inception features retain: discarded information, which may matter for realism, does not contribute.
- Sensitive to both realism and diversity but does not separate them; [[Manifold Precision and Recall]] does.[^3]
- Lower is better.

[^1]: [Prince, p. 273](zotero://open-pdf/library/items/BWT7FYX5?page=287&annotation=MFCGQUJT)
[^2]: [Prince, p. 274](zotero://open-pdf/library/items/BWT7FYX5?page=288&annotation=5U2JGI6R)
[^3]: [Prince, p. 274](zotero://open-pdf/library/items/BWT7FYX5?page=288&annotation=BIPZK5JQ)
