---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Autoregressive Flow[^1]
> A generalization of [[Coupling Flow|coupling flows]] in which each input dimension is a separate block: the $d$-th output depends on the $d$-th input and the first $d-1$ inputs,
> $$
> \begin{align}
> h_d' = \mathrm{g}\left[h_d, \boldsymbol{\phi}[h_{1:d-1}]\right]
> \end{align}
> $$
> The invertible function $\mathrm{g}[\bullet, \bullet]$ is the **transformer** (unrelated to the [[Transformer]] architecture), and the parameters $\boldsymbol{\phi}, \boldsymbol{\phi}[h_1], \boldsymbol{\phi}[h_1, h_2], \dots$ are the **conditioners**, which may be arbitrary functions, usually neural networks.

![[Autoregressive Flow.png]]

# Types
- **Masked autoregressive flow (MAF)**: all outputs $h_d'$ are computed in parallel by one network with masks, so that the parameters at position $d$ depend only on earlier positions, as in [[Masked Self-Attention]] (connections relating inputs to previous outputs are pruned). Defined in the normalizing (inverse) direction so that the likelihood, and hence training, is efficient, but sampling is sequential and slow.[^2][^3]
- **Inverse autoregressive flow (IAF)**: the autoregressive flow is used in the forward (generative) direction, so sampling is efficient but likelihood evaluation (and training on data) is slow.[^3]

# Properties
- **Universal**: with sufficiently flexible transformer and conditioners, autoregressive flows are universal approximators that can represent any probability distribution.[^1]
- **Triangular Jacobian**: $\partial h_d' / \partial h_{d'} = 0$ for $d' > d$, so the Jacobian is [[Lower Triangular Matrix|lower triangular]] and its determinant is $\prod_d \partial \mathrm{g} / \partial h_d$.
- **Sequential inversion**: the inverse must be computed one dimension at a time, since $h_d$ requires the already recovered $h_{1:d-1}$:[^2]
$$
\begin{align}
h_1 &= \mathrm{g}^{-1}\left[h_1', \boldsymbol{\phi}\right] \\
h_2 &= \mathrm{g}^{-1}\left[h_2', \boldsymbol{\phi}[h_1]\right] \\
h_3 &= \mathrm{g}^{-1}\left[h_3', \boldsymbol{\phi}[h_{1:2}]\right] \\
h_4 &= \mathrm{g}^{-1}\left[h_4', \boldsymbol{\phi}[h_{1:3}]\right]
\end{align}
$$
  This cannot be parallelized, so inversion is time-consuming for large inputs; one direction is always fast and the other slow.
- **Teacher-student trick**: a MAF learns the distribution (teacher), then trains an IAF (student) from which sampling is efficient, giving fast learning and fast but approximate sampling ([[Probability Density Distillation]]).[^3]

[^1]: [Prince, p. 313](zotero://open-pdf/library/items/BWT7FYX5?page=327&annotation=RX38FBNQ)
[^2]: [Prince, p. 314](zotero://open-pdf/library/items/BWT7FYX5?page=328&annotation=DLPYEQTE)
[^3]: [Prince, p. 314](zotero://open-pdf/library/items/BWT7FYX5?page=328&annotation=QWYLYBD3)
