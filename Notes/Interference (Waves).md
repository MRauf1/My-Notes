---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Interference (Waves)[^1]
> When waves of the same frequency overlap, the total wave is their sum ([[Superposition Principle (Partial Differential Equations)|superposition principle]]). Its intensity depends on their [[Phase (Waves)|phase]] difference $\Delta\varphi$:
> $$
> \begin{align}
> \big|A_1 e^{i\varphi_1} + A_2 e^{i\varphi_2}\big|^2 = A_1^2 + A_2^2 + 2A_1A_2\cos\Delta\varphi, \qquad \Delta\varphi = \varphi_1 - \varphi_2.
> \end{align}
> $$
> - **Constructive interference**, $\Delta\varphi = 0 \pmod{2\pi}$ (crest on crest): intensity $(A_1 + A_2)^2$.
> - **Destructive interference**, $\Delta\varphi = \pi \pmod{2\pi}$ (crest on trough): intensity $(A_1 - A_2)^2$.

# Properties
- The cross-term $2A_1A_2\cos\Delta\varphi$ is the only place where phase becomes visible in intensity. Holography, phase-contrast microscopy and the [[Contrast Transfer Function]] all rely on it.
- [[Diffraction]] is interference of the waves scattered from many points. Its directions satisfy path difference $= n\lambda$, e.g. $d\sin\theta = n\lambda$ for a period-$d$ object.
- Interfering [[Plane Wave|plane waves]] produce straight fringes.
- Interference requires *coherence*, a stable phase relation between the waves. Incoherent waves add intensities instead, since the cross-term averages to zero.

# Questions
> [!question]- Why do incoherent waves add intensities instead of amplitudes?
> If the phase difference $\Delta\varphi$ fluctuates randomly and uniformly over $[0, 2\pi)$ during the measurement, the time-averaged cross-term is $2A_1A_2\,\mathbb{E}[\cos\Delta\varphi] = 0$. The observed intensity is then $A_1^2 + A_2^2$. This is why the spatial coherence of the electron source matters in cryo-EM ([[CTF Envelope Function]]).

[^1]: [Wave interference (Wikipedia)](https://en.wikipedia.org/wiki/Wave_interference)
