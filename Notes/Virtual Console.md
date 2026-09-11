---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Virtual Console[^1]
> A virtual console is one of several [[Terminal (Unix)|terminals]] that Linux multiplexes onto a single physical display, each able to run independently in text or graphics mode.

# Properties
- Linux systems traditionally booted directly into a text-mode virtual console, but most distributions now hide text mode behind an interim graphical bootsplash and switch to full graphics mode near the end of booting.[^2]
- An X server running in graphics mode takes over a free virtual console itself, rather than receiving one from init configuration, unless directed to use a specific one.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=77&annotation=FIKTXTPQ)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=76&annotation=4APELS69)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=77&annotation=Z2H43U8I)
