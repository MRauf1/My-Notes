---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Process User ID[^1]
> Every Unix [[Process (Computing)|process]] actually carries more than one user ID — the real, effective, saved, and filesystem user IDs — which together determine what the process may do and who may control it.

# Types
- [[Effective User ID]]
- [[Real User ID]]
- [[Saved User ID]]
- [[Filesystem User ID]]

# Properties
- On most Linux systems, a process's effective and real user IDs are the same.[^2]
- The difference between the effective and real user IDs is confusing enough that much documentation on process ownership gets it wrong.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=FZNDBBCD)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=UGI4B2YP)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=9CFXV6IN)
