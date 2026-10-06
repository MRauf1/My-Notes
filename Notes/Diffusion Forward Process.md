---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Diffusion Forward Process[^1][^2]
> The fixed encoder of a [[Diffusion Model|diffusion model]], mapping a data example $\mathbf{x}$ through latent variables $\mathbf{z}_1, \dots, \mathbf{z}_T$ of the same size as $\mathbf{x}$:
> $$
> \begin{align}
> \mathbf{z}_1 &= \sqrt{1-\beta_1}\cdot\mathbf{x} + \sqrt{\beta_1}\cdot\boldsymbol{\epsilon}_1 \\
> \mathbf{z}_t &= \sqrt{1-\beta_t}\cdot\mathbf{z}_{t-1} + \sqrt{\beta_t}\cdot\boldsymbol{\epsilon}_t \qquad \forall\, t \in \{2, \dots, T\}
> \end{align}
> $$
> with $\boldsymbol{\epsilon}_t \sim \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$. The first term attenuates the data plus the noise added so far; the second adds more noise. Equivalently,
> $$
> \begin{align}
> q(\mathbf{z}_1|\mathbf{x}) &= \mathrm{Norm}_{\mathbf{z}_1}\left[\sqrt{1-\beta_1}\,\mathbf{x}, \beta_1\mathbf{I}\right] \\
> q(\mathbf{z}_t|\mathbf{z}_{t-1}) &= \mathrm{Norm}_{\mathbf{z}_t}\left[\sqrt{1-\beta_t}\,\mathbf{z}_{t-1}, \beta_t\mathbf{I}\right] \\
> q(\mathbf{z}_{1\dots T}|\mathbf{x}) &= q(\mathbf{z}_1|\mathbf{x})\prod_{t=2}^T q(\mathbf{z}_t|\mathbf{z}_{t-1})
> \end{align}
> $$
> The hyperparameters $\beta_t \in [0, 1]$, which set how quickly noise is blended in, are the **noise schedule**.

# Properties
- **Markov chain**: $\mathbf{z}_t$ depends only on $\mathbf{z}_{t-1}$, so $q(\mathbf{z}_t|\mathbf{z}_{t-1}, \mathbf{x}) = q(\mathbf{z}_t|\mathbf{z}_{t-1})$.[^2]
- **Variance preserving**: if $\mathrm{Var}[\mathbf{z}_{t-1}] = \mathbf{I}$ then $\mathrm{Var}[\mathbf{z}_t] = (1-\beta_t)\mathbf{I} + \beta_t\mathbf{I} = \mathbf{I}$, so the scaling $\sqrt{1-\beta_t}$ keeps the signal from blowing up as noise accumulates.
- **Convergence to noise**: with enough steps all traces of the data are removed, and $q(\mathbf{z}_T|\mathbf{x}) = q(\mathbf{z}_T) = \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$ ([[Diffusion Kernel]] with $\alpha_T \to 0$).[^2]
- Can be sampled at any $t$ directly from $\mathbf{x}$, skipping intermediate steps ([[Diffusion Kernel]]).
- **Not invertible in closed form**: the reverse $q(\mathbf{z}_{t-1}|\mathbf{z}_t)$ requires the unknown marginal $q(\mathbf{z}_{t-1})$, but conditioning on $\mathbf{x}$ makes it tractable ([[Conditional Diffusion Distribution]]).
- The discrete-time limit of the variance-preserving SDE $d\mathbf{z} = -\tfrac{1}{2}\beta(t)\mathbf{z}\,dt + \sqrt{\beta(t)}\,d\mathbf{w}$, an Ornstein–Uhlenbeck-type process ([[Probability Flow ODE]]).
- Has no learned parameters; varying $\beta_t$ across steps (e.g. linear or cosine schedules) improves results.[^3]

[^1]: [Prince, p. 350](zotero://open-pdf/library/items/BWT7FYX5?page=364&annotation=KJ4IJTAV)
[^2]: [Prince, p. 351](zotero://open-pdf/library/items/BWT7FYX5?page=365&annotation=UWCIDYTZ)
[^3]: [Prince, p. 368](zotero://open-pdf/library/items/BWT7FYX5?page=382&annotation=5GEFQ5BZ)
