---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Systemd Unit[^1]
> A systemd unit is a specific instance of some capability that [[Systemd|systemd]] can operate — a service, a mount, a network socket, a timer, and so on — each belonging to a unit type describing that kind of capability; turning a unit on is called activating it.

# Properties
- Declares dependencies (e.g. `Requires`, `Wants`) on other units; by default, activating a unit activates all such dependencies at the same time as the unit itself, maximizing parallelism and minimizing boot time.[^2]
- Can instead require strict ordering (e.g. via `After`) when one unit must start only once another has already started.[^2]
- A dependency can also be a conditional dependency, evaluated against overall operating system state rather than another unit; if false, only that dependent unit fails to activate, while its other, non-conditional dependencies are still attempted regardless.[^3]
- The default boot goal is typically a target unit that groups a number of service and mount units together as dependencies; its full dependency tree can be visualized with `systemctl dot`.[^4]
- Strict dependencies can reduce fault tolerance — for example, chaining a login prompt's activation to a database server means a database failure also locks out login — so systemd offers a range of dependency types and styles to balance flexibility, speed, and fault tolerance.[^5]
- Distribution-maintained unit files live in the system unit directory; local customizations belong instead in the system configuration directory (`/etc`) rather than `/usr`, so they survive distribution updates.[^6]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=140&annotation=6JS96G8U)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=142&annotation=XDKL9FR9)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=142&annotation=DUQYJF6X)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=140&annotation=PT858S9T)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=141&annotation=I9TJ9EMW)
[^6]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=143&annotation=SAD66QRC)
