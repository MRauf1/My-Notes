---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Load Average[^1]
> The load average is the average number of processes currently ready to run — an estimate of how many processes are capable of using the CPU at any given time.

# Properties
- Most processes are usually waiting for input (keyboard, mouse, network) rather than ready to run, so they contribute nothing to the load average; only processes actually doing something affect it.[^1]
- A load average near 0 is normal for a desktop system doing nothing CPU-intensive, and is a good sign, since it means the processor isn't challenged and power is being saved.[^2]
- A load average around 1 usually means a single process is using the CPU nearly all the time; the `top` command usually identifies it, since it rises to the top of the display.[^3]
- On a multi-core system, a load average of $n$ means $n$ cores have just enough to do all the time — a load average of 1 on a two-core machine means only one core is likely active at any given time.[^4]
- A high load average does not necessarily indicate trouble: a system with enough memory and I/O resources can handle many ready processes, which simply take longer to finish since they compete for CPU time; a web server can also show an artificially high load average because processes start and terminate too quickly for the measurement mechanism to work effectively.[^5]
- A high load average combined with a genuinely slow system instead suggests memory problems, such as [[Thrashing]], where processes remain ready-to-run without available memory for much longer than usual.[^6]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=205&annotation=RQ6JEINX)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=205&annotation=SU8I6G4N)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=206&annotation=B63W7KCF)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=206&annotation=HKGZGGZF)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=206&annotation=FPATLKXM)
[^6]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=206&annotation=XSM7ZS86)
