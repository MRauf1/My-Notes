---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Concatenated ReLU[^1]
> A variant of the [[ReLU Function|ReLU]] (Shang et al., 2016) that produces two outputs, one clipped below zero and one clipped above zero:
> $$
> \begin{align}
> \mathrm{CReLU}[z] = \left(\mathrm{ReLU}[z],\ \min[z, 0]\right)
> \end{align}
> $$

# Properties
- Equivalent up to sign to the original formulation $(\mathrm{ReLU}[z], \mathrm{ReLU}[-z])$; it doubles the number of activations.
- Keeps information from negative pre-activations, avoiding the [[Dying ReLU Problem]].

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=QC3TLEG7)
