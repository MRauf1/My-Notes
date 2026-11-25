---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Rosenthal–Henderson Relation[^1]
> Model all losses of high-frequency signal (radiation damage, motion, alignment errors) by a Gaussian envelope $e^{-B k^2/4}$ on the Fourier amplitude at spatial frequency $k = 1/d$ ([[Resolution (Cryo-EM)|resolution]] $d$), where $B$ is the **B-factor** (in Å$^2$). Averaging $N$ particles raises the SNR by $\sqrt{N}$. Requiring a fixed SNR threshold at resolution $d$ then gives
> $$
> \begin{align}
> \ln N \approx \frac{B}{2}\,\frac{1}{d^2} + \text{const}.
> \end{align}
> $$
> The number of particles needed grows exponentially in $1/d^2$, and a plot of $\ln N$ against $1/d^2$ is a line of slope $B/2$.

# Properties
- **Derivation.** The SNR at frequency $k$ after averaging is $\propto \sqrt{N}\, e^{-Bk^2/4}$. Setting it equal to a threshold gives $\tfrac12 \ln N = \tfrac{B}{4}k^2 + c$.
- **Consequences.** A smaller $B$ (better data) is worth exponentially many particles. Every factor that raises $B$ in cryo-ET (dose splitting, thickness, tilt-geometry errors) makes [[Subtomogram Averaging]] need more particles than [[Single-Particle Analysis]] at the same resolution, while it usually has fewer.
- The same $B$ is the B-factor of the [[CTF Envelope Function]]. Good datasets have $B \approx 60$–$100$ Å$^2$.

[^1]: [Rosenthal & Henderson (2003), Optimal determination of particle orientation, absolute hand, and contrast loss in single-particle electron cryomicroscopy, J. Mol. Biol. 333:721–742](https://doi.org/10.1016/j.jmb.2003.07.013)
