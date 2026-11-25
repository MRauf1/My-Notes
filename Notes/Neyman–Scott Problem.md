---
tags:
  - statistics
  - mathematical_statistics
  - cryoEM
---

# Definition
> [!info] Neyman–Scott Problem[^1]
> Let $X_{ij} \sim \mathcal{N}(\mu_i, \sigma^2)$ be independent, for $i = 1, \dots, n$ and $j = 1, 2$, with unknown $\mu_1, \dots, \mu_n$ (incidental parameters) and $\sigma^2$ (the structural parameter). The joint [[Maximum Likelihood Estimation|MLE]] of $\sigma^2$ is
> $$
> \begin{align}
> \hat\sigma^2 = \frac{1}{2n}\sum_{i=1}^n \sum_{j=1}^2 (X_{ij} - \bar X_i)^2 \xrightarrow{\text{a.s.}} \frac{\sigma^2}{2},
> \end{align}
> $$
> so it is not a [[Consistent Estimator|consistent estimator]]. The MLE's consistency and efficiency require the number of parameters to stay fixed as the data grow, and here it grows with $n$.

# Properties
- **Remedy: remove the incidental parameters before maximizing**, by marginalizing or conditioning. For instance, $X_{i1} - X_{i2} \sim \mathcal{N}(0, 2\sigma^2)$ does not involve $\mu_i$, and the MLE based on these differences is consistent.
- In cryo-EM, maximizing the likelihood jointly over the structure and all per-image poses has the same defect. The correct estimator marginalizes the poses ([[Cryo-EM Maximum Likelihood Reconstruction]]).

# Questions
> [!question]- Derive the limit $\sigma^2/2$.
> With two observations, $\sum_j (X_{ij} - \bar X_i)^2 = (X_{i1} - X_{i2})^2/2$. Since $X_{i1} - X_{i2} \sim \mathcal{N}(0, 2\sigma^2)$, this has mean $\sigma^2$. So $\hat\sigma^2 = \frac{1}{2n}\sum_i (X_{i1} - X_{i2})^2/2$, and by the strong law of large numbers it converges to $\frac{1}{4}\cdot 2\sigma^2 = \sigma^2/2$. Each $\mu_i$ is fitted from 2 points and absorbs one degree of freedom of the 2, which is never corrected as $n \to \infty$.

> [!question]- Connection: How does joint pose–structure maximum likelihood in cryo-EM map onto the Neyman–Scott problem, and where does the analogy break?
> The dictionary:
> - the incidental means $\mu_i$ correspond to the per-image poses $R_i$ (one new nuisance parameter per observation);
> - the structural parameter $\sigma^2$ corresponds to the map $\varphi$;
> - the fix of marginalizing $\mu_i$ corresponds to integrating each $R_i$ over $SO(3)$.
>
> In both, the parameter count grows with the data, which voids the MLE's consistency guarantee. **Where it breaks:** in Neyman–Scott the bias has a closed form ($\sigma^2/2$). In cryo-EM, joint maximization ("hard assignment") is often nearly harmless at high SNR, where the pose posterior is sharply peaked. Its failure shows mainly at low SNR, as overfitting and model bias.

[^1]: [Singer and Sigworth, 2020, p. 14](zotero://open-pdf/library/items/FKVQSKD6?page=14&annotation=X26H6JE5)
