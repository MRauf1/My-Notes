---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Uniform Deviation Bound[^1]
> For a [[Hypothesis Space|hypothesis class]] $\mathcal{F}$, a bound, holding with high probability over an i.i.d. sample of size $n$, on the largest gap between true and empirical risk over the class:
> $$
> \begin{align}
> \max_{f \in \mathcal{F}} \Big|\mathbb{E}[\ell(f)] - \widehat{\mathbb{E}}[\ell(f)]\Big|
> \end{align}
> $$
> where $\mathbb{E}[\ell(f)]$ is the expected loss (e.g. $\mathbb{E}[\mathbb{I}[f(X) \neq Y]]$) and $\widehat{\mathbb{E}}[\ell(f)] = \frac{1}{n}\sum_{i=1}^n \ell(f; X_i, Y_i)$ is its empirical average.

# Properties
- **Reduces excess risk of ERM to uniform deviation.** For the [[Empirical Risk Minimization|ERM]] solution $\hat{f}$ and the population minimizer $f^\star$:
$$
\begin{align}
\mathbb{E}[\ell(\hat{f})] - \mathbb{E}[\ell(f^\star)] &\leq \big(\mathbb{E}[\ell(\hat{f})] - \widehat{\mathbb{E}}[\ell(\hat{f})]\big) + \big(\widehat{\mathbb{E}}[\ell(f^\star)] - \mathbb{E}[\ell(f^\star)]\big) \\
&\leq 2 \max_{f \in \mathcal{F}} \big|\mathbb{E}[\ell(f)] - \widehat{\mathbb{E}}[\ell(f)]\big|
\end{align}
$$
  The first step adds $\widehat{\mathbb{E}}[\ell(f^\star)] - \widehat{\mathbb{E}}[\ell(\hat{f})] \geq 0$, because $\hat{f}$ is optimal for $\widehat{\mathbb{E}}$.
- *Uniform* is essential: $\hat{f}$ depends on the sample, so a deviation bound for each fixed $f$ does not apply to $\hat{f}$ itself.
- For finite $\mathcal{F}$ and bounded loss, [[Hoeffding's Inequality]] plus the union bound ([[Boole's Inequality]]) gives the [[Finite Hypothesis Class Generalization Bound]].
- In RL, a uniform deviation bound over pairs $(f, f') \in \mathcal{F}^2$ of the regression loss drives the [[Fitted Q-Iteration Error Bound]].
- Bounds the gap between training and test risk, i.e. the [[Generalization Error]] relative to the training error, simultaneously for every $f$.

[^1]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), p. 4](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=4)
