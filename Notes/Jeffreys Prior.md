---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Jeffreys Prior[^1]
> The [[Noninformative Prior]]
> $$
> \begin{align}
> p(\theta) \propto [J(\theta)]^{1/2}, \qquad J(\theta) = E\left[\left(\frac{d \log p(y \mid \theta)}{d\theta}\right)^2 \,\middle|\, \theta\right] = -E\left[\frac{d^2 \log p(y \mid \theta)}{d\theta^2} \,\middle|\, \theta\right]
> \end{align}
> $$
> where $J(\theta)$ is the [[Fisher Information]] for $\theta$.

> [!info] Jeffreys' Invariance Principle[^1]
> For a one-to-one reparameterization $\phi = h(\theta)$, the prior $p(\theta)$ expresses the same beliefs as
> $$
> \begin{align}
> p(\phi) = p(\theta)\left|\frac{d\theta}{d\phi}\right| = p(\theta)\,|h'(\theta)|^{-1}
> \end{align}
> $$
> Any rule for determining the prior should be consistent with this: applying the rule to $\theta$ and transforming must give the same result as applying the rule directly to the transformed model $p(y, \phi) = p(\phi)\,p(y \mid \phi)$.

**Invariance proof.**[^2] Evaluate $J(\phi)$ at $\theta = h^{-1}(\phi)$. By the chain rule (the extra term involving $d^2\theta/d\phi^2$ multiplies the [[Score Function|score]], whose expectation is zero),
$$
\begin{align}
J(\phi) = -E\left[\frac{d^2 \log p(y \mid \phi)}{d\phi^2}\right] = -E\left[\frac{d^2 \log p(y \mid \theta = h^{-1}(\phi))}{d\theta^2}\right]\left|\frac{d\theta}{d\phi}\right|^2 = J(\theta)\left|\frac{d\theta}{d\phi}\right|^2
\end{align}
$$
so $J(\phi)^{1/2} = J(\theta)^{1/2}\left|\frac{d\theta}{d\phi}\right|$, exactly the [[Change of Variables]] rule for densities.

$\sqrt{J}$ transforms like a density because $J$ transforms like a metric: Jeffreys prior is the Riemannian volume element of the Fisher information metric on the parameter manifold ($\sqrt{\det J}$ in several dimensions), which is why it does not depend on coordinates.

# Properties
- Resolves the "flat on which scale?" problem of noninformative priors by tying the prior to the model's information geometry rather than to a coordinate system.
- Recovers the uniform prior for a [[Location Parameter]] and $1/\theta$ for a [[Scale Parameter]].
- Often [[Improper Prior|improper]].
- In one-parameter models it is first-order [[Probability Matching Prior|probability matching]].
- Extends to multiparameter models via $p(\theta) \propto |\det J(\theta)|^{1/2}$ ([[Fisher Information Matrix]]), but the results are more controversial, and assigning independent noninformative priors to the components can give different answers. With many parameters, [[Hierarchical Model|hierarchical models]] are preferred.[^3]

[^1]: [Gelman et al., p. 52](zotero://open-pdf/library/items/HDF44SF4?page=62&annotation=6EI44RJ4)
[^2]: [Gelman et al., p. 53](zotero://open-pdf/library/items/HDF44SF4?page=63&annotation=I2UVQHP2)
[^3]: [Gelman et al., p. 53](zotero://open-pdf/library/items/HDF44SF4?page=63&annotation=8EZI3RYS)
