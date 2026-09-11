---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] System V Init[^1]
> System V init (Sys V) is the traditional sequenced [[Init Process|init]] implementation, used by Red Hat Enterprise Linux and others, that performs one startup task at a time according to a fixed boot sequence.

# Properties
- Its strictly sequential model makes dependency resolution easy, but limits performance, since no two parts of the boot sequence can run at once.[^2]
- Only supports a fixed set of services defined by the boot sequence: there is no standardized way to coordinate a newly plugged-in device or an on-demand service with init.[^2]
- Relies on shell scripts that tend to duplicate similar start/stop/restart logic across services.[^3]
- Introduced the concept of [[Runlevel|runlevels]], still supported for backward compatibility by [[Systemd|systemd]] and [[Upstart]].[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=137&annotation=CGQGRP2G)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=137&annotation=FP94IIE5)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=138&annotation=KTV8H9Z2)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=138&annotation=959WAF8B)
