---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Signal (Signal Processing)[^1]
> A measurement of some physical quantity (light, sound, height, temperature, etc.) as a function of another independent quantity (time, space, wavelength, etc.). By convention, parentheses denote continuous variables and brackets denote discrete ones:
> - **Continuous signal**: $\ell(t)$ with $t \in \mathbb{R}$.
> - **Discrete signal**: a sequence $\ell[n]$ with $n \in \mathbb{Z}$, obtained from a continuous signal by [[Sampling (Signal Processing)|sampling]].

Most signals in nature are infinite continuous signals; once introduced into a computer they are sampled into a finite sequence of numbers (a discrete signal).

# Types
- **Infinite length**: extends over the entire support, $\ell[n]$ for $n \in (-\infty, \infty)$.
- **Finite length**: non-zero only on a finite interval $S$, i.e. $\ell[n] = 0$ for $n \notin S$.
- **Periodic**: there exists $N$ such that $\ell[n] = \ell[n + kN]$ for all $n$ and $k$ (discrete analogue of a [[Periodic Function]]); a periodic signal is an infinite length signal.
- **Finite energy** vs. **infinite energy**, according to its [[Signal Energy]].

# Properties
- A grayscale image is a 2D discrete signal $\ell[n, m]$, $n \in [0, N-1]$, $m \in [0, M-1]$ indexing the horizontal and vertical dimensions ([[Image Coordinate System]]), with each value the intensity at that location; a color image has three such channels.
- When analytical derivations are easier in the continuous domain (e.g. image gradients), images are written $\ell(x, y)$ and video sequences $\ell(x, y, t)$, and the result is then approximated in the discrete domain.
- The mean value of a signal is its [[DC Value]].
- Two signals of length $N$ can be compared with the (normalized) squared [[Euclidean Distance]]
$$
\begin{align}
D^2 = \frac{1}{N} \sum_{n=0}^{N-1} \left| \ell_1[n] - \ell_2[n] \right|^2
\end{align}
$$
  This is a poor metric for comparing the *content* of two images; better metrics (often L2 in a learned representation space rather than pixel space) are an active research area.
- Signals are transformed by a [[System (Signal Processing)|system]].
- Not to be confused with [[Signal (Computing)]].

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
