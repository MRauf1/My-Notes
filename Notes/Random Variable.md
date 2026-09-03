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

It induces a [[Image|Sample Space]] $D$ and [[Probability Distribution]] of $X$: $p_X(d_i) = P(\{c | X(c) = d_i\})$.

Empirically, for a [[Random Experiment|random experiment]] carried out $n$ times, the expectation is that the [[Probability|probability]] of an [[Event|event]] $A$ occurring should be close to the [[Relative Frequency|relative frequency]] of the event $A$.

# Types
- [[Discrete Random Variable|Discrete Random Variable]]
- [[Continuous Random Variable|Continuous Random Variable]]
- [[Mixture Random Variable]]

# Properties
- [[Quantile Function]]
- [[Random Variable Transformation]]

## Expectation Types
- [[Expectation]]
- [[Variance]]
- [[Moment Generating Function]]

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=50)