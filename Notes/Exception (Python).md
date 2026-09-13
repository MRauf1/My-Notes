---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Exception (Python)[^1]
> An event that signals a condition and modifies a program's flow of control: a sort of structured "go-to" that unwinds execution directly back to a handler in a single step, abandoning any activity begun since that handler was entered, rather than being checked for after every operation via return codes.

# Properties
- Triggered automatically by Python whenever it detects an error at runtime, but can equally be triggered manually by a script's own code, via [[Raise Statement (Python)|raise]] or [[Assert Statement (Python)|assert]][^2].
- Beyond error handling, exceptions commonly serve several other roles: event notification (signaling a valid condition instead of returning and testing a result code), special-case handling (concentrating rare-condition logic in one handler instead of scattering checks throughout a program), termination actions, and even unusual control flows a `break` cannot achieve, such as jumping out of several nested loops at once[^3].
- If left uncaught, Python's default behavior is to stop the program and print an error message; wrapping the risky code in a [[Try Statement (Python)|try statement]] catches the exception and lets the program continue instead[^2].
- A concrete, language-level instance of the broader [[Exception Handling (Software Design)|software-design notion of exception handling]].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1323&annotation=B7JDT352)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1324&annotation=UAT4E5I6)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1324&annotation=X99QFLPP)
