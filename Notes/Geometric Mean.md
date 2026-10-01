---
tags:
  - mathematics
  - pre_algebra
---

# Definition

> [!info] Definition 1 (Geometric Mean)
> For a dataset of $n$ positive numbers $\{x_1, ..., x_n\}$, the geometric mean is
> $$
> \begin{align}
> \left( \prod_{i=1}^{n} x_i \right)^{1/n}
> \end{align}
> $$

> [!info] Definition 2 (Geometric Mean of a Random Variable)[^1]
> For a positive [[Random Variable]] $\theta$, the geometric mean is
> $$
> \begin{align}
> \mathrm{GM}(\theta) = \exp\big(E[\log \theta]\big)
> \end{align}
> $$
> Definition 1 is the case of $\theta$ uniform on $\{x_1, \dots, x_n\}$.

The geometric mean is the average of a set of positive numbers under multiplication rather than addition, making it appropriate for quantities that combine multiplicatively, such as growth rates or ratios. It is a type of [[Mean|mean]].

# Properties

- The geometric mean of a set is always less than or equal to its [[Arithmetic Mean|arithmetic mean]], with equality iff all values in the set are equal ([[AM-GM Inequality]]).
- $\mathrm{GM}(\theta) \leq E(\theta)$ by [[Jensen's Inequality]]; its spread counterpart is the [[Geometric Standard Deviation]].

[^1]: [Gelman et al., p. 6](zotero://open-pdf/library/items/HDF44SF4?page=16&annotation=3BPERD6Z)
