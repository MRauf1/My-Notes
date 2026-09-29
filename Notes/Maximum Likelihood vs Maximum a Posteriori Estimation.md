---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Maximum Likelihood vs Maximum a Posteriori Estimation[^1][^2]
> Both return a single point estimate of the parameters $\mathbf{w}$ from data $\mathcal{D}$:
> $$
> \begin{align}
> \mathbf{w}_{\mathrm{ML}} &= \underset{\mathbf{w}}{\arg\max}\; \ln p(\mathcal{D} | \mathbf{w}) \\
> \mathbf{w}_{\mathrm{MAP}} &= \underset{\mathbf{w}}{\arg\max}\; \ln p(\mathbf{w} | \mathcal{D}) = \underset{\mathbf{w}}{\arg\max}\; \big[\ln p(\mathcal{D} | \mathbf{w}) + \ln p(\mathbf{w})\big]
> \end{align}
> $$
> MAP is maximum likelihood plus a log-prior penalty; the evidence $p(\mathcal{D})$ does not depend on $\mathbf{w}$ and drops out. With a uniform (flat) prior, MAP reduces to maximum likelihood.

[[Maximum Likelihood Estimation|Maximum likelihood]] is a frequentist estimator: $\mathbf{w}$ is a fixed unknown and $p(\mathcal{D} | \mathbf{w})$ is the probability of the observed data. MAP ([[Maximum a Posteriori Learning]]) maximizes the posterior of [[Bayes' Theorem]] but, being a point estimate, is not yet a full Bayesian treatment, which would instead marginalize over $\mathbf{w}$ ([[Predictive Distribution]]).

# Properties
## Maximum Likelihood
- Advantages:
	- Requires no prior, so it is objective in the sense of depending only on the data and the model.
	- Invariant to reparametrization: if $\hat{\theta}$ is the ML estimate of $\theta$, then $g(\hat{\theta})$ is the ML estimate of $g(\theta)$.
	- Under regularity conditions, consistent, asymptotically normal, and asymptotically efficient ([[Maximum Likelihood Estimation Properties]]).
	- Equivalent to minimizing the [[Kullback-Leibler Divergence]] from the data distribution to the model, and to minimizing the usual error functions (least squares, [[Cross-Entropy Loss|cross-entropy]]).
- Disadvantages:
	- [[Overfitting|Over-fits]] when data is scarce relative to model flexibility; the training likelihood always increases with complexity, so it cannot select complexity by itself.
	- Gives extreme estimates from small samples: three heads in three tosses gives $P(\text{heads}) = 1$.[^3]
	- Systematically biased for some quantities, e.g. it underestimates variance by a factor $(N-1)/N$ ([[Normal Distribution Maximum Likelihood Estimation]]).
	- Can be degenerate: the likelihood may be unbounded (e.g. a Gaussian mixture component collapsing onto a single point).

## Maximum a Posteriori
- Advantages:
	- Incorporates prior knowledge naturally; a Gaussian prior yields [[L2 Regularization]] with $\lambda = \alpha/\beta$, and a Laplace prior yields [[L1 Regularization]].
	- Reduces over-fitting and stabilizes small-sample estimates (e.g. a [[Beta Distribution|Beta]] prior acts as pseudo-counts, pulling the coin estimate away from $1$), and removes likelihood degeneracies.
	- Converges to the ML estimate as $N \to \infty$, since the likelihood term grows with $N$ while the prior term does not.
	- Costs the same as ML: one optimization, with an extra penalty term.
- Disadvantages:
	- Depends on the choice of prior and its [[Hyperparameter|hyperparameters]], which are often chosen for convenience and must still be tuned (e.g. by [[Cross-Validation]]).
	- **Not** invariant to reparametrization: the mode of a density moves under a nonlinear change of variables because of the Jacobian, so MAP answers depend on the parametrization.
	- Still a point estimate: it discards parameter uncertainty, so its predictive variance contains only the noise term.
	- The mode can be unrepresentative of the posterior, especially in high dimensions where most posterior mass lies far from the mode ([[Curse of Dimensionality]]).

[^1]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=4KU9QTLZ)
[^2]: [Bishop, 2006, p. 30](zotero://open-pdf/library/items/5G99AZ8U?page=50&annotation=AVFP5PDR)
[^3]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=I67L46V2)
