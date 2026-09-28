---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Algorithmic Systems Biology[^1]
> The modelling of biological systems with formal, executable languages from computer science (e.g. process calculi for concurrency) that can be automatically translated into code and support simulation and analysis techniques for proving properties of biological systems.

# Properties
- **Causality vs. precedence**: in concurrent languages, activity $A$ causes activity $B$ iff $A$ is a necessary condition for $B$ *and* $A$ influences $B$ (information flows from $A$ to $B$). Causality is thus a subset of temporal ordering; a list of reactions gives only temporal, not causal, information, so dedicated tools are needed.[^1]
- Causality helps dissect independent components, simplify models, and identify cross-talk between signalling cascades.[^2]
- Challenges: relating local interactions to emergent global behaviour, incomplete knowledge, multi-scale representations, and context. Suitable formalisms should complement mathematical modelling and be parallel, algorithmic, quantitative, causal, interaction-driven, composable, scalable, and modular.[^3]
- *Behavioural equivalences*, a primary tool for verifying computing systems, check that an implementation agrees with a specification by comparing semantics (dynamics) rather than syntax.[^4]
- An application of [[Data-Intensive Science]].

[^1]: [Hey et al., 2009, p. 99](zotero://open-pdf/library/items/XHD2CC9T?page=133&annotation=R56367FL); [Hey et al., 2009, p. 100](zotero://open-pdf/library/items/XHD2CC9T?page=134&annotation=L5T9SAPE)
[^2]: [Hey et al., 2009, p. 100](zotero://open-pdf/library/items/XHD2CC9T?page=134&annotation=BEXLMP2Y)
[^3]: [Hey et al., 2009, p. 100](zotero://open-pdf/library/items/XHD2CC9T?page=134&annotation=FZT859RL)
[^4]: [Hey et al., 2009, p. 102](zotero://open-pdf/library/items/XHD2CC9T?page=136&annotation=KUNNV47R)
