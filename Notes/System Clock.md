---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] System Clock[^1]
> The system clock is the clock that the Linux kernel maintains and consults for the current time, as when running commands like `date`.

# Properties
- Represents the current time as the number of seconds since 12:00 midnight on January 1, 1970, UTC (the Unix epoch).[^2]
- Can be set directly with the `date` command, but doing so is usually a bad idea, since the time will rarely be exactly right; the system clock should stay as close to the correct time as possible.[^1]
- Initialized from the [[Real-Time Clock (RTC)|real-time clock]] at boot time.[^3]
- Drifts from the true time the longer a machine stays up on a single boot, since the kernel keeps time even worse than the RTC; see [[Time Drift]].[^4]
- Best kept correct with a [[Network Time Protocol (NTP)|network time daemon]] rather than by direct correction.[^5]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=182&annotation=F65B8M9F)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=183&annotation=3U77HJXY)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=182&annotation=G8FQDF87)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=182&annotation=S25KJM3H)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=183&annotation=VZS6222V)
