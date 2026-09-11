---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Environment Variable[^1]
> An environment variable is like a [[Shell Variable|shell variable]] storing a text string, except that it is not specific to the shell: every [[Process (Computing)|process]] on a Unix system has environment variable storage.

# Properties
- The operating system passes all of a shell's environment variables to the programs that the shell runs, unlike shell variables.
- Many programs read environment variables for configuration and options.
- [[PATH (Environment Variable)|PATH]] is a special environment variable containing the command path.
- Inherited across [[Fork and Exec|fork() and exec()]], letting a process pass a standard set of behaviors down to its children.[^2]
- Cannot be read by an outside process, unlike a process's `argv`, which can be — a security-relevant distinction.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=47&annotation=5Y4Q7I93)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=110&annotation=RH95AWJR)
