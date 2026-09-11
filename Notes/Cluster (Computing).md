---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Cluster[^1]
> A set of computers connected over a network — typically a local area network, over standard network switches — that function together as a single large [[Message-Passing Multiprocessor|message-passing multiprocessor]].

# Properties
- Each node in a cluster runs its own separate copy of the [[Operating System]], unlike the cores of a single [[Multicore Microprocessor|multicore]] chip or a [[Shared Memory Multiprocessor|shared-memory]] system, which communicate over a far higher-bandwidth, lower-latency on-chip or memory interconnect.
- Its separate-memory design, a weakness for parallel programmers, becomes a strength for dependability: a failed node's computer can be replaced, or the cluster can scale down gracefully, without bringing down the whole system — unlike a shared-memory multiprocessor, whose components are typically far more tightly coupled.
- A large-scale collection of clusters or servers optimized for internet-scale services is called a [[Warehouse-Scale Computer]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=525&annotation=24XG6Y2K)
