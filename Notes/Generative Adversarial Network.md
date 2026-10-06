---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Generative Adversarial Network (GAN)[^1][^2]
> An [[Unsupervised Learning|unsupervised]] [[Generative Model|generative model]] consisting of two networks trained against each other:
> - a **generator** $\mathbf{x}_j^* = \mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}]$ that maps [[Latent Variables|latent variables]] $\mathbf{z}_j$ drawn from a simple base distribution (e.g. a standard normal) to samples in data space;
> - a **discriminator** $f[\mathbf{x}, \boldsymbol{\phi}]$ that returns a scalar which is higher when it believes $\mathbf{x}$ is a real example rather than a generated sample.
>
> With real examples labelled $y = 1$ and generated samples $y = 0$, the discriminator minimizes the [[Binary Cross-Entropy Loss|binary cross-entropy]] while the generator maximizes it, giving the minimax game
> $$
> \begin{align}
> \hat{\boldsymbol{\theta}} = \underset{\boldsymbol{\theta}}{\operatorname{argmax}}\left[\min_{\boldsymbol{\phi}}\left[\sum_j -\log\left[1 - \mathrm{sig}\left[f[\mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}], \boldsymbol{\phi}]\right]\right] - \sum_i \log\left[\mathrm{sig}\left[f[\mathbf{x}_i, \boldsymbol{\phi}]\right]\right]\right]\right]
> \end{align}
> $$
> where $i$ indexes real examples, $j$ generated samples, and $\mathrm{sig}[\bullet]$ is the logistic [[Sigmoid Function|sigmoid]].

![[GAN Training Pipeline.png]]

# Types
- [[DCGAN]]: convolutional GAN with a specific recipe for stable training.
- [[Wasserstein GAN]]: replaces the implicit [[Jensen-Shannon Divergence]] with the [[Wasserstein Distance]].
- [[Conditional GAN]], [[Auxiliary Classifier GAN]], [[InfoGAN]]: conditional generation and attribute discovery.
- [[Pix2Pix]], [[SRGAN]], [[CycleGAN]]: image translation driven by an [[Adversarial Loss]].
- [[StyleGAN]]: injects style and noise latents at multiple scales.

# Properties
- **No likelihood**: a GAN is only a sampling mechanism; it builds no probability distribution over the data and cannot evaluate the probability of a new data point (contrast [[Probabilistic Generative Model]]).[^1]
- **Training**: split the minimax objective into two minimization problems (negate the generator objective and drop the real-example term, which does not depend on $\boldsymbol{\theta}$):[^3][^4]
$$
\begin{align}
L[\boldsymbol{\phi}] &= \sum_j -\log\left[1 - \mathrm{sig}\left[f[\mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}], \boldsymbol{\phi}]\right]\right] - \sum_i \log\left[\mathrm{sig}\left[f[\mathbf{x}_i, \boldsymbol{\phi}]\right]\right] \\
L[\boldsymbol{\theta}] &= \sum_j \log\left[1 - \mathrm{sig}\left[f[\mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}], \boldsymbol{\phi}]\right]\right]
\end{align}
$$
  At each step, draw a batch $\{\mathbf{z}_j\}$, generate $\mathbf{x}_j^* = \mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}]$, draw a batch of real examples $\{\mathbf{x}_i\}$, and alternate one or more [[Gradient Descent|gradient descent]] steps on each loss.
- **Non-saturating generator loss**: early in training $\mathrm{sig}[f[\mathbf{x}^*, \boldsymbol{\phi}]] \approx 0$ and $L[\boldsymbol{\theta}]$ saturates, so in practice the generator usually minimizes $-\sum_j \log\left[\mathrm{sig}\left[f[\mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}], \boldsymbol{\phi}]\right]\right]$ instead, which has the same fixed point but stronger gradients (Goodfellow et al., 2014).
- **The solution is a [[Nash Equilibrium]]**: a point that is simultaneously a minimum of the loss in $\boldsymbol{\phi}$ and a maximum in $\boldsymbol{\theta}$. At convergence the generated samples follow the data distribution and $\mathrm{sig}[f[\bullet, \boldsymbol{\phi}]] = 0.5$ (chance), after which the discriminator is discarded.[^2][^5]
- As the two sets become harder to separate, the sigmoid flattens and the impetus to change $\boldsymbol{\theta}$ weakens.[^2]
- **Optimal discriminator**: with equal numbers of real and generated samples, writing the losses as expectations over the generated distribution $Pr(\mathbf{x}^*)$ and the data distribution $Pr(\mathbf{x})$, the optimal discriminator for an input $\tilde{\mathbf{x}}$ of unknown origin evaluates it under both:[^6]
$$
\begin{align}
\mathrm{sig}[f[\tilde{\mathbf{x}}, \boldsymbol{\phi}]] = Pr(\text{real} | \tilde{\mathbf{x}}) = \frac{Pr(\tilde{\mathbf{x}} | \text{real})}{Pr(\tilde{\mathbf{x}} | \text{generated}) + Pr(\tilde{\mathbf{x}} | \text{real})}
\end{align}
$$
  Substituting it back gives $L[\boldsymbol{\phi}^*] = \log 4 - 2\,D_{JS}\left[Pr(\mathbf{x}^*) \,\|\, Pr(\mathbf{x})\right]$, so against an optimal discriminator the generator minimizes the [[Jensen-Shannon Divergence]] between the generated and real distributions.
- **Missing coverage**: of the two JS terms, only the *quality* term depends on the generator; the *coverage* term does not, so the generator is content to model a subset of the data accurately — the putative cause of [[Mode Collapse|mode dropping]].[^7]
- **Vanishing gradients**: if the two distributions are disjoint, the JS divergence is maximal and constant, so small changes to the generator do not decrease the loss; equivalently, a discriminator that perfectly separates the sets has flat outputs around the samples. Disjointness is likely: generated samples lie on a manifold whose dimension is that of $\mathbf{z}$, and real data also lie on a low-dimensional manifold. Empirically, training the discriminator further with the generator frozen shrinks the generator gradients, so the discriminator must not get too good relative to the generator. This motivates the [[Wasserstein GAN]].[^8]
- **Notoriously hard to train**: unstable optimization and unusual sensitivity to architectural and optimizer choices (see [[DCGAN]]); realistic samples do not imply that all modes are generated ([[Mode Collapse]]).[^9]
- **Quality improvements**: [[Progressive Growing]], [[Minibatch Discrimination]], the [[Truncation Trick]], and careful normalization and regularization; moving smoothly through latent space can produce realistic interpolations.[^10]
- **Inversion**: edit a real image by projecting it to latent space, manipulating the latent variable, and mapping back ([[GAN Inversion]]).[^11]
- The discriminator can also serve as a learned prior favouring realism in translation tasks ([[Adversarial Loss]]).[^12]
- In terms of [[Generative Model Desiderata]]: efficient sampling, high quality, well-behaved latent space, but poor coverage and no likelihood. Evaluated with [[Fréchet Inception Distance]], [[Inception Score]], [[Manifold Precision and Recall]].

[^1]: [Prince, p. 276](zotero://open-pdf/library/items/BWT7FYX5?page=290&annotation=M5ZRXB98); [Prince, p. 276](zotero://open-pdf/library/items/BWT7FYX5?page=290&annotation=X4HVXGZR)
[^2]: [Prince, p. 276](zotero://open-pdf/library/items/BWT7FYX5?page=290&annotation=9NMYXSL4); [Prince, p. 276](zotero://open-pdf/library/items/BWT7FYX5?page=290&annotation=FJYK64LY); [Prince, p. 277](zotero://open-pdf/library/items/BWT7FYX5?page=291&annotation=3NEV2JB7); [Prince, p. 277](zotero://open-pdf/library/items/BWT7FYX5?page=291&annotation=AMZMMIYV)
[^3]: [Prince, p. 278](zotero://open-pdf/library/items/BWT7FYX5?page=292&annotation=D5K288KV); [Prince, p. 278](zotero://open-pdf/library/items/BWT7FYX5?page=292&annotation=X8R7XCJN)
[^4]: [Prince, p. 279](zotero://open-pdf/library/items/BWT7FYX5?page=293&annotation=EADV72DM); [Prince, p. 279](zotero://open-pdf/library/items/BWT7FYX5?page=293&annotation=RZWFVKEW)
[^5]: [Prince, p. 278](zotero://open-pdf/library/items/BWT7FYX5?page=292&annotation=DSBU53YR)
[^6]: [Prince, p. 282](zotero://open-pdf/library/items/BWT7FYX5?page=296&annotation=7IKS8BK7)
[^7]: [Prince, p. 283](zotero://open-pdf/library/items/BWT7FYX5?page=297&annotation=ZD6YAEMZ)
[^8]: [Prince, p. 283](zotero://open-pdf/library/items/BWT7FYX5?page=297&annotation=V9QJTZ5H)
[^9]: [Prince, p. 280](zotero://open-pdf/library/items/BWT7FYX5?page=294&annotation=KTE77RQX); [Prince, p. 276](zotero://open-pdf/library/items/BWT7FYX5?page=290&annotation=X4HVXGZR)
[^10]: [Prince, p. 289](zotero://open-pdf/library/items/BWT7FYX5?page=303&annotation=BNF8TWA5)
[^11]: [Prince, p. 302](zotero://open-pdf/library/items/BWT7FYX5?page=316&annotation=44KUHMX9)
[^12]: [Prince, p. 291](zotero://open-pdf/library/items/BWT7FYX5?page=305&annotation=W9HV4LEK)
