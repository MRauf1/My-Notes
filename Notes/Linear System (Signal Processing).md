---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Linear System (Signal Processing)[^1]
> A [[System (Signal Processing)|system]] $f$ that is a [[Linear Map|linear map]]:
> $$
> \begin{align}
> f(\ell_1 + \ell_2) &= f(\ell_1) + f(\ell_2) \\
> f(a\ell) &= a f(\ell) \quad \text{for any scalar } a
> \end{align}
> $$
> For a 1D input of length $N$ and output of length $M$, its most general form is
> $$
> \begin{align}
> \ell_{\text{out}}[n] = \sum_{k=0}^{N-1} h[n, k] \, \ell_{\text{in}}[k], \quad n \in [0, M-1]
> \end{align}
> $$
> i.e. $\boldsymbol{\ell}_{\text{out}} = \mathbf{H} \boldsymbol{\ell}_{\text{in}}$ with $\mathbf{H} \in \mathbb{R}^{M \times N}$, $\mathbf{H}_{nk} = h[n, k]$ the weight of input sample $\ell_{\text{in}}[k]$ in output sample $\ell_{\text{out}}[n]$.

![[Hierarchy of Systems.png]]

# Types
- [[Shift-Invariant System|Linear translation invariant (LTI) system]]

# Properties
- In 2D, each output pixel is a linear combination of all input pixels:
$$
\begin{align}
\ell_{\text{out}}[n, m] = \sum_{k=0}^{M-1} \sum_{l=0}^{N-1} h[n, m, k, l] \, \ell_{\text{in}}[k, l]
\end{align}
$$
  which, after stacking the image columns into a long vector, is again $\boldsymbol{\ell}_{\text{out}} = \mathbf{H} \boldsymbol{\ell}_{\text{in}}$ ([[Matrix of Linear Map]]).
- Equivalent to a [[Linear Layer|fully connected layer]] with weights $\mathbf{W} = \mathbf{H}$: output unit $\ell_{\text{out}}[i]$ is the linear combination of the input with weights given by the $i$-th row of $\mathbf{H}$.
- A very small portion of all possible systems, yet capable of very rich image transformations; the [[Camera as Linear System|camera]] is one example.

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
