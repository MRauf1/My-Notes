---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Curse of Dimensionality[^1]
> The severe difficulties that arise in spaces of many dimensions (Bellman), where intuitions formed in low-dimensional spaces fail. In particular, dividing a region of a $D$-dimensional space into regular cells, with $k$ divisions per axis, gives $k^D$ cells, so the amount of training data needed to keep the cells non-empty grows exponentially with $D$.[^2]

# Properties
- **Polynomial models**: a general polynomial of order $M$ in $D$ input variables has $\binom{D+M}{M}$ independent coefficients (not $D^M$ distinct ones, due to interchange symmetries among the variables), which grows like $D^M$. This is power-law rather than exponential growth, but still rapidly unwieldy.[^3]
- **Volume concentrates near the surface**: the volume of a $D$-dimensional [[Sphere|sphere]] of radius $r$ scales as $V_D(r) = K_D r^D$ with $K_D = \pi^{D/2}/\Gamma(D/2 + 1)$ ([[Gamma Function]]), so the fraction of the unit sphere's volume in the shell between $r = 1 - \epsilon$ and $r = 1$ is
$$
\begin{align}
\frac{V_D(1) - V_D(1 - \epsilon)}{V_D(1)} = 1 - (1 - \epsilon)^D
\end{align}
$$
  which tends to $1$ for large $D$ even for small $\epsilon$.[^4]
- **Gaussian mass concentrates in a thin shell**: the density of the radius $r$ of a $D$-dimensional isotropic Gaussian, $p(r) \propto r^{D-1}\exp(-r^2/2\sigma^2)$, is sharply peaked near $r \approx \sigma\sqrt{D}$, far from the mode at the origin, where the density is highest but the volume is negligible.[^5]
- Does not prevent effective high-dimensional methods, for two reasons:[^6]
	- Real data is often confined to a region of much lower effective dimensionality, and the directions of important variation in the targets may be confined further.
	- Real data typically exhibits (at least local) smoothness, so small changes in the input produce small changes in the target, enabling local interpolation.
- Motivates [[Feature Extraction]], and explains why [[Rejection Sampling]] envelopes and grid-based [[Density Estimation]] degrade in high dimensions.

[^1]: [Bishop, 2006, p. 36](zotero://open-pdf/library/items/5G99AZ8U?page=56&annotation=6X6VGU9N)
[^2]: [Bishop, 2006, p. 35](zotero://open-pdf/library/items/5G99AZ8U?page=55&annotation=GUNT53A2)
[^3]: [Bishop, 2006, p. 36](zotero://open-pdf/library/items/5G99AZ8U?page=56&annotation=C9AIYB2T)
[^4]: [Bishop, 2006, p. 36](zotero://open-pdf/library/items/5G99AZ8U?page=56&annotation=DLA2WA46)
[^5]: [Bishop, 2006, p. 36](zotero://open-pdf/library/items/5G99AZ8U?page=56&annotation=USYG6GWT)
[^6]: [Bishop, 2006, p. 37](zotero://open-pdf/library/items/5G99AZ8U?page=57&annotation=8PZ3IMKQ)
