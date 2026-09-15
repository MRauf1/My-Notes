---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Hebbian Learning)[^1]
> An alternative to [[Backpropagation]] for training neural networks, in which neurons wire up based only on the feedforward pattern of activity in the network, rather than on error feedback. The canonical learning rule, **Hebb's rule**, is "fire together, wire together": the weight of the connection between two neurons is increased whenever the two neurons are active at the same time.

# Properties
- A bottom-up approach, in contrast to backpropagation, which is top-down: errors incurred at the output are propagated backward to inform earlier layers how to update.
- Does not explicitly minimize a [[Loss Function|loss function]], yet has been shown to lead to effective neural representations, such as infomax representations that capture as much information as possible about the input signal in the neural activations, and networks that act like memory banks.
- Considered more biologically plausible than backpropagation, because Hebb's rule can be computed locally: each neuron updates its weights based only on the activity of adjacent neurons, whereas backpropagation requires coordinating updates globally throughout the network, a form of coordination not currently known to occur in biological brains.

[^1]: [MIT Vision Book - Neural Networks](https://visionbook.mit.edu/neural_nets.html)
