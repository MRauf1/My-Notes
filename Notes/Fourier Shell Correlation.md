---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Fourier Shell Correlation (FSC)[^1]
> Split the particles into two random halves and reconstruct each independently, giving $\hat f_1, \hat f_2$. For each spherical shell $|k| \approx k_0$ in Fourier space,
> $$
> \begin{align}
> \text{FSC}(k_0) = \frac{\sum_{|k| \approx k_0} \hat f_1(k)\, \overline{\hat f_2(k)}}{\sqrt{\sum_{|k| \approx k_0} |\hat f_1(k)|^2 \;\sum_{|k| \approx k_0} |\hat f_2(k)|^2}} .
> \end{align}
> $$
> The reported ("gold-standard") [[Resolution (Cryo-EM)|resolution]] is $d = 1/k_0$ at the first $k_0$ where $\text{FSC}(k_0) < 0.143$.

# Properties
- $\text{FSC} \approx 1$ at low $k$, where the halves agree, and $\text{FSC} \to 0$ at high $k$, where they share only noise. Signal is what two independent estimates agree on, the same idea as [[Cross-Validation]].
- The halves must be refined independently. Otherwise noise aligned to a common reference correlates, and the resolution is overestimated.
- Map–model FSC compares a map with the map simulated from an [[Atomic Model]].
- Its weaknesses as a validation tool are covered in [[Cryo-EM Validation]].

# Questions
> [!question]- If each half-map is $\hat f_i = S + N_i$ on a shell, with independent zero-mean noise of equal power, what does the FSC estimate?
> In expectation, the cross-term is $\sum |S|^2$ (the noise terms are uncorrelated with the signal and with each other), and each denominator sum is $\sum |S|^2 + \sum |N|^2$. So $\text{FSC} \approx \dfrac{\text{SNR}_{1/2}}{1 + \text{SNR}_{1/2}}$, where $\text{SNR}_{1/2} = \sum|S|^2 / \sum|N|^2$ is the per-shell SNR of a half-map. It is a monotone function of the SNR, so a threshold on the FSC is a threshold on the shell SNR.

[^1]: [Rosenthal & Henderson (2003), Optimal determination of particle orientation, absolute hand, and contrast loss in single-particle electron cryomicroscopy, J. Mol. Biol. 333:721–742](https://doi.org/10.1016/j.jmb.2003.07.013)
