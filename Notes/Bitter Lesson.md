---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Bitter Lesson[^1]
> The historical observation from roughly 70 years of [[Artificial Intelligence|AI]] research that general-purpose methods which leverage computation, and continue to scale as available computation grows, are ultimately the most effective by a large margin, outperforming methods that build human domain knowledge into agents. The two classes of methods that seem to scale arbitrarily in this way are search and learning.

# Properties
- Rests on four recurring historical observations:[^2]
	1. AI researchers have often tried to build knowledge into their agents.
	2. This always helps in the short term and is personally satisfying to the researcher.
	3. In the long run it plateaus and even inhibits further progress.
	4. Breakthrough progress eventually arrives through the opposing approach: scaling computation via search and learning.
- Leveraging human knowledge gives short-term improvements, but only leveraging computation matters in the long run.[^3]
- The two approaches need not conflict in principle, but in practice they do: time spent on one is time not spent on the other.[^4]
- The human-knowledge approach tends to complicate methods in ways that make them less suited to exploiting general methods that leverage computation.[^5]
- Search and [[Machine Learning|learning]] (including learning by self-play, as in [[Reinforcement Learning]]) are the two most important classes of techniques for bringing massive computation to bear.[^6]
- The actual contents of minds (e.g. notions of space, objects, multiple agents, or symmetries) are tremendously, irredeemably complex, being part of the arbitrary, intrinsically complex outside world. They should not be hand-built into agents, e.g. via hand-crafted [[Knowledge Representation (Artificial Intelligence)|knowledge representations]] or [[Inductive Bias|inductive biases]].[^7]
- Instead, only the meta-methods that can find and capture this arbitrary complexity should be built in. These methods must be able to find good approximations, but the search for those approximations should be done by the methods, not by the researcher: agents should discover like we can, rather than contain what we have discovered. Building in our discoveries only obscures how the discovering process itself can be done.[^7]
- See [[The Bitter Lesson (Sutton)]] for a review and critique of the source essay.

[^1]: [Sutton, The Bitter Lesson, p. 1](zotero://open-pdf/library/items/7HZ94VF3?page=1&annotation=W2CINBZ3); [p. 2](zotero://open-pdf/library/items/7HZ94VF3?page=2&annotation=EQ8LZIBE)
[^2]: [Sutton, The Bitter Lesson, p. 2](zotero://open-pdf/library/items/7HZ94VF3?page=2&annotation=2TZE9AKV)
[^3]: [Sutton, The Bitter Lesson, p. 1](zotero://open-pdf/library/items/7HZ94VF3?page=1&annotation=93LK98VF)
[^4]: [Sutton, The Bitter Lesson, p. 1](zotero://open-pdf/library/items/7HZ94VF3?page=1&annotation=ANGR9IES)
[^5]: [Sutton, The Bitter Lesson, p. 1](zotero://open-pdf/library/items/7HZ94VF3?page=1&annotation=28W4GQI9)
[^6]: [Sutton, The Bitter Lesson, p. 1](zotero://open-pdf/library/items/7HZ94VF3?page=1&annotation=W8PBQAWW)
[^7]: [Sutton, The Bitter Lesson, p. 2](zotero://open-pdf/library/items/7HZ94VF3?page=2&annotation=26R6U3KN)
