---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

Given data, for a chosen [[Probability Distribution]], the likelihood function is the probability of the data as a [[Function]] of an unknown parameter.

For an unknown parameter $\beta$, the likelihood function is denoted as $l(\beta)$.

The part of the likelihood function involving the parameters is called the kernel.[^1]

> [!info] Definition 1 (Likelihood of a Random Sample)[^4]
> For a [[Random Sample]] $X_1, \dots, X_n$ from $f(x; \theta)$, $\theta \in \Omega$, the joint pdf viewed as a function of $\theta$ for the fixed observed data is the likelihood function
> $$
> \begin{align}
> L(\theta) = L(\theta; x_1, \dots, x_n) = \prod_{i=1}^n f(x_i; \theta)
> \end{align}
> $$

# Properties
- $p(\mathcal{D} | \mathbf{w})$ expresses how probable the observed data set is for different settings of $\mathbf{w}$; it is **not** a probability distribution over $\mathbf{w}$, and its integral with respect to $\mathbf{w}$ need not equal one.[^2]
- In [[Bayes' Theorem]], posterior $\propto$ likelihood $\times$ prior, all viewed as functions of $\mathbf{w}$.
- Central to both the [[Probability Bayesian Framework|Bayesian]] and [[Probability Frequentist Framework|frequentist]] paradigms, though used in fundamentally different ways.
- For [[Independent and Identically Distributed|i.i.d.]] data it factorizes, e.g. $p(\mathbf{x} | \mu, \sigma^2) = \prod_{n=1}^N \mathcal{N}(x_n | \mu, \sigma^2)$ for a Gaussian ([[Normal Distribution Maximum Likelihood Estimation]]).[^3]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=27)
[^2]: [Bishop, 2006, p. 22](zotero://open-pdf/library/items/5G99AZ8U?page=42&annotation=J77YU8CI)
[^3]: [Bishop, 2006, p. 26](zotero://open-pdf/library/items/5G99AZ8U?page=46&annotation=N2Q47J9S)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=242)
