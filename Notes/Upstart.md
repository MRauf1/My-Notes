---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Upstart[^1]
> Upstart is a reactionary [[Init Process|init]] implementation, historically used on Ubuntu, that receives events and runs jobs in response, which can themselves produce further events that trigger more jobs.

# Properties
- Starts services in parallel, like [[Systemd|systemd]], to speed up boot, unlike the strictly sequential [[System V Init]].[^2]
- Manages individual service [[Daemon (Computing)|daemons]] directly from the start, rather than relying on daemons to detach themselves from scripts.[^3]
- Offers some on-demand service startup and System V backward compatibility, including support for [[Runlevel|runlevels]].[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=137&annotation=JU5BDNF6)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=137&annotation=JU5BDNF6)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=138&annotation=BNESQ8I7)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=138&annotation=959WAF8B)
