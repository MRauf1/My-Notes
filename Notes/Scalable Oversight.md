---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Scalable Oversight[^1]
> The problem of ensuring safe behaviour of a machine learning system when the correct objective function is known, or can be evaluated (e.g. by consulting a human), but is too expensive to evaluate frequently, so that the system must rely on cheap proxy signals and extrapolate from limited samples of the true objective.

# Properties
- A type of [[Accident (Machine Learning)|accident]] arising from bad extrapolation from limited samples.
- Cheap proxy signals can be evaluated efficiently during training but do not perfectly track what we care about; this divergence exacerbates [[Negative Side Effects (Machine Learning)|negative side effects]] (penalised by the true objective but omitted from the proxy) and [[Reward Hacking|reward hacking]] (which thorough oversight would recognise).[^2]
- Can be ameliorated by exploiting a limited oversight budget more efficiently, e.g. combining limited calls to the true objective with frequent calls to an imperfect proxy that is given or learned.[^2]
- Frameworks:
	- [[Semi-Supervised Reinforcement Learning]], the main proposed framework.[^2]
	- *Distant supervision*: provide useful information about the system's decisions in aggregate, or noisy hints about correct evaluations, rather than per-decision labels.[^3]
	- *Hierarchical reinforcement learning*: a top-level agent takes few, highly abstract actions over long timescales and delegates to sub-agents whose rewards it assigns, so that oversight is only needed at the sparse top level.[^3]

[^1]: [Amodei et al., 2016, p. 3](zotero://open-pdf/library/items/JKJMXPTZ?page=3&annotation=VUX89RGI); [Amodei et al., 2016, p. 3](zotero://open-pdf/library/items/JKJMXPTZ?page=3&annotation=YRG9BHC5)
[^2]: [Amodei et al., 2016, p. 11](zotero://open-pdf/library/items/JKJMXPTZ?page=11&annotation=WBWJYC54); [Amodei et al., 2016, p. 11](zotero://open-pdf/library/items/JKJMXPTZ?page=11&annotation=723JIFE6)
[^3]: [Amodei et al., 2016, p. 13](zotero://open-pdf/library/items/JKJMXPTZ?page=13&annotation=XEIDMJ3X); [Amodei et al., 2016, p. 13](zotero://open-pdf/library/items/JKJMXPTZ?page=13&annotation=PNWL2NK7); [Amodei et al., 2016, p. 13](zotero://open-pdf/library/items/JKJMXPTZ?page=13&annotation=QJHKPWAS)
