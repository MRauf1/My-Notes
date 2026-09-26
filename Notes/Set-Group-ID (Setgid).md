---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Set-Group-ID (Setgid)[^1]
> The set-group-ID bit (setgid, SGID) is a file-mode bit with two distinct uses: on an executable regular file it can change a new process's effective group ID, and on a directory it makes newly created entries inherit the directory's group instead of the creator's default group.

# Properties
- A directory's newly created subdirectories also inherit the setgid bit on Linux, helping a shared project tree keep a consistent group throughout.[^1]
- Does not itself grant group write access: the directory mode, process [[umask]], requested creation mode, default ACLs, and other controls still determine actual access.[^1]
- On an executable, the kernel initializes the new process's effective group ID from the executable's group owner only when it honors the bit; this can be suppressed by controls such as a `nosuid` mount, and is not a universal guarantee across every file type or environment.[^1]
- For a collaborative directory, combining an intended group owner, setgid, and narrowly chosen access bits usually gives clearer control than making a tree world-writable.[^1]

[^1]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
