---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Locally Measurable Set and Saturated Measure[^1]
> Let $(X, \mathcal{M}, \mu)$ be a [[Measure Space]]. A set $E \subseteq X$ is **locally measurable** if
> $$
> \begin{align}
> E \cap A \in \mathcal{M} \quad \text{for all } A \in \mathcal{M} \text{ with } \mu(A) < \infty.
> \end{align}
> $$
> Let $\widetilde{\mathcal{M}}$ be the collection of locally measurable sets; clearly $\mathcal{M} \subseteq \widetilde{\mathcal{M}}$. If $\mathcal{M} = \widetilde{\mathcal{M}}$, then $\mu$ is **saturated**.

Saturation asks that measurability be detectable "locally", by intersecting with sets of finite measure only.

# Properties
- If $\mu$ is [[Sigma-Finite Measure|$\sigma$-finite]], then $\mu$ is saturated.[^2]
- $\widetilde{\mathcal{M}}$ is a [[Sigma-Field|$\sigma$-algebra]].[^2]
- **Saturation**: $\widetilde{\mu}(E) = \mu(E)$ for $E \in \mathcal{M}$ and $\widetilde{\mu}(E) = \infty$ otherwise defines a saturated measure on $\widetilde{\mathcal{M}}$, the saturation of $\mu$.[^2]
- If $\mu$ is [[Complete Measure|complete]], so is $\widetilde{\mu}$.[^2]
- If $\mu$ is [[Semifinite Measure|semifinite]], then $\underline{\mu}(E) = \sup\{\mu(A) : A \in \mathcal{M},\ A \subseteq E\}$ is a saturated measure on $\widetilde{\mathcal{M}}$ extending $\mu$; in general $\underline{\mu} \neq \widetilde{\mu}$.[^2]

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=41&annotation=DI7TPTM5)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=41&annotation=4I3KVIC3)
