---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Module Decomposition[^1]
> The design decision of how to divide a system's functionality among its constituent components, whether by splitting a larger component into smaller ones or by combining smaller components into a larger one.

# Properties
- Splitting a component into smaller pieces is not automatically good, since it adds components and the code needed to manage them, can separate genuinely related pieces, and can introduce duplication.
- Splitting is best justified when the resulting subtask becomes an independent, [[General-Purpose Code|general-purpose]] helper method that the parent method simply calls; dividing a method into several sibling methods that the parent then invokes in sequence is less ideal and can add rather than remove complexity.
- Combining modules is favored when they are related: when they are used together and depend on each other bidirectionally, when they conceptually overlap, or when one is hard to understand without the other.
- Combining is also favored when it lets modules share information, simplifies the resulting interface, eliminates duplication, or separates general-purpose from special-purpose code.
- Layers that all expose the same or a similar abstraction are a red flag of poor decomposition, often surfacing as [[Pass-Through Method|pass-through methods]].
- Repetition of the same code in multiple places is a red flag that the right abstraction has not yet been found.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
