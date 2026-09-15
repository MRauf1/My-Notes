---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Hypothesis Space)[^1]
> The set $\mathcal{F}$ of all possible functions under consideration by a learner as candidates for the [[Learned Function]], e.g. "all mappings from $\mathbb{R}^2 \to \mathbb{R}$" or "all functions $\mathbb{R} \times \mathbb{R} \to \mathbb{R}_{\geq 0}$ satisfying the conditions of being a distance metric."

# Properties
- Fully defining a learning algorithm requires specifying not just the hypothesis space itself, but also how it is **parameterized**; e.g. the space of affine functions $\mathbb{R} \to \mathbb{R}$ can be parameterized as $y = \theta_1 x + \theta_0$, or, equivalently as a set, as $y = \theta_2\theta_1 x + \theta_0$.
- Two parameterizations that represent exactly the same hypothesis space are nonetheless not equivalent for learning, because optimizers and [[Objective Function|objectives]] can treat different parameterizations differently.
- An [[Overparameterized Model]] uses a parameterization with more parameters than the minimum necessary to represent the needed functions; most neural networks used in computer vision are overparameterized.
- In [[Metalearning]], the hypothesis space is the set of all learning algorithms, rather than a set of ordinary input-output functions.
- In [[Empirical Risk Minimization]], the learned function is chosen from the hypothesis space to minimize average loss over the training data.
- Places a hard constraint on the search for a solution: unlike data or a [[Regularization|prior]], which apply soft constraints that can be violated at a penalty, if the true solution is not in the hypothesis space, no amount of data or priors can help find it. This is like the joke of a drunk man searching for his lost keys only under a lamppost, "because this is where the light is."

[^1]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)
