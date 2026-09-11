---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Shutdown Process (Linux)[^1]
> The Linux shutdown process is the sequence, initiated by the `shutdown` command and carried out by [[Init Process|init]], that cleanly stops a running system.

# Properties
- `shutdown` notifies logged-in users the machine is going down; if given a future time rather than "now," it also creates `/etc/nologin`, which prohibits any login except by the superuser while present.[^2]
- At the scheduled time, `shutdown` tells init to begin shutting down: activating shutdown units on [[Systemd|systemd]], emitting shutdown events on [[Upstart]], or changing the [[Runlevel|runlevel]] to 0 or 6 on [[System V Init|System V init]].[^3]
- Regardless of init implementation, the procedure generally: (1) asks every process to shut down cleanly; (2) sends unresponsive processes a `TERM` [[Signal (Computing)|signal]]; (3) sends any still-unresponsive stragglers a `KILL` signal; (4) locks system files and prepares for shutdown; (5) unmounts every filesystem but the root; (6) remounts the root filesystem read-only; (7) flushes all buffered writes to disk with `sync`; (8) invokes the `reboot(2)` system call — via init itself or an auxiliary program such as `reboot`, `halt`, or `poweroff` — to actually reboot or stop the kernel.[^3][^4]
- Takes several seconds to complete; the machine should never be reset or powered off while it is in progress.[^5]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=169&annotation=6ASLXW2I)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=169&annotation=NN3CWK7R)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=169&annotation=NIT96P5X)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=170&annotation=Y98UUC8P)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=169&annotation=M2ZEUQJH)
