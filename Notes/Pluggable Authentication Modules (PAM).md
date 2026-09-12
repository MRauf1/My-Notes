---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Pluggable Authentication Modules (PAM)[^1]
> PAM is a system of dynamically loadable shared libraries, proposed by Sun Microsystems in 1995, to which an application hands off the task of determining whether a user can successfully [[Authentication (Computer Security)|authenticate]] itself.

# Properties
- Built to accommodate flexibility in authentication, making it comparatively easy to add support for additional authentication techniques such as two-factor authentication and physical keys.[^1]
- Works on top of the existing Unix authentication API and uses `/etc/shadow` directly, so integrating PAM support into a client typically requires little extra work; it does not, however, use every corresponding configuration file from the earlier [[Shadow File|shadow password]] package, such as `/etc/login.defs`.[^2]
- Also provides a limited amount of [[Authorization (Computer Security)|authorization]] control for services, such as denying a service like [[Cron|cron]] to certain users.[^1]
- Employs a number of dynamically loadable modules, each performing a specific task — for example, the `pam_unix.so` module checks a user's password.[^3]
- Its configuration lines stack: many rules can apply when performing one function, so a [[PAM Control Argument|control argument]] determines how the success or failure of one line affects the lines that follow.[^4]
- Nearly every program on a Linux system that requires authentication supports PAM, and most distributions use it, even though its programming interface is not easy and it does not obviously solve every problem left by traditional Unix authentication.[^5]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=190&annotation=SVT3XGHI)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=ZDYI97KN)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=190&annotation=ABQ6AHL7)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=192&annotation=NZAJKVT3)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=191&annotation=PV5SAH5K)
