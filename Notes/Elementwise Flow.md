---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Elementwise Flow[^1]
> A nonlinear [[Normalizing Flow|normalizing flow]] layer that applies the same invertible pointwise function $\mathrm{f}[\bullet, \boldsymbol{\phi}]$ to each element of the input:
> $$
> \begin{align}
> \mathbf{f}[\mathbf{h}] = \left[\mathrm{f}[h_1, \boldsymbol{\phi}], \mathrm{f}[h_2, \boldsymbol{\phi}], \dots, \mathrm{f}[h_D, \boldsymbol{\phi}]\right]^T
> \end{align}
> $$
> Since the $d$-th input only affects the $d$-th output, the [[Jacobian Matrix]] is [[Diagonal Matrix|diagonal]] and
> $$
> \begin{align}
> \left|\frac{\partial \mathbf{f}[\mathbf{h}]}{\partial \mathbf{h}}\right| = \prod_{d=1}^D \left|\frac{\partial \mathrm{f}[h_d]}{\partial h_d}\right|
> \end{align}
> $$

# Types
- **Fixed nonlinearity**: an invertible activation with no parameters, such as the [[Leaky ReLU]].[^1]
- **Piecewise linear** with $K$ bins, mapping $[0, 1] \to [0, 1]$:[^2]
$$
\begin{align}
\mathrm{f}[h, \boldsymbol{\phi}] = \left(\sum_{k=1}^{b-1} \phi_k\right) + (hK - b + 1)\phi_b, \qquad b = \lfloor Kh \rfloor + 1
\end{align}
$$
  where $\phi_1, \dots, \phi_K > 0$ sum to one and $b$ is the index of the bin containing $h$. The first term sums the preceding bins and the second is the proportion of the way through the current bin. It is easy to invert and differentiable almost everywhere, with slope $K\phi_b$ in bin $b$.
- **Monotonic splines**: smooth parameterized functions whose parameters ensure the function is [[Monotonic Function|monotonic]] and hence invertible.[^2]

# Properties
- Any strictly monotonic $\mathrm{f}$ works, since it is a [[Bijective Function|bijection]] onto its image.
- **No mixing**: nonlinear but does not mix input dimensions, so it cannot create correlations between variables. Alternating with [[Linear Flow|linear flows]] (which mix dimensions) models more complex transformations, but in practice elementwise flows serve as components of more complex layers, e.g. as the invertible transformer $\mathbf{g}$ in [[Coupling Flow|coupling]] and [[Autoregressive Flow|autoregressive flows]].[^2]

[^1]: [Prince, p. 310](zotero://open-pdf/library/items/BWT7FYX5?page=324&annotation=PX9H4FAI)
[^2]: [Prince, p. 311](zotero://open-pdf/library/items/BWT7FYX5?page=325&annotation=UBA3APKL)
