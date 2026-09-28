---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Feature Visualization[^1]
> Techniques that render what a neural network's units or classes respond to as images, e.g. Zeiler and Fergus's *deconvolution*, which maps intermediate activations back into image space, or optimising an input image (starting from random static) to maximise the probability of a chosen label.

# Types
- *Class maximisation* - tweak pixels of noise to maximise a class score (Mordvintsev, Olah, Tyka, 2015).[^1]
- *DeepDream* - start from a real image and amplify whatever neurons are already most active, creating a feedback loop in which faint patterns (a cloud resembling a bird) become vivid hallucinations.[^2]

# Properties
- Reveals when a network is not looking for what we thought: "dumbbell" visualisations included disembodied arms, since dumbbells were never seen without lifters, exposing training mishaps.[^3]
- Useful for auditing bias: if maximising "face" yields only white male faces, the network likely recognises other faces less readily ([[Algorithmic Bias]]).[^3]
- Suggests an artistic practice: with good taste, random variation, and time, anyone who can tell good from bad art can create.[^4]
- A technique of [[Interpretability (Machine Learning)]].

[^1]: [Christian, 2021, p. 114](zotero://open-pdf/library/items/P27SWKW4?page=114&annotation=UAKMBLYG); [Christian, 2021, p. 115](zotero://open-pdf/library/items/P27SWKW4?page=115&annotation=T736ZP2N)
[^2]: [Christian, 2021, p. 115](zotero://open-pdf/library/items/P27SWKW4?page=115&annotation=KXY2ZSCM)
[^3]: [Christian, 2021, p. 116](zotero://open-pdf/library/items/P27SWKW4?page=116&annotation=PLK7ELMW)
[^4]: [Christian, 2021, p. 116](zotero://open-pdf/library/items/P27SWKW4?page=116&annotation=WQX6C8RQ)
