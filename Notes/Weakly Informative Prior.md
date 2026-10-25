---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Weakly Informative Prior[^1][^2]
> A [[Prior Distribution]] that is proper but intentionally conveys weaker information than whatever actual prior knowledge is available. It contains enough information to **regularize** the [[Posterior Distribution]], keeping it roughly within reasonable bounds, without attempting to fully capture one's scientific knowledge about the parameter.

# Properties
- Two principles for constructing one, approaching from opposite directions (neither is pure):[^3]
  - Start from some [[Noninformative Prior]] and add enough information that inferences are constrained to be reasonable.
  - Start from a strong, highly informative prior and broaden it to account for uncertainty in one's prior beliefs and in the applicability of historically based priors to new data.
- Arguably virtually all statistical models are weakly informative: a model always conveys some information (choice of inputs, functional form), but it is neither possible nor perhaps desirable to encode all prior beliefs as probability distributions.[^3]
- Being proper, it avoids the propriety problems of [[Improper Prior|improper priors]].
- **Fairness / symmetry principle.** In some settings it is recommended **not** to use relevant information even when it would improve inferences, so that the prior does not pull inferences in any predetermined direction.[^4]

[^1]: [Gelman et al., p. 51](zotero://open-pdf/library/items/HDF44SF4?page=61&annotation=FEESI5NA)
[^2]: [Gelman et al., p. 55](zotero://open-pdf/library/items/HDF44SF4?page=65&annotation=R6IY9MLB)
[^3]: [Gelman et al., p. 55](zotero://open-pdf/library/items/HDF44SF4?page=65&annotation=IX3MF2YN)
[^4]: [Gelman et al., p. 56](zotero://open-pdf/library/items/HDF44SF4?page=66&annotation=WIRN7K6Q)
