---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Linux Directory Hierarchy[^1]
> The Linux directory hierarchy is the standard set of subdirectories found under the [[Path (Unix)|root directory]] (/) of a Linux system, each serving a conventional purpose.

![[Linux Directory Hierarchy.png]]

# Properties
- /bin — ready-to-run programs (executables), including most basic Unix commands.
- /dev — device files.
- /etc — core system configuration, such as user password, boot, device, and networking setup files.
- /home — personal directories for regular users.
- /lib — library files containing code that executables can use; should contain only shared libraries, unlike other lib directories such as /usr/lib.
- /proc — system statistics and information about currently running processes and kernel parameters, exposed through a browsable directory-and-file interface.
- /sys — a device and system interface similar to /proc.
- /sbin — system executables related to system management; usually requires root to run.
- /tmp — storage for smaller, temporary files, cleared on boot by most distributions.
- /usr — the bulk of the Linux system's user-space programs and data, containing its own /bin, /sbin, /lib, /include (C compiler header files), /info (GNU info manuals), /local (administrator-installed software), /man (manual pages), and /share (files portable across Unix machines).
- /var — runtime information recorded by programs, such as system logging, user tracking, and caches; /var/tmp is not wiped on boot, unlike /tmp.
- /boot — kernel boot loader files, used only in the first stage of the Linux startup procedure.
- /media — a base attachment point for removable media such as flash drives.
- /opt — optional third-party software; not used by many systems.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=65&annotation=7D3L7PXQ)
