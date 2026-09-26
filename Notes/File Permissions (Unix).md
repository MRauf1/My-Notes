---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] File Permissions (Unix)[^1]
> Every Unix file has a set of permissions that determine whether a [[User (Unix)|user]] can read, write, or run the file.

# Properties
- The [[Root User]] is exempt from these ordinary restrictions and may read any file on the system.
- A file with its setuid permission bit set runs as its owner rather than as the invoking user when executed; see [[Setuid]]. The analogous [[Set-Group-ID (Setgid)|setgid]] bit does the same for group ID, and a directory's [[Sticky Bit|sticky bit]] further restricts who may remove or rename its entries.
- Expressed as a mode of three fixed-order triplets — owner, group, and other — each written as three characters (`r`, `w`, `x`, or `-` for absent); owner permissions apply when a process's effective user ID matches the file's [[File Ownership (Unix)|owner]], group permissions apply when an applicable process group ID matches the file's group, and other applies when neither class matches.[^2]
- The kernel selects exactly one applicable class per access and does not combine the three triplets to find the most permissive result.[^2]
- On a regular file: read permits access to its contents, write permits modifying them, and execute permits the kernel to attempt to run it as a program — though execution can still fail for reasons such as the file format, interpreter line, mount options, or another security control.[^2]
- On a directory, the same letters instead govern directory entries: read permits listing the names inside, write permits creating or removing entries (normally together with execute), and execute — also called search permission — permits traversing the directory and accessing entries by name.[^2]
- Deleting a file is governed primarily by the write and execute permissions on its parent directory, not by the file's own write bit.[^2]
- A separate [[File Ownership (Unix)|owner and group owner]] recorded on the object determines which triplet applies, but ownership alone grants no permission; both are inspected together with `ls -l`.[^2]
- Additional mechanisms — an [[Access Control List (Unix)|access control list]], mount options, capabilities, or mandatory access controls — can further affect the final decision beyond the matched triplet.[^2]
- A newly created object's requested mode has selected bits removed by the creating process's [[umask]].[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=58&annotation=A4TEJCNV)
[^2]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
