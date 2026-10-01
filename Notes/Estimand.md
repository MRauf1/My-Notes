---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Estimand[^1]
> An unobserved quantity for which [[Statistical Inference|statistical inferences]] are made.

The distinction between the two types is not always precise, but it shows how a statistical model for a problem fits into the real world.[^1]

# Types
- Potentially observable quantities: future observations of a process, or the outcome under the treatment not received ([[Causal Inference]]). Inference about them is predictive ([[Prior Predictive Distribution]], [[Predictive Distribution]]).[^1]
- Quantities not directly observable: parameters that govern the hypothetical process generating the data, e.g. regression coefficients. Inference about them is through the [[Posterior Distribution]].[^1]

# Properties
- An [[Estimator]] is a function of the data used to estimate an estimand; the estimand is the target, not the procedure.

[^1]: [Gelman et al., p. 4](zotero://open-pdf/library/items/HDF44SF4?page=14&annotation=B6N76VW4)
