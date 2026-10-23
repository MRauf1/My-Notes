---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Probability Function|Probability]] Density Function)[^1][^2]
> For an (absolutely) [[Continuous Random Variable]] $X$, a pdf is a function $f_X$ such that
> $$
> \begin{align}
> F_X(x) = \int_{-\infty}^x f_X(t)\,dt
> \end{align}
> $$
> where $F_X$ is the [[Cumulative Distribution Function]]. Probabilities are computed by [[Riemann Integral|integration]]: $P(a < X \leq b) = \int_a^b f_X(t)\,dt$, the area under $y = f_X(x)$ between $a$ and $b$.

If $f_X$ is continuous at $x$, the [[Fundamental Theorem of Calculus]] gives $\frac{d}{dx} F_X(x) = f_X(x)$. The density value itself is not a probability: $P(X = x) = 0$ for all $x$, while $f_X(x)$ can be any nonnegative number.

**Mass vs. density.** A [[Probability Mass Function|pmf]] value is a probability *mass*; a pdf value is a probability *density*, i.e. mass per unit volume (length in 1D, volume in $\mathbb{R}^D$). For almost every $\mathbf{x}$ ([[Lebesgue Measure|Lebesgue]] differentiation),[^3]
$$
\begin{align}
f_X(\mathbf{x}) = \lim_{\varepsilon \to 0} \frac{P\left(X \in B_\varepsilon(\mathbf{x})\right)}{\operatorname{vol}\left(B_\varepsilon(\mathbf{x})\right)}
\end{align}
$$
so a density has no upper bound: a fixed amount of mass squeezed into a vanishing volume has density tending to $\infty$. More generally, a pdf is the Radon-Nikodym derivative $dP_X / d\lambda$ with respect to Lebesgue measure $\lambda$, and it exists only if $P_X$ is [[Absolutely Continuous Measure|absolutely continuous]] ($\lambda(A) = 0 \Rightarrow P_X(A) = 0$). A purely discrete distribution, or one concentrated on a lower-dimensional manifold (a set of volume zero), is [[Mutually Singular Measures|singular]] with respect to $\lambda$ and has no pdf; it behaves like a [[Dirac Delta Function|Dirac delta]] of "infinite density" there. Objectives built on density values, such as [[Maximum Likelihood Estimation|maximum likelihood]] for continuous models (e.g. [[Normalizing Flow|normalizing flows]]), then become ill-posed, since the likelihood can be driven to $+\infty$ ([[Maximum Likelihood Loss Optimality and Failure Modes]]).

# Properties
- [[Probability Density Function Definitional Properties]]: $f_X(x) \geq 0$ and $\int_{-\infty}^\infty f_X(t)\,dt = 1$.
- Not unique: changing $f_X$ at countably many points (more generally, on a set of length zero) leaves every probability unchanged.
- Its positive set is the [[Random Variable Support|support]].
- Transforms under $Y = g(X)$ via the Jacobian ([[Cumulative Distribution Function Transformation Technique]]).

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=52)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=65)
[^3]: Supplementary notes provided by the creator.
