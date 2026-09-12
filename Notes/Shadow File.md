---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Shadow File[^1]
> `/etc/shadow` is the file that stores a Unix system's user authentication information — including encrypted passwords and password expiration data — corresponding to the users listed in [[Passwd File|/etc/passwd]].

# Properties
- Unlike `/etc/passwd`, normal users do not have read permission for `/etc/shadow`.[^2]
- Introduced to provide a more flexible and secure way of storing passwords than keeping the encrypted password directly in `/etc/passwd`.[^3]
- Its original suite of libraries and utilities was largely superseded by [[Pluggable Authentication Modules (PAM)|PAM]], though PAM still reads `/etc/shadow` directly rather than certain of its companion configuration files, such as `/etc/login.defs`.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=PQSJXN67)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=179&annotation=K4E5EGUI)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=ZDYI97KN)
