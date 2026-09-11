---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Ostrich Algorithm[^1]
> The strategy of simply ignoring [[Deadlock]]: the operating system takes no special action when deadlock occurs, relying on it to typically resolve on its own.

# Properties
- Named for the (unsourced) image of an ostrich sticking its head in the sand.
- Works in practice because the OS routinely preempts processes for context switches and can interrupt system calls, either of which may incidentally break a deadlock; making some resources (such as files) read-only can also remove the need for exclusive access altogether.
- Can still fail against an adversarially crafted, or simply poorly written, program designed to deadlock the OS, but this is an acceptable risk for most everyday systems.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=199&annotation=3M9BE63R)
