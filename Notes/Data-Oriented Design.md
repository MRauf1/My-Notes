---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Data-Oriented Design[^1]
> The practice of designing software by developing transformations for well-formed data, where the criteria for "well-formed" are guided by the target hardware and by the patterns and types of transforms that need to operate on the data.

# Properties
- Founded on two principles: [[Data Is Not the Problem Domain]] and [[Data Is Type, Frequency, Quantity, Shape, and Probability]].
- Centered on live, real data that is also information, in contrast to [[Object-Oriented Design]], which is centered on the problem definition rather than the data itself.
- Treats the schema of the data as a second-class citizen and does not assume the design needs to exist anywhere other than in a document, making progress instead through high-level code that controls sequences of events and gives temporary meaning to the data.
- Prioritizes the most probable input to direct the choice of algorithm, favoring being simple and replaceable over being extendable, since extendability can be added later (with unit tests as a safety net) and future-proof systems rarely are.
- Is current rather than historical or future-facing: it does not carry forward the history of a past solution and does not build in generic solutions for problems that have not yet arisen.
- Keeps data and operations separate, coupling them only by [[Coupling Data to Aspect|aspect]] rather than binding them together inside objects, which makes handling change and refactoring more tractable than in [[Object-Oriented Design]].
- Is product- and workflow-specific, much like domain-driven design: data can be generic by type but is not generic in how it is used, so one learns to practice data-oriented design directly on a given problem rather than adding it on top of an existing project.

[^1]: [Data-Oriented Design](zotero://open-pdf/library/items/QRB7VVMF?page=9&annotation=KCSC4APW)
