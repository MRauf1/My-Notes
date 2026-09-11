---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] systemd[^1]
> systemd is the modern, goal-oriented [[Init Process|init]] implementation that has become the emerging standard on Linux distributions: it resolves a target's dependencies and satisfies them, rather than following a fixed startup sequence.

# Properties
- Starts many services in parallel to speed up boot, and can defer a service's start until it is actually needed — one of its most significant features.[^2]
- Boots by loading its configuration, determining its boot goal (usually the `default.target` unit), resolving that goal's full dependency tree, and activating the goal along with its dependencies; after boot it can react to system events (such as [[Uevent|uevents]]) to activate further components.[^3]
- Deliberately avoids any rigid startup sequence, preferring other mechanisms to resolve dependencies while maximizing parallelism.[^4]
- Operates on more than processes: it can mount filesystems, monitor network sockets, run timers, and more; each kind of capability is a unit type, and each specific instance is a [[Systemd Unit|unit]], which is activated to turn it on.[^5]
- Manages individual service [[Daemon (Computing)|daemons]] directly from the start, using [[Control Group (Cgroups)|control groups]] to track a service's full process hierarchy regardless of how many times it forks.[^6]
- Distinguishes enabling a unit (installing it into systemd's configuration so it persists across reboots) from activating a unit (turning it on for the current runtime with `systemctl start`); enabling does not itself activate.[^7]
- Aims to incorporate standard Unix services such as cron and inetd, taking inspiration from Apple's launchd, and is written in C rather than shell scripts to reduce the number of scripts on a system.[^8]
- Offers System V backward compatibility, including support for [[Runlevel|runlevels]].[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=137&annotation=JU5BDNF6)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=139&annotation=RSGTZSM3)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=139&annotation=UMMIKV85)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=139&annotation=V4EU82RK)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=140&annotation=6JS96G8U)
[^6]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=149&annotation=ML8NCGH6)
[^7]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=145&annotation=ANUT2JLY)
[^8]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=154&annotation=KIWVBM6H)
