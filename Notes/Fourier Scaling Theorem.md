---
tags:
  - mathematics
  - real_analysis
  - cryoEM
---

# Definition
> [!info] Fourier Scaling Theorem[^1]
> If $g \xrightarrow{\mathcal{F}} G$ ([[Fourier Transform]]), then for $a \neq 0$
> $$
> \begin{align}
> g(ax) \ \xrightarrow{\ \mathcal{F}\ }\ \frac{1}{|a|}\, G\Big(\frac{u}{a}\Big).
> \end{align}
> $$
> Compressing a function in real space ($|a| > 1$) stretches its transform in frequency space, and vice versa.

# Properties
- **Reciprocal space.** Applied to a [[Dirac Comb]], a lattice with spacing $a$ transforms into a lattice with spacing $1/a$. This reciprocal relationship is the origin of the crystallographic term "reciprocal space".
- **Area-preserving version**: $|a|\,g(ax) \to G(u/a)$, as in the [[Fourier Transform of Gaussian]].
- In several dimensions, $g(A\mathbf{x}) \to |\det A|^{-1}\, G(A^{-\top}\mathbf{u})$.
- Its quantitative form is the uncertainty principle: the widths of $g$ and $G$ cannot both be small.

# Questions
> [!question]- Prove the scaling theorem, including the absolute value.
> Substitute $y = ax$. For $a > 0$, $\int g(ax)e^{-2\pi iux}dx = \frac1a\int g(y)e^{-2\pi i(u/a)y}dy = \frac1a G(u/a)$. For $a < 0$, the substitution reverses the limits of integration. Flipping them back gives a factor $-1$, so the prefactor is $-1/a = 1/|a|$.

[^1]: [Sigworth, Fourier transform notes, p. 4](zotero://open-pdf/library/items/FEUF2XYA?page=4&annotation=LW2C75WW)
