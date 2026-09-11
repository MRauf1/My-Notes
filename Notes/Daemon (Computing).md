---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Daemon (Computing)[^1]
> A daemon is a background service process, conventionally started from a script that runs the daemon program and then lets it detach itself so it continues running autonomously after the script exits.

# Properties
- Under traditional [[Init Process|init]] systems, a daemon's PID must be discovered afterward with `ps` or some service-specific mechanism, since the daemon detaches itself from the script that launched it.[^1]
- Modern init systems such as [[Systemd|systemd]] and [[Upstart]] instead manage individual daemons directly from the start, tracking exactly what is running without needing this rediscovery step.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=138&annotation=BNESQ8I7)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=138&annotation=BNESQ8I7)
