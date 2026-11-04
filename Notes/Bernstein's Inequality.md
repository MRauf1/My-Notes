---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Bernstein's Inequality[^1]
> Let $X_1, \dots, X_n$ be independent with $X_i - \mathbb{E}[X_i] \leq M$ almost surely, and let $\sigma^2 := \frac{1}{n}\sum_{i=1}^n \mathrm{Var}(X_i)$. Then for $t > 0$
> $$
> \begin{align}
> P\left(\frac{1}{n}\sum_{i=1}^n (X_i - \mathbb{E}[X_i]) \geq t\right) \leq \exp\left(-\frac{n t^2}{2\sigma^2 + \frac{2}{3}Mt}\right).
> \end{align}
> $$
> Equivalently, with probability at least $1 - \delta$,
> $$
> \begin{align}
> \frac{1}{n}\sum_{i=1}^n (X_i - \mathbb{E}[X_i]) \leq \sqrt{\frac{2\sigma^2\log(1/\delta)}{n}} + \frac{2M\log(1/\delta)}{3n}.
> \end{align}
> $$

# Properties
- **Variance-adaptive.** The deviation is $\sqrt{\sigma^2/n}$ plus a lower-order $M/n$ term. When $\sigma^2 \ll M^2$, this beats [[Hoeffding's Inequality]], whose $\sqrt{M^2/n}$ deviation uses only the range. With $\sigma^2$ of the order of the range squared, the two agree up to constants.
- **Fast rates.** If $\sigma^2 \lesssim \mathbb{E}[X]$ (as for excess squared loss), the bound becomes self-bounding and gives $O(1/n)$ rates, e.g. the [[Fitted Q-Iteration Fast Rate]].
- Only an upper bound on $X_i - \mathbb{E}X_i$ is needed for this upper tail; apply it to $-X_i$ for the lower tail. Combine with [[Boole's Inequality]] for uniform bounds over finite classes.
- Proved by the Chernoff method ([[Markov's Inequality]] applied to $e^{\lambda S_n}$) with a [[Moment Generating Function]] bound that uses the variance.
- Saves a factor $\sqrt{K}$ over Hoeffding for the [[Inverse Propensity Score Estimator]], whose variance is of the order of its range $K$.

# Questions
> [!question]- Derive the high-probability form from the tail bound.
> Set the right side to $\delta$, writing $L = \log(1/\delta)$: one needs $nt^2 \geq L(2\sigma^2 + \frac{2}{3}Mt)$. Take $t = a + b$ with $a = \sqrt{2\sigma^2 L/n}$, $b = \frac{2ML}{3n}$. Then $n(a+b)^2 = na^2 + nb(a+b) + nab \geq 2\sigma^2 L + \frac{2}{3}ML(a+b)$, since $na^2 = 2\sigma^2 L$ and $nb = \frac{2}{3}ML$. So the tail probability at $t = a + b$ is at most $\delta$.

> [!question]- What is the proof idea, and where does the variance enter?
> By Markov, $P(\sum_i (X_i - \mathbb{E}X_i) \geq nt) \leq e^{-\lambda nt}\prod_i\mathbb{E}[e^{\lambda(X_i - \mathbb{E}X_i)}]$ using independence. For $Z = X - \mathbb{E}X \leq M$ with variance $v$, expanding $e^{\lambda Z} = 1 + \lambda Z + \lambda^2 Z^2\,\psi(\lambda Z)$ with $\psi(u) = (e^u - 1 - u)/u^2$ increasing gives $\mathbb{E}e^{\lambda Z} \leq 1 + \lambda^2 v\,\psi(\lambda M) \leq \exp(\lambda^2 v\,\psi(\lambda M))$. The variance enters here, where Hoeffding's lemma uses only the range. Bounding $\psi(u) \leq \frac{1}{2(1 - u/3)}$ for $0 \leq u < 3$ and optimizing over $\lambda$ gives the stated exponent.

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), p. 4](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=4)
