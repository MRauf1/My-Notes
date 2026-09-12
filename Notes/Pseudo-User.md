---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Pseudo-User[^1]
> A pseudo-user is a [[User (Unix)|Unix user]] that cannot log in, but under which the system can still start processes.

# Properties
- Usually created for security reasons, so a process can run with restricted privileges rather than as a real, login-capable user.[^1]
- The `nobody` user is an underprivileged pseudo-user that cannot write to anything on the system, so processes that should not need write access are run as it.[^2]
- The `daemon` pseudo-user similarly lacks login privileges but can still own processes.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=24WH2ZGH)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=DVAG39F5)
