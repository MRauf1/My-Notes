---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] System Configuration Directory[^1]
> `/etc` is the [[Linux Directory Hierarchy|directory]] holding a Linux system's customizable, single-machine configuration files, such as user information and network details.

# Properties
- General application details, such as a distribution's user-interface defaults, do not belong in `/etc`; noncustomizable system configuration files, such as systemd's prepackaged unit files, may instead live elsewhere, such as under `/usr/lib`.[^2]
- The long-standing trend has been to move individual configuration files into subdirectories under `/etc`, such as `/etc/init` for [[Upstart]] and `/etc/systemd` for [[Systemd|systemd]]; most entries under `/etc` are now themselves subdirectories.[^3]
- Placing customizations in separate files within these configuration subdirectories, as with `/etc/grub.d`, avoids a package update simply overwriting a single, hand-edited configuration file.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=175&annotation=7FNX2NC4)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=175&annotation=EQ3S4FHC)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=175&annotation=A38AIIL2)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=175&annotation=42R4J6AV)
