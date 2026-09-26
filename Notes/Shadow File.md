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
- Despite the traditional description of its passwords as "encrypted," a password entry is not stored reversibly: it normally holds a one-way password hash encoded with an algorithm identifier, salt, and parameters.[^4]
- An attacker who obtains the hashes can guess candidate passwords offline, so the database must remain restricted — commonly to root and a narrow set of authorized system components — and its contents should never be printed, copied, logged, or shared merely to inspect account status.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=PQSJXN67)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=179&annotation=K4E5EGUI)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=ZDYI97KN)
[^4]: [Linux Journey: User Management](https://labex.io/linuxjourney/courses/user-management)
