---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Setuid[^1]
> Setuid is the mechanism, governed by the `setuid()` family of system calls, by which a process changes which user ID it runs as.

# Properties
- A process running as root (user ID 0) can use `setuid()` to become any other user.[^1]
- A process not running as root has severe restrictions on how it may use `setuid()`; in most cases it cannot use it at all.[^1]
- Any process can execute a setuid program — one whose setuid permission bit is set — as long as it has adequate [[File Permissions (Unix)|file permissions]] to run it; doing so runs the program as its owner rather than as the invoking user.[^1]
- Has nothing to do with usernames or passwords, which are strictly [[User Space|user-space]] concepts; the kernel only ever deals with numeric user IDs.[^2]
- Because all user switching, and the file-access permissions that result from it, flows through setuid programs and the system calls they make, both which programs are setuid and what those programs do must be handled with extreme care: a setuid-root copy of a shell, or a buggy setuid-root program, lets any local user gain complete control of the system, making setuid-root programs a primary target of systems intrusion.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=6ZLNLDY5)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=JSPB45RG)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=188&annotation=24H85DCU)
