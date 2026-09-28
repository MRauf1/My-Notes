---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Robustness to Distributional Shift[^1]
> The problem of ensuring that a machine learning system trained on a distribution $p_0$ "performs reasonably" on a different test distribution $p^*$, in the sense that (1) it often performs well on $p^*$, and (2) it knows when it is performing badly, ideally avoiding or mitigating the bad performance by taking conservative actions or soliciting human input.

# Properties
- A type of [[Accident (Machine Learning)|accident]]; the danger is silent, unpredictable failure on inputs very different from training data.[^1]
- When $p^* \neq p_0$, systems may not only perform poorly but also wrongly believe their performance is good.[^2]
- The simplest and most important failure is the brittle implicit contract of most ML systems: they only necessarily perform well if training and test distributions are identical, a condition that is hard to check and rare in practice. Systems should be built to perform well under weaker contracts that are easier to reason about.[^3]
- Approaches:[^4]
	- *Well-specified models*: covariate shift correction (e.g. importance weighting by $p^*(x)/p_0(x)$) and marginal likelihood, which require the model family to contain the truth.
	- *Partially specified models*: method of moments, unsupervised risk estimation, causal identification, and limited-information maximum likelihood, which make assumptions only about parts of the distribution.
	- *Training on multiple distributions*: train on many distributions so that a novel one is less likely to be out of reach.
	- *Responding when out-of-distribution*: detect novel inputs and take conservative actions or ask a human.
	- *Unifying view*: counterfactual reasoning and machine learning with contracts, i.e. systems with explicit, checkable guarantees on the conditions under which they perform well.
- Closely tied to [[Generalization]] beyond the training distribution.

[^1]: [Amodei et al., 2016, p. 3](zotero://open-pdf/library/items/JKJMXPTZ?page=3&annotation=W97US924); [Amodei et al., 2016, p. 3](zotero://open-pdf/library/items/JKJMXPTZ?page=3&annotation=BSPMFQ9P); [Amodei et al., 2016, p. 16](zotero://open-pdf/library/items/JKJMXPTZ?page=16&annotation=CX96LXPN)
[^2]: [Amodei et al., 2016, p. 16](zotero://open-pdf/library/items/JKJMXPTZ?page=16&annotation=RR8EH7KL)
[^3]: [Amodei et al., 2016, p. 19](zotero://open-pdf/library/items/JKJMXPTZ?page=19&annotation=P2UUPME9)
[^4]: [Amodei et al., 2016, p. 17](zotero://open-pdf/library/items/JKJMXPTZ?page=17&annotation=74N5R4IZ); [Amodei et al., 2016, p. 17](zotero://open-pdf/library/items/JKJMXPTZ?page=17&annotation=4P2F5YW6); [Amodei et al., 2016, p. 18](zotero://open-pdf/library/items/JKJMXPTZ?page=18&annotation=5T4MGMSU); [Amodei et al., 2016, p. 18](zotero://open-pdf/library/items/JKJMXPTZ?page=18&annotation=VGA5JYD7); [Amodei et al., 2016, p. 19](zotero://open-pdf/library/items/JKJMXPTZ?page=19&annotation=QDEBQXM6)
