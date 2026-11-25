---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Maximum Likelihood Reconstruction[^1]
> Under the [[Cryo-EM Image Formation Model]] with white Gaussian noise of pixel variance $\sigma^2$ ($p$ pixels per image), the [[Maximum Likelihood Estimation|maximum likelihood]] estimate of the structure **marginalizes the rotations**, integrating over $SO(3)$ with the uniform (Haar) measure:
> $$
> \begin{align}
> \ell_n(\varphi) &= -\frac{np}{2}\log(2\pi\sigma^2) + \sum_{i=1}^n \log \int_{SO(3)} \exp\!\Big(-\frac{\|I_i - h_i \star P(R\circ\varphi)\|^2}{2\sigma^2}\Big)\, dR, \\
> \hat\varphi_{\text{MLE}} &= \arg\max_{\varphi}\ \sum_{i=1}^n \log \int_{SO(3)} \exp\!\Big(-\frac{\|I_i - h_i \star P(R\circ\varphi)\|^2}{2\sigma^2}\Big)\, dR .
> \end{align}
> $$

# Properties
- **Marginal, not joint.** Maximizing jointly over $\varphi, R_1, \dots, R_n$ makes the number of parameters grow with $n$, which voids consistency and asymptotic efficiency ([[Neyman–Scott Problem]]). The marginal MLE keeps a fixed parameter count. Under mild conditions it is consistent and asymptotically attains the [[Rao-Cramér Lower Bound|Cramér–Rao bound]].
- **Hard optimization.** It is high-dimensional (about $10^6$ parameters for a $100^3$ grid), nonlinear and non-convex. Newton-type methods are too costly per iteration, which leaves first-order methods ([[Stochastic Gradient Descent|SGD]], in [[Ab Initio Reconstruction]]) and EM ([[Iterative Refinement (Cryo-EM)]]).
- Consistency does not imply small error at finite $n$: the problem can be ill-conditioned, which needs a prior ([[MAP Refinement (Cryo-EM)]]).

# Questions
> [!question]- Why is the "correct" MLE the one that marginalizes the rotations?
> The theorems giving the MLE consistency and asymptotic efficiency assume a fixed, finite-dimensional parameter while $n \to \infty$. If each image's $R_i$ is also a parameter, the dimension grows with $n$: every new image adds an unknown, and the joint MLE can be inconsistent, as in Neyman–Scott. Integrating each $R_i$ out leaves the likelihood a function of $\varphi$ alone, where the standard asymptotics apply.

[^1]: [Singer and Sigworth, 2020, p. 13](zotero://open-pdf/library/items/FKVQSKD6?page=13&annotation=XW9CBBNK)
