---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Training Phase)[^1]
> The phase of [[Machine Learning|learning]] in which an algorithm is searched for that performs well on past instances of a problem, given as **training data**.

# Properties
- Followed by the [[Testing Phase]], in which the learned algorithm is deployed to solve new instances of the problem.
- In [[Supervised Learning]], training searches for a functional mapping that explains observed example input-output behavior.
- The **training set** $\{\mathbf{x}_1, \dots, \mathbf{x}_N\}$ is used to tune the parameters of an adaptive model; in supervised problems each input comes with a known **target vector** $\mathbf{t}$ (e.g. obtained by hand-labelling), and training determines the precise form of the learned function $\mathbf{y}(\mathbf{x})$, whose outputs are encoded in the same way as the targets.[^2]
- Also called the **learning phase**; finding parameters $\hat{\boldsymbol{\phi}} = \arg\min_{\boldsymbol{\phi}} L[\boldsymbol{\phi}]$ is termed **model fitting**, **training**, or **learning**. The basic method initializes the parameters randomly and repeatedly steps in the most steeply downhill direction of the loss until the gradient is flat ([[Gradient Descent]]); the result is then deployed via [[Inference (Machine Learning)|inference]].[^3]

[^1]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)
[^2]: [Bishop, 2006, p. 2](zotero://open-pdf/library/items/5G99AZ8U?page=22&annotation=TMH98CJ6)
[^3]: [Prince, p. 18](zotero://open-pdf/library/items/BWT7FYX5?page=32&annotation=FJJLVJX4); [Prince, p. 22](zotero://open-pdf/library/items/BWT7FYX5?page=36&annotation=P5GMFW68)
