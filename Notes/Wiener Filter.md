---
tags:
  - computer_science
  - computer_vision
  - cryoEM
---

# Definition
> [!info] Wiener Filter[^1]
> For a degradation $y = h * x + n$ with $x$ and $n$ zero-mean, uncorrelated, and stationary, with power spectra $S_x, S_n$, the linear filter minimizing the mean squared error $\mathbb{E}\|\hat x - x\|^2$ among all linear estimators $\hat x = g * y$ is, in Fourier space,
> $$
> \begin{align}
> G(k) = \frac{\overline{H(k)}\, S_x(k)}{|H(k)|^2 S_x(k) + S_n(k)} = \frac{\overline{H(k)}}{|H(k)|^2 + 1/\mathrm{SSNR}(k)}, \qquad \mathrm{SSNR} = \frac{S_x}{S_n}.
> \end{align}
> $$

# Properties
- Where $\mathrm{SSNR} \to \infty$ it inverts $H$. Where $H \approx 0$ it outputs $\approx 0$ instead of amplifying noise, so information at zeros of $H$ is not recovered.
- With $m$ observations $y_i = h_i * x + n_i$ of the same $x$: $\hat X = \sum_i \overline{H_i} Y_i \big/ \big(\sum_i |H_i|^2 + 1/\mathrm{SSNR}\big)$. Zeros of one $H_i$ are filled by the others.
- For Gaussian $x$ and $n$, it is the posterior mean. It equals Tikhonov regularization with a frequency-dependent weight $1/\mathrm{SSNR}(k)$.
- Uses: [[CTF Correction]] and the M-step of [[MAP Refinement (Cryo-EM)]].

# Questions
> [!question]- Derive $G$ frequency by frequency.
> In Fourier space the problem decouples: $Y = HX + N$ at each $k$. Minimize $\mathbb{E}|GY - X|^2 = |GH - 1|^2 S_x + |G|^2 S_n$ over the complex number $G$. Setting the derivative in $\overline{G}$ to zero gives $(GH - 1)\overline{H} S_x + G S_n = 0$, so $G = \overline{H} S_x/(|H|^2 S_x + S_n)$. The cross-terms vanish because $X$ and $N$ are uncorrelated.

[^1]: [Singer and Sigworth, 2020, p. 11](zotero://open-pdf/library/items/FKVQSKD6?page=11&annotation=62GRKYFV)
