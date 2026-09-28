---
tags:
  - statistics
  - introduction_to_statistics
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
- [[Discrete Random Variable|Discrete Random Variable]]
- [[Continuous Random Variable|Continuous Random Variable]]
- [[Mixture Random Variable]]

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