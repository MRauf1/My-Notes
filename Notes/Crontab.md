---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Crontab[^1]
> A crontab is a per-user table of scheduled [[Cron|cron]] jobs; system-wide recurring tasks are instead scheduled through `/etc/crontab` or files under `/etc/cron.d`, rather than the superuser's own crontab.

# Properties
- `/etc/crontab` should not be edited with the `crontab` command, since it has an extra field inserted before the command to run: the user that should run the job.[^1]
- Files under `/etc/cron.d` may have any name but share the same format as `/etc/crontab`.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=186&annotation=R56XGRA5)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=186&annotation=QTQ2D86F)
