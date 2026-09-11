---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] User Space Scheduler[^1]
> A scheduler implemented as an ordinary program rather than inside the kernel; for a fixed list of commands to run, it can schedule them itself by sending `SIGSTOP` and `SIGCONT` to pause and resume the corresponding processes.

# Properties
- Relies on [[Signal (Computing)|signals]] rather than kernel-level [[CPU Scheduling]] mechanisms to control which of its managed processes may run.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=236&annotation=HZGBW68K)
