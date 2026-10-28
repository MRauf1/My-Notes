---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Predictive Distribution[^1][^2]
> The probability distribution over the target $t$ for a new input $\mathbf{x}$, given the training data $\mathbf{X}, \mathbf{t}$. A fully Bayesian treatment obtains it by consistently applying the sum and product rules, marginalizing over the parameters with respect to their posterior:
> $$
> \begin{align}
> p(t | \mathbf{x}, \mathbf{X}, \mathbf{t}) = \int p(t | \mathbf{x}, \mathbf{w})\, p(\mathbf{w} | \mathbf{X}, \mathbf{t})\, d\mathbf{w}
> \end{align}
> $$

A point-estimate method instead plugs in a single parameter value, e.g. $p(t | \mathbf{x}, \mathbf{w}_{\mathrm{ML}}, \beta_{\mathrm{ML}}) = \mathcal{N}(t | y(\mathbf{x}, \mathbf{w}_{\mathrm{ML}}), \beta_{\mathrm{ML}}^{-1})$ ([[Probabilistic Formulation of Regression]]). Including a prior but still maximizing ([[Maximum a Posteriori Learning|MAP]]) remains a point estimate and is not yet Bayesian; marginalizations like the integral above lie at the heart of Bayesian methods.[^3]

> [!abstract] Bayesian [[Linear Model]] Predictive Distribution[^2]
> For $y(\mathbf{x}, \mathbf{w}) = \mathbf{w}^T\boldsymbol{\phi}(\mathbf{x})$ with Gaussian noise of known precision $\beta$ and prior $\mathcal{N}(\mathbf{w} | \mathbf{0}, \alpha^{-1}\mathbf{I})$, the posterior is Gaussian and the predictive distribution is analytically
> $$
> \begin{align}
> p(t | \mathbf{x}, \mathbf{X}, \mathbf{t}) &= \mathcal{N}\big(t \,|\, m(\mathbf{x}), s^2(\mathbf{x})\big) \\
> m(\mathbf{x}) &= \beta\,\boldsymbol{\phi}(\mathbf{x})^T\mathbf{S}\sum_{n=1}^N \boldsymbol{\phi}(\mathbf{x}_n)\, t_n \\
> s^2(\mathbf{x}) &= \beta^{-1} + \boldsymbol{\phi}(\mathbf{x})^T\mathbf{S}\,\boldsymbol{\phi}(\mathbf{x}) \\
> \mathbf{S}^{-1} &= \alpha\mathbf{I} + \beta\sum_{n=1}^N \boldsymbol{\phi}(\mathbf{x}_n)\boldsymbol{\phi}(\mathbf{x}_n)^T
> \end{align}
> $$
> For polynomial curve fitting, $\phi_i(x) = x^i$ for $i = 0, \dots, M$.

> [!info] Posterior Predictive Distribution[^5][^7]
> For a future observation $\tilde{y}$ given observed data $y$,
> $$
> \begin{align}
> p(\tilde{y} \mid y) = \int p(\tilde{y} \mid \theta, y)\, p(\theta \mid y)\, d\theta = \int p(\tilde{y} \mid \theta)\, p(\theta \mid y)\, d\theta
> \end{align}
> $$

**Why $p(\tilde{y} \mid \theta, y) = p(\tilde{y} \mid \theta)$.**[^8] This is a modeling assumption, not an identity. The future $\tilde{y}$ is taken to be [[Exchangeability|exchangeable]] with the past $y$, which is modeled as all observations being iid given $\theta$, i.e. $\tilde{y}$ and $y$ are conditionally independent given $\theta$:
$$
\begin{align}
p(\tilde{y}, y \mid \theta) = p(\tilde{y} \mid \theta)\, p(y \mid \theta) \implies p(\tilde{y} \mid \theta, y) = \frac{p(\tilde{y}, y \mid \theta)}{p(y \mid \theta)} = p(\tilde{y} \mid \theta)
\end{align}
$$
The parameter is the entire channel through which past data inform the future: once $\theta$ is known, $y$ carries nothing further about $\tilde{y}$. Marginally, $\tilde{y}$ and $y$ are **dependent** ($p(\tilde{y} \mid y) \neq p(\tilde{y})$), and all the learning happens by $y$ reshaping $p(\theta \mid y)$. The assumption fails when the data have structure beyond $\theta$ (time series, spatial dependence, covariates for $\tilde{y}$), and then $p(\tilde{y} \mid \theta, y)$ must be modeled explicitly.

**Generative view.**[^10] The joint factorizes by the chain rule as $p(y, \tilde{y}, \theta) = p(\tilde{y} \mid y, \theta)\, p(y \mid \theta)\, p(\theta)$. In a parametric model, $\theta$ represents the entire data-generating mechanism, so given $\theta$ it is a complete bottleneck between past and future and the first factor reduces to $p(\tilde{y} \mid \theta)$. The predictive integral then follows from marginalizing $\theta$:
$$
\begin{align}
p(\tilde{y} \mid y) = \int p(\tilde{y}, \theta \mid y)\, d\theta = \int p(\tilde{y} \mid \theta, y)\, p(\theta \mid y)\, d\theta = \int p(\tilde{y} \mid \theta)\, p(\theta \mid y)\, d\theta
\end{align}
$$

**"iid" does not mean $p(\tilde{y} \mid y) = p(\tilde{y})$.**[^10] In the Bayesian framework "iid" means **conditionally** iid given $\theta$. Since $\theta$ is unknown, integrating it out couples $y$ and $\tilde{y}$ through their shared dependence on $\theta$, so they are **marginally dependent**. Information flows along the chain
$$
\begin{align}
y \longrightarrow \theta \longrightarrow \tilde{y}
\end{align}
$$
$y$ updates beliefs about $\theta$ (prior $\to$ posterior), and $\theta$ governs $\tilde{y}$. Comparing
$$
\begin{align}
p(\tilde{y}) = \int p(\tilde{y} \mid \theta)\, p(\theta)\, d\theta \qquad \text{vs} \qquad p(\tilde{y} \mid y) = \int p(\tilde{y} \mid \theta)\, p(\theta \mid y)\, d\theta
\end{align}
$$
([[Prior Predictive Distribution]] vs posterior predictive), the two differ exactly because $p(\theta \mid y) \neq p(\theta)$. If $p(\tilde{y} \mid y) = p(\tilde{y})$ held, past data would say nothing about the future and learning would be impossible. Independence holds only while $\theta$ is held fixed.

> [!example]- Bag of Coins
> One of two coins is picked at random: fair ($P(H) = 0.5$) or biased ($P(H) = 0.9$), so $\theta \in \{\text{fair}, \text{biased}\}$. Ten flips give ten heads.
> - **Given $\theta$**: if told "it is the fair coin", the prediction for flip 11 reverts to $0.5$, ignoring the ten heads (conditional independence).
> - **Without $\theta$**: the ten heads shift the posterior strongly toward the biased coin, so the prediction for flip 11 moves toward heads (marginal dependence).

> [!abstract] Posterior Predictive Mean and Variance[^9]
> By the [[Law of Total Expectation]] and [[Law of Total Variance]] conditional on $y$,
> $$
> \begin{align}
> E(\tilde{y} \mid y) &= E\big(E(\tilde{y} \mid \theta, y) \mid y\big) \\
> \text{var}(\tilde{y} \mid y) &= \underbrace{E\big(\text{var}(\tilde{y} \mid \theta, y) \mid y\big)}_{\text{sampling variance}} + \underbrace{\text{var}\big(E(\tilde{y} \mid \theta, y) \mid y\big)}_{\text{posterior uncertainty in } \theta}
> \end{align}
> $$
> E.g. for a normal model with known $\sigma^2$ and posterior $N(\mu_1, \tau_1^2)$: mean $\mu_1$, variance $\sigma^2 + \tau_1^2$.

# Properties
- **Bayesian approach for neural networks** (Prince): maximum likelihood is overconfident, choosing the single most likely parameters although many are broadly compatible with the data. The Bayesian approach computes $Pr(\boldsymbol{\phi} | \{\mathbf{x}_i, \mathbf{y}_i\}) \propto \prod_i Pr(\mathbf{y}_i | \mathbf{x}_i, \boldsymbol{\phi}) Pr(\boldsymbol{\phi})$ and predicts $Pr(\mathbf{y} | \mathbf{x}, \{\mathbf{x}_i, \mathbf{y}_i\}) = \int Pr(\mathbf{y} | \mathbf{x}, \boldsymbol{\phi}) Pr(\boldsymbol{\phi} | \{\mathbf{x}_i, \mathbf{y}_i\}) d\boldsymbol{\phi}$, an infinite weighted [[Ensemble Learning|ensemble]] whose weights depend on the prior and on agreement with the data. It is elegant and more robust, but for neural networks the posterior cannot be represented or integrated exactly, so all practical methods approximate it, adding considerable complexity.[^6]
- Both the mean and the variance of the Bayesian predictive distribution depend on $\mathbf{x}$.[^4]
- The variance splits into two sources: $\beta^{-1}$ is the noise on the targets (already present in the maximum likelihood plug-in predictive), while $\boldsymbol{\phi}(\mathbf{x})^T\mathbf{S}\boldsymbol{\phi}(\mathbf{x})$ is the uncertainty in $\mathbf{w}$, which arises only from the Bayesian treatment and is largest where training data is sparse.[^4]
- Here $\alpha, \beta$ are fixed [[Hyperparameter|hyperparameters]]; a fuller treatment infers them from data as well.
- The mean $m(\mathbf{x})$ coincides with the prediction of the MAP (ridge) solution; the difference lies in the variance.
- General form (posterior predictive distribution): $p(\tilde{y} \mid y) = \int p(\tilde{y} \mid \theta)\, p(\theta \mid y)\, d\theta$, an average of conditional predictions over the [[Posterior Distribution]]; dropping $y$ from $p(\tilde{y} \mid \theta, y)$ uses the conditional independence of $y$ and $\tilde{y}$ given $\theta$. Its pre-data counterpart is the [[Prior Predictive Distribution]].[^5]
- With several parameters the average is over all of them, e.g. $p(\tilde{y} \mid y) = \iint p(\tilde{y} \mid \mu, \sigma^2, y)\, p(\mu, \sigma^2 \mid y)\, d\mu\, d\sigma^2$; it is simulated by drawing $\tilde{y}^s \sim p(\tilde{y} \mid \theta^s)$ for each posterior draw $\theta^s$ ([[Marginal Posterior Distribution]], [[Bayesian Posterior Simulation Strategy]]).[^11]
- Averaging over parameters rather than committing to one is what lets Bayesian models avoid [[Overfitting|over-fitting]] even when parameters outnumber data points.

[^1]: [Bishop, 2006, p. 31](zotero://open-pdf/library/items/5G99AZ8U?page=51&annotation=W4DVFWL2)
[^2]: [Bishop, 2006, p. 31](zotero://open-pdf/library/items/5G99AZ8U?page=51&annotation=FF38GDUR)
[^3]: [Bishop, 2006, p. 30](zotero://open-pdf/library/items/5G99AZ8U?page=50&annotation=84MJ5RRL)
[^4]: [Bishop, 2006, p. 31](zotero://open-pdf/library/items/5G99AZ8U?page=51&annotation=D9K9DJ8G)
[^5]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=5SYNH2BZ)
[^6]: [Prince, p. 150](zotero://open-pdf/library/items/BWT7FYX5?page=164&annotation=FIP4DUG2); [Prince, p. 150](zotero://open-pdf/library/items/BWT7FYX5?page=164&annotation=3LNCV3VC); [Prince, p. 151](zotero://open-pdf/library/items/BWT7FYX5?page=165&annotation=VN26RKRH)
[^7]: [Gelman et al., p. 41](zotero://open-pdf/library/items/HDF44SF4?page=51&annotation=FRGV6RK9)
[^8]: [Gelman et al., p. 41](zotero://open-pdf/library/items/HDF44SF4?page=51&annotation=3VYIG7K6)
[^9]: [Gelman et al., p. 41](zotero://open-pdf/library/items/HDF44SF4?page=51&annotation=DCAGDPZ5)
[^10]: Supplementary notes provided by the creator.
[^11]: [Gelman et al., p. 66](zotero://open-pdf/library/items/HDF44SF4?page=76&annotation=K27Y3WQ3)
