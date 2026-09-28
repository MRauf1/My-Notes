---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Gray's Laws[^1]
> Jim Gray's informal rules for data engineering of large-scale scientific datasets:
> 1. Scientific computing is becoming increasingly data intensive.
> 2. The solution is a scale-out architecture.
> 3. Bring computations to the data, rather than data to the computations.
> 4. Start the design with the "20 queries".
> 5. Go from "working to working".

# Properties
- **I/O bottleneck**: analysis of observational data and large simulations is limited by I/O; once data exceeds RAM, cache locality no longer helps. Numerical packages must be redesigned in multi-phase, divide-and-conquer (out-of-core) form, like database sorts and joins on larger-than-RAM data.[^2]
- **Scale-out**: larger network storage attached to compute clusters fails because interconnect speeds lag the yearly doubling of storage; instead partition data among simple nodes with local storage, the smaller the better for balancing CPU, disk, and network ([[Scaling (Parallel Computing)]]).[^3]
- **Computation to data**: most analyses are expressible in a set-oriented, declarative language benefiting from cost-based query optimisation, automatic parallelism, and indexes; [[Relational Database|relational databases]] (extended with procedural class libraries) and MapReduce both serve this role.[^4]
- **20 queries**: to bridge database builders and domain scientists, ask for the 20 most important questions the system must answer.[^5]
- **Working to working**: a system that works only when every component works will never finish; build modular systems whose components can be replaced as technology evolves.[^6]
- Rather than monolithic result sets, queries over partitioned data can return results bucket by bucket (easing checkpointing) or stop once an aggregate is within a target accuracy.[^7]
- Scientists need templates and best practices for balanced hardware and software, including cloud and specialised data clouds, to avoid reinventing the wheel.[^8]
- Principles of [[Data-Intensive Science]].

[^1]: [Hey et al., 2009, p. 5](zotero://open-pdf/library/items/XHD2CC9T?page=39&annotation=EGJ3KHPD); [Hey et al., 2009, p. 5](zotero://open-pdf/library/items/XHD2CC9T?page=39&annotation=LLJ7G3HX)
[^2]: [Hey et al., 2009, p. 6](zotero://open-pdf/library/items/XHD2CC9T?page=40&annotation=Z7KM8L4K); [Hey et al., 2009, p. 6](zotero://open-pdf/library/items/XHD2CC9T?page=40&annotation=I4N4CYPG)
[^3]: [Hey et al., 2009, p. 6](zotero://open-pdf/library/items/XHD2CC9T?page=40&annotation=46AA8QNL)
[^4]: [Hey et al., 2009, p. 7](zotero://open-pdf/library/items/XHD2CC9T?page=41&annotation=NT2RMRX7); [Hey et al., 2009, p. 7](zotero://open-pdf/library/items/XHD2CC9T?page=41&annotation=XTC24WUC); [Hey et al., 2009, p. 7](zotero://open-pdf/library/items/XHD2CC9T?page=41&annotation=457LW737)
[^5]: [Hey et al., 2009, p. 7](zotero://open-pdf/library/items/XHD2CC9T?page=41&annotation=VRZEKHMD); [Hey et al., 2009, p. 7](zotero://open-pdf/library/items/XHD2CC9T?page=41&annotation=ER8AGHVU)
[^6]: [Hey et al., 2009, p. 8](zotero://open-pdf/library/items/XHD2CC9T?page=42&annotation=3MD98V5W); [Hey et al., 2009, p. 8](zotero://open-pdf/library/items/XHD2CC9T?page=42&annotation=AJ5AZ88A); [Hey et al., 2009, p. 8](zotero://open-pdf/library/items/XHD2CC9T?page=42&annotation=QAD4A7G9)
[^7]: [Hey et al., 2009, p. 9](zotero://open-pdf/library/items/XHD2CC9T?page=43&annotation=C6T3KJSM)
[^8]: [Hey et al., 2009, p. 9](zotero://open-pdf/library/items/XHD2CC9T?page=43&annotation=FSBPP7NB); [Hey et al., 2009, p. 9](zotero://open-pdf/library/items/XHD2CC9T?page=43&annotation=4SXSMCUL); [Hey et al., 2009, p. 9](zotero://open-pdf/library/items/XHD2CC9T?page=43&annotation=6DD5UGFI)
