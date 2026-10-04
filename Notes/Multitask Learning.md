---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Multitask Learning[^1]
> Training a single model to predict several related targets simultaneously, e.g. using ancillary data (age, sex, blood pressure) as additional *outputs*, i.e. extra sources of ground truth, rather than as additional inputs.

# Properties
- In deep learning, a network trained to solve several related problems concurrently (e.g. several image-understanding tasks); since all require some shared understanding of the input, performance on each may improve. A regularizer that exploits additional labels, related to [[Transfer Learning]].[^3]
- Can be easier than training on one target at a time, since many related targets provide more signal, nudging the model toward more accurate internal assessments.[^1]
- Multitask models trained faster, reached higher accuracy, and were more transparent, making problems easier to identify.[^1]
- Ancillary outputs act as a control that makes the model more robust and gives insight into cases where the main predictions fail.[^2]
- A tool for [[Interpretability (Machine Learning)]], often combined with [[Saliency Map|saliency maps]].

[^1]: [Christian, 2021, p. 111](zotero://open-pdf/library/items/P27SWKW4?page=111&annotation=KW37DVJD); [Christian, 2021, p. 111](zotero://open-pdf/library/items/P27SWKW4?page=111&annotation=FTZK794T); [Christian, 2021, p. 111](zotero://open-pdf/library/items/P27SWKW4?page=111&annotation=UUM2F6AL); [Christian, 2021, p. 111](zotero://open-pdf/library/items/P27SWKW4?page=111&annotation=YQMQ2MXJ)
[^2]: [Christian, 2021, p. 112](zotero://open-pdf/library/items/P27SWKW4?page=112&annotation=2VA99TIU)
[^3]: [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=MQMA5H9E); [Prince, p. 152](zotero://open-pdf/library/items/BWT7FYX5?page=166&annotation=LIV8ZJ3B)
