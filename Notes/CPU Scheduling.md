---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] CPU Scheduling[^1]
> The problem of efficiently selecting which process among the [[Ready Queue|ready-to-run processes]] to run on a system's CPU cores, since a busy system typically has more ready processes than cores.

# Properties
- Realizes [[Process Management]]'s task of deciding which process is allowed to use the CPU at any given time.
- Also decides when to pause a running process, along with its threads, so another process can run; must balance pausing processes often enough to stay responsive against pausing so often that time is wasted on [[Context Switch|context switching]].
- Affects a system's latency and throughput.[^2]
- No single scheduler is optimal for every environment and set of goals.[^3]
- Implemented either inside the kernel, or, for a fixed list of commands, by a [[User Space Scheduler]].[^4]
- On Linux, expressed per-process as a [[Scheduling Priority (Linux)|scheduling priority]], influenced indirectly through the process's [[Nice Value|nice value]]; a similar priority scheme governs [[IO Scheduling Priority|I/O scheduling]].
- The [[Ready Queue]]'s size at any moment is estimated by the [[Load Average]].

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=235&annotation=PV5ZZXRC)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=236&annotation=2NFW9N2V)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=236&annotation=N5KHSD8Y)
[^4]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=236&annotation=HZGBW68K)
