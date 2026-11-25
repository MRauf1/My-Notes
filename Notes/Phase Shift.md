---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Phase Shift[^1]
> A change $\Delta\varphi$ in the [[Phase (Waves)|phase]] of a [[Sinusoidal Wave]]:
> $$
> \begin{align}
> A\cos(kx - \omega t + \varphi_0) \ \longmapsto\ A\cos(kx - \omega t + \varphi_0 + \Delta\varphi).
> \end{align}
> $$
> For a wave of fixed wavenumber it is equivalent to a **spatial translation** by $-\Delta\varphi/k$ (a fraction $\Delta\varphi/2\pi$ of a [[Wavelength|wavelength]]), or a **time shift** by $\Delta\varphi/\omega$. In complex form it is multiplication by $e^{i\Delta\varphi}$.

# Properties
- **Accumulated phase.** If the local [[Wavenumber|wavenumber]] $k(x)$ varies along the path, the phase is $\int k\,dx$, not $kx$. A region where $k$ differs from $k_0$ leaves a permanent phase shift $\Delta\varphi = \int (k(x) - k_0)\,dx$, even though the wave regains wavelength $2\pi/k_0$ beyond it. This is how a cryo-EM specimen phase-shifts the electron wave: $\Delta\varphi(x,y) = \sigma\int V\,dz$ ([[Projection Approximation]]).
- A phase shift alone does not change intensity. It becomes visible only through [[Interference (Waves)|interference]] with another wave, which is why phase-contrast imaging needs defocus or a phase plate ([[Contrast Transfer Function]]).
- **The Fourier shift theorem:** translating a signal multiplies each Fourier component by a phase factor that is linear in frequency.

# Questions
> [!question]- Why is a phase shift $\Delta\varphi$ the same as a translation, and by how much?
> $\cos(kx - \omega t + \varphi_0 + \Delta\varphi) = \cos\big(k(x + \Delta\varphi/k) - \omega t + \varphi_0\big)$. So the shifted wave equals the original evaluated at $x + \Delta\varphi/k$, i.e. the graph translated by $-\Delta\varphi/k$. This uses a single fixed $k$. If $k$ varies along the path, the phase is $\int k\,dx$, and the shift is the accumulated excess $\int(k - k_0)\,dx$.

> [!question]- If a phase shift is invisible to an intensity detector, how can a pure phase object be imaged?
> Its exit wave is $e^{i\Delta\varphi(x)} \approx 1 + i\Delta\varphi(x)$. The intensity is $|1 + i\Delta\varphi|^2 = 1 + \Delta\varphi^2$: no first-order signal, because the scattered part $i\Delta\varphi$ is $90°$ out of phase with the unscattered $1$. Adding a further phase between scattered and unscattered waves (defocus, or a phase plate shifting by $\pi/2$) rotates $i\Delta\varphi$ toward the real axis, and the intensity becomes $1 \pm 2\Delta\varphi$ to first order.

[^1]: [Phase (waves) (Wikipedia)](https://en.wikipedia.org/wiki/Phase_(waves))
