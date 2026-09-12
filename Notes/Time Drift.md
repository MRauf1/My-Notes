---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Time Drift[^1]
> Time drift is the current difference between the [[System Clock|kernel's system clock]] and the true time, as defined by an [[Atomic Clock|atomic clock]] or another very accurate reference clock.

# Properties
- Tends to develop because Unix machines often stay up for months or years on a single boot, and the kernel keeps time even worse than the [[Real-Time Clock (RTC)|RTC]].[^1]
- Should not be corrected with `hwclock`, since abruptly resetting the clock can cause time-based system events to be lost or mangled.[^2]
- Can be corrected smoothly with a utility like `adjtimex`, but is usually best kept in check with a [[Network Time Protocol (NTP)|network time daemon]].[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=182&annotation=S25KJM3H)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=183&annotation=VZS6222V)
