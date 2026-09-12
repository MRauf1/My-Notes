---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Real-Time Clock (RTC)[^1]
> The real-time clock (RTC) is the battery-backed hardware clock built into PC hardware, consulted by the kernel to set the [[System Clock|system clock]] at boot time.

# Properties
- Not the most accurate clock, but better than nothing.[^1]
- Can be read into the system clock at any time with `hwclock`.[^1]
- Should be kept in Universal Coordinated Time (UTC) to avoid trouble with time zone or daylight saving time corrections.[^1]
- Should not be used to correct [[Time Drift]] in the system clock, since abrupt correction can cause time-based system events to be lost or mangled.[^2]
- Can instead be set from network time so that time coherency survives a reboot.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=182&annotation=G8FQDF87)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=183&annotation=VZS6222V)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=184&annotation=DDF59VKX)
