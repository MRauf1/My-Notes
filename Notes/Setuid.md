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
- Not the only mechanism that can change a process's effective identity: saying a process runs only "as the user who started it" is an oversimplification, since service managers, containers, namespaces, and other privilege-changing system calls can likewise affect the identities visible or effective in a particular context.[^4]
- Setting the bit is not a general instruction to "run as root": its effect depends on the executable's owner, the operating system, the filesystem and mount options, and how the program itself manages its credentials.[^5]
- Even for a root-owned program, the resulting root-authorized access lasts only while the program runs, and only through the operations its own code actually performs; modern implementations also rely on PAM, file locking, policy, and other safeguards, so the bit alone does not explain the complete workflow.[^5]
- Linux normally does not honor the bit on interpreted scripts, since doing so safely raises race- and interpreter-related problems; a filesystem mounted with `nosuid` also suppresses both setuid and [[Set-Group-ID (Setgid)|setgid]] effects.[^5]
- A flaw in a privileged setuid program can become a privilege-escalation path, so such programs must validate input, control which environment and file paths they trust, avoid unsafe subprocess behavior, minimize privileged code, and drop elevated credentials as soon as possible.[^5]
- Narrower mechanisms — service-mediated operations, carefully scoped [[Sudo (Command)|sudo]] policy, or capabilities — are preferable when they fit the requirement; the bit should never be added to an arbitrary shell, interpreter, or copied program as an experiment on a shared system.[^5]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=6ZLNLDY5)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=JSPB45RG)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=188&annotation=24H85DCU)
[^4]: [Linux Journey: User Management](https://labex.io/linuxjourney/courses/user-management)
[^5]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
