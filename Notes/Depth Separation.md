---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Depth Separation)[^1]
> A theoretical result establishing that certain classes of functions can be represented by a depth-$d$ neural network using only a polynomial number of neurons, but require an exponential number of neurons to represent at some shallower depth $d' < d$.

# Properties
- Also called the **depth efficiency** of neural networks: some functions realized by deep networks cannot be realized by any shallow network whose capacity is bounded above exponentially.[^2]
- Known results: for any integer $k$, there are networks with one input, one output, and $O[k^3]$ layers of constant width that cannot be realized with $O[k]$ layers and fewer than $2^k$ units of width (Telgarsky, 2016); with multivariate inputs, there is a three-layer network that no two-layer network with capacity sub-exponential in the input dimension can realize (Eldan & Shamir, 2016); and for a broad class of functions, including univariate ones, shallow networks need exponentially more hidden units than deep ones for a given approximation-error bound (Liang & Srikant, 2016). See also Cohen et al. (2016), Safran & Shamir (2017), and Poggio et al. (2017).[^2]
- It is unclear whether the real-world functions we want to approximate fall into this category.[^3]
- The converse, [[Width Efficiency]], has only a polynomial lower bound, suggesting depth matters more than width.
- Gives a partial theoretical explanation for the empirical observation that deep networks often require far fewer parameters to fit data than wide (shallow) networks of comparable capacity.
- An ongoing area of research into why and when depth, rather than width, is an effective way to increase a [[Deep Neural Network|network's]] capacity.

[^1]: [MIT Vision Book - Neural Networks](https://visionbook.mit.edu/neural_nets.html)
[^2]: [Prince, p. 53](zotero://open-pdf/library/items/BWT7FYX5?page=67&annotation=H2Z8VKIL); [Prince, p. 53](zotero://open-pdf/library/items/BWT7FYX5?page=67&annotation=ZW4TBQ2Z)
[^3]: [Prince, p. 50](zotero://open-pdf/library/items/BWT7FYX5?page=64&annotation=Z47Q3DJK)
