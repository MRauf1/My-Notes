---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Combinatorial Explosion[^1]
> The rapid (typically exponential) growth in the number of possibilities that must be explored by methods relying on something like exhaustive search, as problems become larger or harder.

# Properties
- A key reason early (GOFAI) demonstration systems proved difficult to extend to wider or harder problems.[^1]
- Overcoming it requires algorithms that exploit structure in the target domain and prior knowledge, via [[Heuristic|heuristic]] search, planning, and flexible abstract representations.[^1]
- Also defeats idealised [[Bayesian Inference|Bayesian]] agents: an agent with a prior favouring simpler possible worlds (e.g. by Kolmogorov complexity, the length of the shortest program generating a world's description) plus programmer-supplied background knowledge is computationally intractable to build exactly.[^2]
- Relating domain-specific learning problems to general Bayesian inference means efficiency improvements to inference yield immediate gains across many areas, part of a broader unification of disparate techniques in a common mathematical framework.[^3]
- Compare the [[Bitter Lesson]] on search and learning that scale with computation.

[^1]: [Bostrom, 2014, p. 6](zotero://open-pdf/library/items/9ECZCLTQ?page=23&annotation=W8L5976Z); [Bostrom, 2014, p. 6](zotero://open-pdf/library/items/9ECZCLTQ?page=23&annotation=6EYXYCL2)
[^2]: [Bostrom, 2014, p. 10](zotero://open-pdf/library/items/9ECZCLTQ?page=27&annotation=BHI6BJNV); [Bostrom, 2014, p. 11](zotero://open-pdf/library/items/9ECZCLTQ?page=28&annotation=VPLSINRH)
[^3]: [Bostrom, 2014, p. 9](zotero://open-pdf/library/items/9ECZCLTQ?page=26&annotation=6MJYFJC5); [Bostrom, 2014, p. 9](zotero://open-pdf/library/items/9ECZCLTQ?page=26&annotation=53H7MCEJ)
