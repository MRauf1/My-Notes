---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Convolution Basic Properties[^1]
> For discrete signals and the [[Convolution|convolution]] $\circ$:
> - **Commutative**: $h[n] \circ \ell[n] = \ell[n] \circ h[n]$.
> - **Associative**: $\ell_1[n] \circ \ell_2[n] \circ \ell_3[n] = \ell_1[n] \circ (\ell_2[n] \circ \ell_3[n]) = (\ell_1[n] \circ \ell_2[n]) \circ \ell_3[n]$.
> - **Distributive** over addition: $\ell_1[n] \circ (\ell_2[n] + \ell_3[n]) = \ell_1[n] \circ \ell_2[n] + \ell_1[n] \circ \ell_3[n]$.
> - **Shift**: if $\ell_{\text{out}}[n] = h[n] \circ \ell_{\text{in}}[n]$, then for any $n_0$
> $$
> \begin{align}
> \ell_{\text{out}}[n - n_0] = h[n] \circ \ell_{\text{in}}[n - n_0] = h[n - n_0] \circ \ell_{\text{in}}[n]
> \end{align}
> $$
> - **Support**: convolving a signal of length $N$ with a signal of length $M$ gives a signal of length $L \leq M + N - 1$.
> - **Identity**: the discrete impulse $\delta[n]$ ($1$ at $n = 0$, $0$ elsewhere; a [[Kronecker Delta]]) satisfies $\delta[n] \circ \ell[n] = \ell[n]$.

The same properties hold for continuous signals, with the [[Dirac Delta Function]] as identity.

# Properties
- Commutativity follows from the change of variables $k = n - k'$:
$$
\begin{align}
h[n] \circ \ell_{\text{in}}[n] = \sum_{k=-\infty}^{\infty} h[n - k] \, \ell_{\text{in}}[k] = \sum_{k'=-\infty}^{\infty} h[k'] \, \ell_{\text{in}}[n - k'] = \ell_{\text{in}}[n] \circ h[n]
\end{align}
$$
  Hence the order of convolutions is irrelevant, which is not true for [[Cross Correlation (Signal Processing)|cross-correlation]].
- For finite length signals, associativity may be broken by how boundary conditions ([[Padding (Convolution)|padding]]) are implemented.
- The shift property is the translation [[Equivariant Function|equivariance]] of convolution ([[Shift-Invariant System]]).
- Commutativity, associativity and distributivity make (absolutely summable) signals under $+$ and $\circ$ a commutative ring with identity $\delta$.[^2]

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: Added from general knowledge.
