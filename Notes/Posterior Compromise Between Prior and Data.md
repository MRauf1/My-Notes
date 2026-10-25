---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Posterior Compromise Between Prior and Data[^1]
> The [[Posterior Distribution]] is centered at a point that is a compromise between the prior information and the data. The compromise is controlled to a greater extent by the data as the sample size increases, and in the limit the parameters of the [[Prior Distribution]] have no influence on the posterior.

> [!abstract] Gaussian Form (Precision Weighting)[^2][^3]
> For $y_1, \dots, y_n \overset{\text{iid}}{\sim} N(\theta, \sigma^2)$ with $\sigma^2$ known and prior $\theta \sim N(\mu_0, \tau_0^2)$, the posterior is $N(\mu_n, \tau_n^2)$ with
> $$
> \begin{align}
> \mu_n = \frac{\frac{1}{\tau_0^2}\mu_0 + \frac{n}{\sigma^2}\bar{y}}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}}, \qquad \frac{1}{\tau_n^2} = \frac{1}{\tau_0^2} + \frac{n}{\sigma^2}
> \end{align}
> $$
> The posterior mean is a weighted average of prior mean and data, with weights equal to their [[Precision (Statistics)|precisions]]; the posterior precision is their sum.

For $n = 1$ the posterior mean can be read three equivalent ways:[^4]
$$
\begin{align}
\mu_1 &= \frac{\frac{1}{\tau_0^2}\mu_0 + \frac{1}{\sigma^2}y}{\frac{1}{\tau_0^2} + \frac{1}{\sigma^2}} && \text{(precision-weighted average)} \\
&= \mu_0 + (y - \mu_0)\frac{\tau_0^2}{\sigma^2 + \tau_0^2} && \text{(prior adjusted toward the data)} \\
&= y - (y - \mu_0)\frac{\sigma^2}{\sigma^2 + \tau_0^2} && \text{(data shrunk toward the prior)}
\end{align}
$$

# Properties
- Extremes:[^5] if $\tau_0^2 = 0$ the prior is infinitely more precise than the data and the posterior equals the prior (concentrated at $\mu_0$); if $\sigma^2 = 0$ the data are perfectly precise and the posterior concentrates at $y$; if $y = \mu_0$ the posterior mean sits at that common value.
- **Prior as pseudo-data.** Prior precision $1/\tau_0^2$ and data precision $n/\sigma^2$ play equivalent roles; if $\tau_0^2 = \sigma^2$, the prior has the weight of one extra observation at $\mu_0$.[^6] More generally, [[Conjugate Prior|conjugate priors]] can be read as additional data.
- **Prior washes out.** As $\tau_0 \to \infty$ with $n$ fixed, or $n \to \infty$ with $\tau_0^2$ fixed, $p(\theta \mid y) \approx N(\theta \mid \bar{y}, \sigma^2/n)$. This is a good approximation whenever the prior is diffuse over the range where the likelihood is substantial.[^6] The general asymptotic statement is the [[Bernstein-von Mises Theorem]].
- The posterior variance shrinks at rate $1/n$ in regular models.[^7]
- On average the posterior is less variable than the prior ([[Prior and Posterior Moment Relations]]).
- **Sequential updating** gives the same result: adding $y_1, \dots, y_n$ one at a time, with each posterior serving as the prior for the next observation, yields the same posterior as processing all data at once.[^3]

[^1]: [Gelman et al., p. 32](zotero://open-pdf/library/items/HDF44SF4?page=42&annotation=HKJ4N6MY)
[^2]: [Gelman et al., p. 41](zotero://open-pdf/library/items/HDF44SF4?page=51&annotation=YMSCDW7Q)
[^3]: [Gelman et al., p. 42](zotero://open-pdf/library/items/HDF44SF4?page=52&annotation=LL6W7MPC)
[^4]: [Gelman et al., p. 40](zotero://open-pdf/library/items/HDF44SF4?page=50&annotation=DG3R4UTC)
[^5]: [Gelman et al., p. 40](zotero://open-pdf/library/items/HDF44SF4?page=50&annotation=3JUAXN6F)
[^6]: [Gelman et al., p. 42](zotero://open-pdf/library/items/HDF44SF4?page=52&annotation=IQIWFYVK)
[^7]: [Gelman et al., p. 35](zotero://open-pdf/library/items/HDF44SF4?page=45&annotation=D7LUMWCH)
