---
tags:
  - mathematics
  - real_analysis
  - cryoEM
---

# Definition
> [!info] Fourier Transform of Gaussian[^1]
> With the ordinary-frequency convention $G(u) = \int g(x)\,e^{-2\pi i ux}\,dx$ ([[Fourier Transform]]), the Gaussian $e^{-\pi x^2}$ is its own Fourier transform, and its area-preserving rescalings transform reciprocally:
> $$
> \begin{align}
> e^{-\pi x^2} \ \xrightarrow{\ \mathcal{F}\ }\ e^{-\pi u^2}, \qquad a\,e^{-\pi (ax)^2} \ \xrightarrow{\ \mathcal{F}\ }\ e^{-\pi (u/a)^2} \quad (a > 0).
> \end{align}
> $$

# Properties
- A narrower Gaussian in $x$ (larger $a$) gives a broader one in $u$ ([[Fourier Scaling Theorem]]). The prefactor $a$ keeps the area $\int a\,e^{-\pi(ax)^2}dx = 1$, which makes the transform equal $1$ at $u = 0$.
- As $a \to \infty$, $a\,e^{-\pi(ax)^2} \to \delta(x)$ and its transform tends to $1$, giving $\delta \leftrightarrow 1$ ([[Dirac Delta Function]]).
- A Gaussian blur is therefore a Gaussian damping of high frequencies, the form of the [[CTF Envelope Function]].

# Questions
> [!question]- Prove $e^{-\pi x^2} \to e^{-\pi u^2}$ by completing the square.
> $$
> \begin{align}
> G(u) = \int e^{-\pi(x^2 + 2iux)}dx = \int e^{-\pi(x^2 + 2iux - u^2)}dx\; e^{-\pi u^2} = e^{-\pi u^2}\int e^{-\pi(x + iu)^2}dx.
> \end{align}
> $$
> The remaining integral equals $\int e^{-\pi x^2}dx = 1$: by Cauchy's theorem, the integral of the entire function $e^{-\pi z^2}$ along the horizontal line $\operatorname{Im} z = u$ equals that along the real axis, since the vertical end segments vanish as $|\operatorname{Re} z| \to \infty$. Hence $G(u) = e^{-\pi u^2}$.

> [!question]- Derive the scaled pair $a\,e^{-\pi(ax)^2} \to e^{-\pi(u/a)^2}$.
> Substitute $y = ax$, $dy = a\,dx$: $\int a\,e^{-\pi(ax)^2}e^{-2\pi iux}dx = \int e^{-\pi y^2}e^{-2\pi i(u/a)y}dy = e^{-\pi(u/a)^2}$, by the unscaled pair evaluated at $u/a$.

[^1]: [Sigworth, Fourier transform notes, p. 2](zotero://open-pdf/library/items/FEUF2XYA?page=2&annotation=9HG3R78W)
