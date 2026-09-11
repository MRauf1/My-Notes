---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Deadlock[^1]
> A state in which a system of processes — each either working or waiting for a resource — cannot make any forward progress: no process is working, and no waiting process can be given the resource it is waiting for.

# Properties
- Deliberately ignored in many systems (see [[Ostrich Algorithm]]); for low-stakes products such as consumer operating systems or phones, allowing deadlock and restarting can be more efficient than preventing it, whereas failure-intolerant systems need to track, break, or prevent deadlock instead.
- Modeled and detected using a [[Resource Allocation Graph]]: if it contains a cycle in which every resource has only a single instance, the processes in that cycle are deadlocked.
- Possible only when the [[Coffman Conditions]] all hold simultaneously.
- Distinct from [[Livelock]], in which processes remain busy yet the system still fails to make forward progress.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=195&annotation=DB7TZ4UD)
