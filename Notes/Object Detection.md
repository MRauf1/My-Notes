---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Object Detection[^1]
> The task of locating (typically with bounding boxes) and classifying the objects present in an image.

# Types
- **Proposal-based (two-stage)**: a [[Convolutional Neural Network|CNN]] ingests the whole image and proposes regions that might contain objects; the regions are resized and a second network establishes whether there is an object there and what it is (e.g. the R-CNN family).[^1]
- **Proposal-free (single-stage)**: all processing is performed in a single pass (e.g. YOLO, SSD).[^2]

# Properties
- Single-stage detectors face extreme foreground–background class imbalance, addressed e.g. by [[Focal Loss]].

[^1]: [Prince, p. 183](zotero://open-pdf/library/items/BWT7FYX5?page=197&annotation=QTWS4IU5)
[^2]: [Prince, p. 184](zotero://open-pdf/library/items/BWT7FYX5?page=198&annotation=EBCDYKYD)
