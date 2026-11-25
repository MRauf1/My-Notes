---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Sinusoidal Wave (Harmonic Wave)[^1]
> A [[Wave]] whose profile is a sinusoid:
> $$
> \begin{align}
> u(x, t) = A\cos(kx - \omega t + \varphi_0), \qquad \text{or in complex form } u = \operatorname{Re}\big(A e^{i(kx - \omega t + \varphi_0)}\big),
> \end{align}
> $$
> with [[Amplitude (Wave)|amplitude]] $A$, [[Wavenumber|wavenumber]] $k = 2\pi/\lambda$ ([[Wavelength]] $\lambda$), angular [[Frequency (Waves)|frequency]] $\omega = 2\pi f$, and [[Phase (Waves)|phase]] $kx - \omega t + \varphi_0$ with initial phase $\varphi_0$.

At a fixed time it is a sinusoid in space with period $\lambda$; at a fixed point it is a sinusoid in time with period $T = 1/f$. The whole pattern moves at the [[Phase Velocity|phase velocity]] $v_p = \omega/k = \lambda f$.

# Properties
- Its maxima and minima are the [[Crest and Trough|crests and troughs]].
- It is a [[Periodic Function]] in both $x$ (period $\lambda$) and $t$ (period $T$).
- The complex form is preferred in physics and Fourier analysis, because shifts and derivatives act by multiplication: $\partial_x \mapsto ik$, $\partial_t \mapsto -i\omega$, and a [[Phase Shift|phase shift]] multiplies by $e^{i\Delta\varphi}$ ([[Complex Exponential Function]]).
- In time-only form it is the [[Sinusoid (Signal Processing)|sinusoid]] of signal processing.

[^1]: [Sinusoidal wave (Wikipedia)](https://en.wikipedia.org/wiki/Sine_wave)
