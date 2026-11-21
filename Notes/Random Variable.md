---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Random Variable)[^1]
> Given a [[Random Experiment|random experiment]] with an [[Universe of Discourse|outcome space]] $S$, the random variable is the [[Function|function]] $X: S \rightarrow \mathbb{R}$ that assigns a [[Real Number|real number]] $X(s) = x$ for each $s \in S$.
> The space/support of $X$ is the [[Image|image]] of the function $X$, i.e. it is the [[Set|set]] $D = \{x \in \mathbb{R} | X(s) = x, \forall s \in S\}$.

Random variable is a ([[Deterministic|deterministic]]) function that enumerates the outcomes of a random experiment (maps the outcomes of a random experiment to real numbers).

It induces a new [[Sample Space]] $\mathcal{D}$ (its range) and a probability on it, the [[Probability Distribution|distribution]] of $X$:[^2]
$$
\begin{align}
P_X(D) = P(\{c \in \mathcal{C} : X(c) \in D\}), \quad D \subseteq \mathcal{D}
\end{align}
$$
which in the discrete case is $P_X(D) = \sum_{d_i \in D} p_X(d_i)$ with $p_X(d_i) = P(\{c : X(c) = d_i\})$, and in the continuous case $P_X[(a, b)] = \int_a^b f_X(x)\,dx$. $P_X$ is fully described by the [[Cumulative Distribution Function]]. $\mathcal{D}$ is typically a [[Countable Set|countable]] set (discrete) or an interval of reals (continuous).

Empirically, for a [[Random Experiment|random experiment]] carried out $n$ times, the expectation is that the [[Probability|probability]] of an [[Event|event]] $A$ occurring should be close to the [[Relative Frequency|relative frequency]] of the event $A$.

# Types
By the Lebesgue decomposition, every distribution on $\mathbb{R}$ splits uniquely as a convex combination of three pure types,[^3]
$$
\begin{align}
P_X = \alpha_d P_d + \alpha_{ac} P_{ac} + \alpha_{sc} P_{sc}, \qquad \alpha_d, \alpha_{ac}, \alpha_{sc} \geq 0, \quad \alpha_d + \alpha_{ac} + \alpha_{sc} = 1
\end{align}
$$
so this list is exhaustive:
- [[Discrete Random Variable|Discrete Random Variable]] ($\alpha_d = 1$): all mass on countably many atoms; has a pmf; the cdf is a step function.
- Absolutely continuous ($\alpha_{ac} = 1$): has a [[Probability Density Function|pdf]]; [[Absolutely Continuous Measure|absolutely continuous]] with respect to [[Lebesgue Measure]]. This is what Hogg calls "continuous".
- Singular continuous ($\alpha_{sc} = 1$): no atoms and no pdf; all mass on a Lebesgue-null set ([[Mutually Singular Measures|singular]] with respect to Lebesgue measure). The cdf is continuous but $F' = 0$ a.e., e.g. the Cantor distribution with cdf the [[Cantor Function]].
- [[Continuous Random Variable|Continuous Random Variable]] in the strict sense (continuous cdf) means $\alpha_d = 0$: absolutely continuous, singular continuous, or a mix of the two.
- [[Mixture Random Variable]]: two or more of the $\alpha$'s positive. Hogg's mixtures have $\alpha_d, \alpha_{ac} > 0$.

A statement proved separately for discrete $X$ (sums) and absolutely continuous $X$ (integrals) has not been proved for every $X$. The measure-theoretic definition $E[g(X)] = \int g(X)\,dP$ covers all cases at once.

# Properties
- [[Random Variable Support]]
- [[Random Variables Equal in Distribution]]
- [[Quantile Function]]
- [[Random Variable Transformation]]

## Expectation Types
- [[Expectation]]
- [[Variance]]
- [[Moment Generating Function]]
- [[Moment (Statistics)]]

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=50)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=53)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=119)