---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Udev[^1]
> Udev is the Linux subsystem, run by the udevd daemon, that enables user-space programs to automatically configure and use newly attached devices.

# Properties
- udevd operates in a loop: the [[Kernel (Operating System)|kernel]] sends it a [[Uevent|uevent]] over an internal netlink; udevd loads the event's attributes; udevd then parses its rules and takes actions or sets further attributes based on them.[^2]
- Historically posed a chicken-and-egg startup problem, since device files are needed early in boot, yet udevd could not depend on the very devices it was meant to create, and had to start quickly enough not to hold up the rest of the system.[^3]
- [[Devtmpfs]] resolved this problem: the kernel creates device files itself and merely notifies udevd, which performs device initialization, process notification, and creates identifying symlinks (such as those under `/dev/disk/by-id`) instead.
- Administered through [[Udevadm]], which reloads rules, triggers events, and searches, explores, or monitors devices and uevents.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=70&annotation=Y7E295W9)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=80&annotation=H373V3SN)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=79&annotation=PCCI5NUF)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=82&annotation=ZIX37GPU)
