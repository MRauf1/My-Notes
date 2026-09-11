---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Control Group (Cgroups)[^1]
> Control groups (cgroups) are an optional Linux kernel feature that lets a process hierarchy be tracked with finer granularity than ordinary process trees.

# Properties
- Used by [[Systemd|systemd]] to identify a service's full set of descendant processes without needing to special-case how many times it forks or daemonizes — only whether it forks at all matters.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=148&annotation=YCLZ8LBM)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=149&annotation=ML8NCGH6)
