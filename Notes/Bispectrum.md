---
tags:
  - computer_science
  - computer_vision
  - cryoEM
---

# Definition
> [!info] Bispectrum[^1]
> A polynomial $p$ is **invariant** under a [[Group Action|group action]] if $p(g\circ x) = p(x)$ for all $g \in G$ and all signals $x$. For a signal $x \in \mathbb{R}^L$ under cyclic shifts, with DFT $X$, the invariants of orders $1$–$3$ are:
> $$
> \begin{align}
> \text{mean: } X[0], \qquad \text{power spectrum: } |X[k]|^2, \qquad \text{bispectrum: } B[k_1, k_2] = X[k_1]\, X[k_2]\, \overline{X[k_1 + k_2]}.
> \end{align}
> $$

# Properties
- The bispectrum (Tukey) is the third-order invariant. For generic signals (no zero Fourier coefficients), it determines $x$ up to a shift, so it solves [[Multi-Reference Alignment]] under cyclic shifts at the third-moment rate ([[Orbit Recovery Sample Complexity]]).
- **Uses in cryo-EM:**
  - rotation-invariant nearest-neighbour search in [[2D Classification]], on [[Steerable PCA]] coefficients;
  - Kam's third-order step in [[Kam's Method]];
  - recovery directly from micrographs in [[Multi-Target Detection]].

# Questions
> [!question]- Show that the bispectrum is shift-invariant, and why the power spectrum is not enough.
> A shift by $s$ multiplies $X[k]$ by $e^{-2\pi i ks/L}$. Then
> $$
> \begin{align}
> B[k_1,k_2] \mapsto X[k_1]X[k_2]\overline{X[k_1+k_2]}\, e^{-2\pi i (k_1 + k_2 - (k_1+k_2))s/L} = B[k_1,k_2].
> \end{align}
> $$
> The power spectrum $|X[k]|^2$ is invariant too, but it discards all phases: every signal with the same Fourier magnitudes, e.g. its reflections and phase-scrambled versions, has the same power spectrum. The bispectrum keeps the phase differences $\phi_{k_1} + \phi_{k_2} - \phi_{k_1+k_2}$. From these, all phases can be recovered recursively (given $\phi_0$ and an arbitrary $\phi_1$, which is the shift freedom), provided no $X[k]$ vanishes.

[^1]: [Bendory et al., 2020, p. 21](zotero://open-pdf/library/items/N4ZIHINK?page=21&annotation=P4C8QPVB)
