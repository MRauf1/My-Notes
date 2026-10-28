---
tags:
  - mathematics
  - topology
---

# Definition
> [!info] Indexed Family of Sets[^1]
> Let $\mathcal{A}$ be a nonempty [[Collection of Set|collection of sets]]. An indexing function for $\mathcal{A}$ is a [[Surjective Function]] $f: J \to \mathcal{A}$ from some set $J$, called the index set. The collection $\mathcal{A}$ together with $f$ is called an indexed family of sets. Writing $A_\alpha = f(\alpha)$ for $\alpha \in J$, the family is denoted $\{A_\alpha\}_{\alpha \in J}$ (or simply $\{A_\alpha\}$).

> [!info] Indexed Union and Intersection[^2]
> $$
> \begin{align}
> \bigcup_{\alpha \in J} A_\alpha &= \{x \mid x \in A_\alpha \text{ for at least one } \alpha \in J\}, \\
> \bigcap_{\alpha \in J} A_\alpha &= \{x \mid x \in A_\alpha \text{ for every } \alpha \in J\}.
> \end{align}
> $$

The indexing function need not be injective: $A_\alpha = A_\beta$ is allowed even though $\alpha \neq \beta$.[^3]

# Properties
- Indexed unions and intersections coincide with the [[Set Union]] $\bigcup \mathcal{A}$ and [[Set Intersection]] $\bigcap \mathcal{A}$ of the collection, since $f$ is surjective.
- The [[Cartesian Product]] $\prod_{\alpha \in J} A_\alpha$ is defined for an indexed family, since it requires an ordering/labelling of the factors.
- [[Sequence|Sequences]] of sets $\{A_n\}_{n \in \mathbb{Z}^+}$ are indexed families with $J = \mathbb{Z}^+$.

[^1]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=38&annotation=E3VSEUEF)
[^2]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=38&annotation=VEX6YHKP)
[^3]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=38&annotation=5SJ8N9XU)
