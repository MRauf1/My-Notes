---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Data Parallelism[^1]
> The oldest and best-established parallel programming paradigm, in which an operation or sequence of operations is applied simultaneously to all items in a collection of data.

# Properties
- Motivation: sequential software does not run faster on multicore processors; exploiting them requires decomposing a task into pieces solved largely independently and assembling the results. Producing parallel software is among the most pressing problems in software development, since parallel programs are far harder to design, write, debug, and tune than sequential ones.[^2]
- *Functional programming* complements it: languages that largely prohibit updates to program state (variables are bound once, and new values create new variables) eliminate the updates that require synchronisation, so mutable state and locks or transactional memory are needed only for inter-processor communication.[^3]
- Underlies scale-out data analysis such as MapReduce ([[Gray's Laws]]); cf. [[Scaling (Parallel Computing)]].

[^1]: [Hey et al., 2009, p. 127](zotero://open-pdf/library/items/XHD2CC9T?page=161&annotation=YD9V75BG)
[^2]: [Hey et al., 2009, p. 125](zotero://open-pdf/library/items/XHD2CC9T?page=159&annotation=EMI23B8R); [Hey et al., 2009, p. 126](zotero://open-pdf/library/items/XHD2CC9T?page=160&annotation=GI4AZT9Q); [Hey et al., 2009, p. 127](zotero://open-pdf/library/items/XHD2CC9T?page=161&annotation=S2DDEPTJ)
[^3]: [Hey et al., 2009, p. 128](zotero://open-pdf/library/items/XHD2CC9T?page=162&annotation=X6GVTR4N)
