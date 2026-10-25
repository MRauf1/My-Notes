---
tags:
  - statistics
  - bayesian_statistics
---

# Definition

Choice of prior can be good or bad in terms of convergence, but as long as the convergence is guaranteed, the choice of prior doesn't have permanent impact.[^1]

# Types
- [[Conjugate Prior]]
- [[Noninformative Prior|Noninformative priors]], motivated by reducing the dependence of conclusions on the prior; e.g. [[Jeffreys Prior]].
- [[Weakly Informative Prior|Weakly informative priors]]: proper, deliberately weaker than available knowledge, enough to regularize.

# Properties
- A common criticism of the Bayesian approach is that priors are often selected for mathematical convenience rather than to reflect prior beliefs, and that conclusions are subjective through their dependence on the prior.[^2]
- Noninformative priors lead to difficulties when comparing different models, and Bayesian methods with poor priors can give poor results **with high confidence**; frequentist checks such as [[Cross-Validation]] offer some protection.[^2]
- **Setting the prior from the data** (e.g. matching the moments of the [[Prior Predictive Distribution]] to the observed data to fix [[Hyperparameter|hyperparameters]]) can be viewed as a rough approximation to [[Hierarchical Model|hierarchical modeling]], where hyperparameters are treated as unknowns and estimated in a fully Bayesian way. Moment matching itself is somewhat sloppy and hard to apply in general.[^3]
- Fairness can argue for deliberately ignoring relevant information, via a symmetry principle that the prior should not pull inferences in any predetermined direction.[^4]

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=54)
[^2]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=BX9FGPHT)
[^3]: [Gelman et al., p. 50](zotero://open-pdf/library/items/HDF44SF4?page=60&annotation=UIMSTEYR); [Gelman et al., p. 51](zotero://open-pdf/library/items/HDF44SF4?page=61&annotation=6T9BL9B7)
[^4]: [Gelman et al., p. 56](zotero://open-pdf/library/items/HDF44SF4?page=66&annotation=WIRN7K6Q)
