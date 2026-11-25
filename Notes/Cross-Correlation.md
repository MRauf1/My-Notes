---
tags:
  - mathematics
  - real_analysis
  - cryoEM
---

# Definition
> [!info] Cross-Correlation[^1]
> The cross-correlation of $g$ and $h$ is
> $$
> \begin{align}
> (g \star h)(x) = \int g(x + s)\,\overline{h(s)}\,ds:
> \end{align}
> $$
> shift $g$ by $x$, multiply by (the conjugate of) $h$, and integrate. Its [[Fourier Transform]] is given by the **correlation theorem**:
> $$
> \begin{align}
> g \star h \ \xrightarrow{\ \mathcal{F}\ }\ G\cdot\overline{H}.
> \end{align}
> $$

# Properties
- **Alignment.** If $h$ is a shifted copy of $g$, then $g \star h$ peaks at the shift: by Cauchy–Schwarz, $|\int g(x + s)\overline{h(s)}ds| \le \|g\|\|h\|$, with equality when $g(\cdot + x) \propto h$. This is the basis of template matching ([[Particle Picking]]), alignment ([[Iterative Refinement (Cryo-EM)]]) and motion correction ([[Motion Correction]]).
- **Relation to convolution**: it is [[Convolution]] with $h$ reflected and conjugated. For real $g$, reflection becomes conjugation in Fourier space, $g(-x) \to \overline{G(u)}$ ([[Complex Conjugate]]).
- **Autocorrelation.** $g \star g \to |G|^2$: the autocorrelation is the inverse transform of the power spectrum ([[Power Spectrum (Signal Processing)]]); in crystallography, the Patterson function.
- **Computation.** Computing it through the FFT costs $O(N\log N)$ instead of $O(N^2)$.

# Questions
> [!question]- Prove the correlation theorem.
> $$
> \begin{align}
> \mathcal{F}\{g\star h\}(u) = \iint g(x + s)\overline{h(s)}e^{-2\pi iux}ds\,dx \overset{y = x + s}{=} \int g(y)e^{-2\pi iuy}dy\;\overline{\int h(s)e^{-2\pi ius}ds} = G(u)\overline{H(u)}.
> \end{align}
> $$
> Here $e^{-2\pi iux} = e^{-2\pi iuy}e^{+2\pi ius}$, and $\overline{h(s)}e^{2\pi ius} = \overline{h(s)e^{-2\pi ius}}$. Fubini's theorem applies for integrable $g, h$.

[^1]: [Sigworth, Fourier transform notes, p. 7](zotero://open-pdf/library/items/FEUF2XYA?page=7&annotation=W4MUXNRT)
