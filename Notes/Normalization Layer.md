---
tags:
  - computer_science
  - computer_vision
---

# Definition

Layer in [[Deep Neural Network|DNNs]] that are nonlinearity that perturb each neuron based on the collective behavior of the [[Set|set]] of neurons.[^1]

# Types

- [[Batch Normalization|Batch Normalization]]
- [[L2 Normalization|L2 Normalization]]
- [[Layer Normalization|Layer Normalization]]
- [[Group Normalization|Group Normalization]]
- [[Instance Normalization]]
- [[Ghost Batch Normalization]]

![[Normalization Schemes.png]]

# Properties
- The schemes differ in which axes (batch index, channel, spatial position) the normalizing statistics are computed over; all use a learned scale and offset per channel.[^2]
- Normalizing the network weights rather than the activations (weight normalization, Salimans & Kingma, 2016) has been less empirically successful.[^3]

[^1]: https://visionbook.mit.edu/neural_nets.html
[^2]: [Prince, p. 203](zotero://open-pdf/library/items/BWT7FYX5?page=217&annotation=E94CD4T3); [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=WQAIWEGA)
[^3]: [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=IWF2TIB4)