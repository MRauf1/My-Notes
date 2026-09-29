---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Minkowski Loss[^1]
> A generalization of the squared loss with expectation
> $$
> \begin{align}
> \mathbb{E}[L_q] = \iint |y(\mathbf{x}) - t|^q\,p(\mathbf{x}, t)\,d\mathbf{x}\,dt
> \end{align}
> $$
> which reduces to the expected squared loss for $q = 2$.

# Properties
- The minimizer $y(\mathbf{x})$ of $\mathbb{E}[L_q]$ is:[^1]
	- the conditional mean $\mathbb{E}[t | \mathbf{x}]$ for $q = 2$ ([[Regression Function]]);
	- the conditional [[Median]] for $q = 1$;
	- the conditional [[Mode]] for $q \to 0$.
- Squared loss can perform poorly when $p(t | \mathbf{x})$ is multimodal, since the conditional mean may fall between modes; other $q$ trade this off.
- $q = 1$ corresponds to maximum likelihood under Laplace noise and is less sensitive to outliers than $q = 2$ ([[Probabilistic Formulation of Regression]]).

[^1]: [Bishop, 2006, p. 48](zotero://open-pdf/library/items/5G99AZ8U?page=68&annotation=6Z33WBIN)
