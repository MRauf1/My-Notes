---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Boot Process (Linux)[^1]
> The Linux boot process is the sequence that carries a machine from power-on to a running user space, coordinated across firmware, the [[Boot Loader|boot loader]], and the [[Kernel (Operating System)|kernel]].

# Properties
- Simplified view: (1) the machine's firmware loads and runs a boot loader; (2) the boot loader finds the kernel image on disk, loads it into memory, and starts it; (3) the kernel initializes its devices and drivers; (4) the kernel mounts the root filesystem; (5) the kernel starts [[Init Process|init]] (PID 1) — the user space start; (6) init sets the rest of the system's processes in motion; (7) near the end of booting, init starts a process that allows login.[^1][^2]
- The kernel's own internal initialization proceeds through: CPU inspection, memory inspection, device bus discovery, device discovery, auxiliary kernel subsystem setup (e.g. networking), root filesystem mount, and finally the user space start.[^3]
- Some components needed this early may be [[Loadable Kernel Module|loadable kernel modules]] that must be loaded — typically from an [[Initial RAM Filesystem (Initrd)|initial RAM filesystem]] — before the true root filesystem can be mounted.[^4]
- User space itself starts in roughly this order: [[Init Process|init]]; essential low-level services (e.g. udevd, syslogd); network configuration; mid- and high-level services (e.g. cron, printing); login prompts, GUIs, and other high-level applications.[^5][^6]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=118&annotation=TG8CZ8EE)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=119&annotation=P7KDIEIF)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=120&annotation=EK5UG7SU)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=120&annotation=GVJWMVKQ)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=136&annotation=ZKN3UQ5I)
[^6]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=137&annotation=E2IIEATK)
