---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Probability Space[^1]
> A probability space is a triple $(\Omega, \mathcal{F}, P)$: a sample space $\Omega$, a $\sigma$-algebra $\mathcal{F}$ of events, and a probability [[Measure (Measure Theory)|measure]] $P$ with $P(\Omega) = 1$. A [[Random Variable]] $X$ takes values in $\Omega$ with $\mathbb{P}[X \in E] = P(E)$.

$P$ is a measure, so the [[Lebesgue Integral (Measure Theory)|Lebesgue integral]] applies to it directly, including for [[Expectation]]:
$$
\begin{align}
\mathbb{E}[f(X)] = \int_\Omega f(x)\, dP(x)
\end{align}
$$
Discrete and continuous random variables share this one formula. When $P$ admits a [[Density with Respect to a Measure|density]] $p$ with respect to a reference measure $\mu$ (that is, $dP = p\,d\mu$), this recovers the familiar
$$
\begin{align}
\mathbb{E}[f(X)] = \int_\Omega f(x)\,p(x)\,d\mu(x)
\end{align}
$$

# Properties
- Generalizes the separate discrete-sum and continuous-integral definitions of [[Expectation]] into one Lebesgue integral.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
