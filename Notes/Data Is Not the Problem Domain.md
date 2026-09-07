---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Data Is Not the Problem Domain[^1]
> The first founding principle of [[Data-Oriented Design]]: the real-world problem being solved is not the same thing as the data used to solve it, since meaning is not inherent in data — meaning is applied to data to create information.

# Properties
- Because meaning is not inherent in data, [[Data-Oriented Design]] keeps the real-world problem domain out of the code, leaving it in the design document instead, at some cost to the human readability that [[Object-Oriented Design]] gains by building the problem domain directly into objects.
- Discarding meaning from data reduces the chance of tangling facts with their contexts, which in turn reduces the likelihood of mixing unrelated data together just to serve a single operation or two.

[^1]: [Data-Oriented Design](zotero://open-pdf/library/items/QRB7VVMF?page=9&annotation=TWL4EDH3)
