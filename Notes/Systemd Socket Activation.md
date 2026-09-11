---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Systemd Socket Activation[^1]
> Socket activation is a [[Systemd|systemd]] pattern in which a lightweight auxiliary [[Systemd Unit|unit]] represents a resource — a socket, path, or device — that a heavier service unit actually provides, letting systemd offer the resource immediately while deferring or parallelizing the service's own startup.

# Types
- On-demand: once the resource unit is activated, systemd monitors the resource; when anything tries to access it, systemd blocks and buffers the access, activates the service unit, and lets the service take over the resource and its buffered input once ready — so the service need not start until the resource is actually used.[^2]
- Eager parallel start: systemd instead activates the service unit as soon as it activates the resource unit, offering the resource quickly while giving slower-starting essential services (e.g. syslog, D-Bus) — and everything depending on them — a head start.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=149&annotation=R8BHQXRC)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=150&annotation=QQI2BGPT)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=150&annotation=8REPAQER)
