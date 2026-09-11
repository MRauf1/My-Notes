---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Coffman Conditions[^1]
> The four necessary and sufficient conditions for [[Deadlock]] to be possible: if all four hold at once, there is a non-zero probability that the system will deadlock at some point.

# Types
- Mutual exclusion — at least one resource is held in a non-shareable mode, so only one process can use it at a time; see [[Mutual Exclusion]].
- [[Hold and Wait|Hold and wait]] — a process already holding one resource is simultaneously waiting to acquire another.
- No preemption — a resource cannot be forcibly taken from the process holding it; it can only be released voluntarily. Contrast with [[Preemptive Scheduling]], which forcibly reclaims the CPU itself rather than a resource a process holds.
- Circular wait — there exists a cycle of processes, each waiting on a resource held by the next process in the cycle.

# Properties
- Correspond directly to a cycle appearing in a [[Resource Allocation Graph]]: circular wait is what produces the cycle, while the other three conditions are what make that cycle unbreakable on its own.
- Breaking any single condition, such as [[Hold and Wait|hold and wait]], removes the possibility of deadlock arising from it.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=197&annotation=TH42L3JY)
