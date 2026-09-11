---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Warehouse-Scale Computer (WSC)[^1]
> A new class of computer: a very large [[Cluster (Computing)|cluster]] of commodity servers, built and operated at the scale of an entire warehouse, that underlies large-scale internet services and cloud computing.

# Properties
- Distinguished from an ordinary server room by three characteristics: an abundance of easy, coarse-grained parallelism across independent requests or jobs; a design where operational costs (power, cooling) are a first-class concern alongside purchase cost; and challenges and opportunities that only appear at very large scale (such as very rare hardware failures becoming routine events).
- MapReduce (and its open-source counterpart, Hadoop) is the most popular WSC batch-processing framework: a programmer-supplied Map function is applied, in parallel across thousands of servers, to each logical input record to produce intermediate key-value pairs, and a programmer-supplied Reduce function then collects and collapses those distributed results — a model simple enough for a novice to run a job across thousands of servers within minutes.
- Enables Software as a Service (SaaS): rather than selling software to install and run locally, a provider runs it remotely (typically behind a web interface) and charges customers by use rather than by ownership; the resulting economies of scale are also what makes cloud computing profitable for providers while remaining cheaper than self-hosting for customers.
- Related large-scale computing models include grid computing, where geographically dispersed computers communicate over long-haul networks, and volunteer computing, which harvests idle cycles from millions of otherwise-idle personal computers by giving each an independent piece of a larger problem.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=556&annotation=MWETHA9B)
