---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Authorization (Computer Security)[^1]
> Authorization is the part of user security that defines and limits what an [[Identification (Computer Security)|identified]] and [[Authentication (Computer Security)|authenticated]] user is allowed to do.

# Properties
- On a Linux system, the kernel's own authorization rules govern how [[Setuid|setuid]] executables run and how user IDs may invoke the `setuid()` family of system calls to switch from one user to another.[^2]
- [[Pluggable Authentication Modules (PAM)|PAM]] additionally provides a limited amount of authorization control for services, such as denying a service like [[Cron|cron]] to certain users.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=189&annotation=SDG29UHL)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=189&annotation=64BC6D7P)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=190&annotation=SVT3XGHI)
