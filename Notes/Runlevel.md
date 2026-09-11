---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Runlevel[^1]
> A runlevel is [[System V Init|System V init's]] representation of a system operating mode, such as shutdown (0), single-user mode (1), or reboot (6).

# Properties
- Supported for backward compatibility by both [[Systemd|systemd]] (as activating shutdown units) and [[Upstart]] (as emitting shutdown events), even though neither uses runlevels as its native mechanism.[^1]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=138&annotation=959WAF8B)
