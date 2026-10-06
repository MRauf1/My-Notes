---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Cascaded Diffusion Model[^1]
> A pipeline of [[Diffusion Model|diffusion models]] for high-resolution generation: the first model generates a low-resolution image (possibly guided by class information), and each subsequent model generates a higher-resolution image conditioned on the previous output, which is resized and appended to the layers of its [[U-Net]] along with any other class information (Ho et al., 2022).

# Properties
- Each stage solves an easier problem: global structure at low resolution, detail via conditional super-resolution (cf. [[SRGAN]]).
- Conditioning-input corruption (noising or blurring the low-resolution input during training) makes later stages robust to the imperfect outputs of earlier ones.
- An alternative route to high resolution is the [[Latent Diffusion Model]].

[^1]: [Prince, p. 368](zotero://open-pdf/library/items/BWT7FYX5?page=382&annotation=5GEFQ5BZ)
