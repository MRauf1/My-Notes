---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Interconnection Network[^1]
> The network topology connecting the nodes of a [[Multiprocessor]], whether a [[Shared Memory Multiprocessor|shared-memory]] system's processor-memory nodes or a [[Cluster (Computing)|cluster's]] separate computers.

# Types
- Fully connected network — supplies a dedicated communication link between every pair of nodes; offers the best performance but scales poorly, since the number of links grows quadratically with the node count.
- Crossbar network — lets any node communicate with any other node in a single pass through the network, without requiring a dedicated link per pair.
- Multistage network — supplies a small switch at each node, trading some latency and contention for a much cheaper, more scalable design than a fully connected or crossbar network.

# Properties
- Network bandwidth is the peak transfer rate of the network, whether of a single link or the collective rate of all links; bisection bandwidth is the worst-case bandwidth across a cut that splits the multiprocessor into two equal halves, a stricter measure of how well the network supports genuinely global communication patterns.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=560&annotation=C6C4BN8H)
