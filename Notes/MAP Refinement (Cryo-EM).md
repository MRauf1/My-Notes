---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] MAP Refinement (Cryo-EM)[^1]
> [[Maximum a Posteriori Learning|MAP]] estimation of the structure from the images $X$,
> $$
> \begin{align}
> \hat\varphi_{\text{MAP}} = \arg\max_{\varphi}\ \log \Pr(X \mid \varphi) + \log \Pr(\varphi),
> \end{align}
> $$
> computed by MAP-EM: the E-step of [[Iterative Refinement (Cryo-EM)]], and an M-step that maximizes the posterior instead of the likelihood. The standard prior makes each Fourier voxel $\Phi_\ell$ of $\varphi$ an independent zero-mean complex Gaussian with variance $\tau_\ell^2$. The variance is re-estimated each iteration as the shell average of $\tfrac12|\Phi_\ell|^2$ (a radial function), then inflated by an ad hoc factor $T \in [2, 4]$.

# Properties
- **Why regularize.** Unregularized ML-EM overfits, producing spurious high-frequency content.
- **Equivalent to Tikhonov / Wiener filtering.** The Gaussian prior adds a Tikhonov term with weight proportional to $1/\tau^2$ in Fourier space, and $\tau^2$ plays the role of the SNR in a [[Wiener Filter]]. The factor $T$ compensates for ignoring correlations between Fourier coefficients.
- **Frequency marching.** Starting from a low-resolution map, $\tau^2$ is large only at low frequencies, so high frequencies are strongly damped. Resolution grows gradually over the iterations.
- **Beyond MAP.** The posterior $\Pr(\varphi \mid X)$ would give the MMSE estimator $\mathbb{E}[\varphi \mid X]$ (the analogue of the Wiener filter) and credible intervals for validation. MAP is the "poor man's Bayesian inference": only the mode. MCMC sampling ([[Markov Chain Monte Carlo]]) is rarely used for full maps ([[Open Problems in Cryo-EM]]).
- Another common prior is the support constraint ([[Cryo-EM Masking]]).
- **Priors in use are chosen for convenience.** RELION uses independent Gaussian Fourier coefficients; cryoSPARC uses independent Poisson voxels. Such priors may bias the result, and replacing them with biologically informed priors was posed as an open challenge in 2020.[^2] Learned generative priors over density maps now exist, e.g. CryoFM, a flow-matching prior used for posterior sampling (ICLR 2025).[^3]
- A deterministic version of frequency marching adds one Fourier shell per iteration, with hard pose assignment and a least-squares solve.

# Questions
> [!question]- Explain frequency marching from the prior update.
> The M-step at frequency $k$ shrinks the data estimate by a factor like $W(k)/(W(k) + \sigma^2/\tau^2(k))$. Since $\tau^2$ is re-estimated from the current map's own power, a low-resolution map has $\tau^2 \approx 0$ at high $k$. There the shrinkage is nearly total, so the next map gains high-frequency content only where the data's signal is strong enough to overcome it. Each iteration raises the power at slightly higher $k$, which raises $\tau^2$ there, and the effective resolution climbs step by step.

[^1]: [Singer and Sigworth, 2020, p. 18](zotero://open-pdf/library/items/FKVQSKD6?page=18&annotation=TVUEFM33)
[^2]: [Bendory et al., 2020, p. 11](zotero://open-pdf/library/items/N4ZIHINK?page=11&annotation=7UQFAMEL)
[^3]: [Zhou, Li, Yuan & Gu (2025), CryoFM: A Flow-based Foundation Model for Cryo-EM Densities, ICLR](https://arxiv.org/abs/2410.08631)
